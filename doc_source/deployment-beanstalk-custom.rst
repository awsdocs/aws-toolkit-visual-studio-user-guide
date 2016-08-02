.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-custom:

################################################
Custom Elastic Beanstalk Application Deployments
################################################

This topic describes how the deployment manifest for |EB|'s Microsoft Windows container 
supports custom application deployments.

Custom application deployments are a powerful feature for advanced users who want to leverage the 
power of |EB| to create and manage their AWS resources, but want complete control on how their 
application is deployed. For a custom application deployment, you create Windows PowerShell scripts for the 
three different actions |EB| performs. The install action is used when a deployment is initiated, 
restart is used when the :code:`RestartAppServer` API is called from either the toolkit or the web 
console, and uninstall which is invoked on any previous deployment whenever a new deployment occurs. 

For example, you might have an ASP.NET application that you want to deploy while your documentation 
team has written a static website that they want included with the deployment. You can do that by 
writing your deployment manifest like this:

.. code-block:: json

   {
     "manifestVersion": 1,
     "deployments": {
    
       "msDeploy": [
         {
           "name": "app",
           "parameters": {
             "appBundle": "CoolApp.zip",
             "iisPath": "/"
           }
         }
       ],
       "custom": [
         {
           "name": "PowerShellDocs",
           "scripts": {
             "install": {
               "file": "install.ps1"
             },
             "restart": {
               "file": "restart.ps1"
             },
             "uninstall": {
               "file": "uninstall.ps1"
             }
           }
         }
       ]
     }
   }

   
The scripts listed for each action must be in the application bundle relative to the deployment 
manifest file. For this example, the application bundle will also contain a documentation.zip file 
which contains a static website created by your documentation team. 

The :file:`install.ps1` script extracts the zip file and sets up the IIS Path. 

.. code-block:: ps1con

   Add-Type -assembly "system.io.compression.filesystem"
   [io.compression.zipfile]::ExtractToDirectory('./documentation.zip', 'c:\inetpub\wwwroot\documentation')
   
   powershell.exe -Command {New-WebApplication -Name documentation -PhysicalPath  c:\inetpub\wwwroot\documentation -Force}

Since your application is running in IIS, the restart action will invoke an IIS reset. 

.. code-block:: ps1con

   iisreset /timeout:1

For uninstall scripts, it is important to clean up all settings and files used during the install 
stage. That way during the install phase for the new version, you can avoid any collision with 
previous deployments. For this example, you need to remove the IIS application for the static 
website and remove the website files. 

.. code-block:: ps1con

   powershell.exe -Command {Remove-WebApplication -Name documentation}
   Remove-Item -Recurse -Force 'c:\inetpub\wwwroot\documentation'

With these script files and the documentation.zip file included in your application bundle, the 
deployment creates the ASP.NET application and then deploys the documentation site. 

For this example, we choose a simple example that deploys a simple static website, but with custom 
application deployment you can deploy any type of application and let |EB| manage the 
AWS resources for it. 
