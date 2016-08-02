.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-custom-netcore:

####################################
Custom ASP.NET Core |EB| Deployments
####################################
 
This topic describes how deployment works and what you can do customize deployments when creating 
ASP.NET Core applications with |EB| and the |TVS|.

After you complete the deployment wizard in the |TVS|, the toolkit bundles 
the application and sends it to |EB|. Your first step in creating the application bundle is 
to use the new dotnet CLI to prepare the application for publishing by using the **publish** command. 
The framework and configuration are passed down from the settings in the wizard to the **publish** 
command. So if you selected **Release** for :code:`configuration` and **netcoreapp1.0** for the 
:code:`framework`, the toolkit will execute the following command:

:code:`dotnet publish --configuration Release --framework netcoreapp1.0`

When the **publish** command finishes, the toolkit writes the new deployment manifest into the 
publishing folder. The deployment manifest is a JSON file named 
**aws-windows-deployment-manifest.json**, which the |EB| Windows container (version 1.2 
or later) reads to determine how to deploy the application. For example, for an ASP.NET Core 
application you want to be deploy at the root of IIS, the toolkit generates a manifest file that 
looks like this: 

.. code-block:: json

   {
     "manifestVersion": 1,
     "deployments": {
    
       "aspNetCoreWeb": [
         {
           "name": "app",
           "parameters": {
             "appBundle": ".",
             "iisPath": "/",
             "iisWebSite": "Default Web Site"
           }
         }
       ]
     }
   }

The :code:`appBundle` property indicates where the application bits are in relation to the manifest 
file. This property can point to either a directory or a ZIP archive. The :code:`iisPath` and 
:code:`iisWebSite` properties indicate where in IIS to host the application. 
 
.. _tkv-deploy-beanstalk-custom-netcore-manifest:

Customizing the Manifest 
------------------------

The toolkit only writes the manifest file if one doesn't already exist in the publishing folder. If 
the file does exist, the toolkit updates the :code:`appBundle`, :code:`iisPath` and 
:code:`iisWebSite` properties in the first application listed under the :code:`aspNetCoreWeb` 
section of the manifest. This allows you to add the **aws-windows-deployment-manifest.json** to your 
project and customize the manifest. To do this for an ASP.NET Core Web application in Visual Studio 
add a new JSON file to the root of the project and name it **aws-windows-deployment-manifest.json**. 

The manifest must be named **aws-windows-deployment-manifest.json** and it must be at the root of 
the project. The |EB| container looks for the manifest in the root and if it finds it 
will invoke the deployment tooling. If the file doesn't exist, the |EB| container falls 
back to the older deployment tooling, which assumes the archive is an **msdeploy** archive. 

To ensure the dotnet CLI :code:`publish` command includes the manifest, update the :file:`project.json` 
file to include the manifest file in the include section under :code:`include` in 
:code:`publishOptions`. 

.. code-block:: json

   {
      "publishOptions": {
        "include": [
          "wwwroot",
          "Views", 
          "Areas/**/Views", 
          "appsettings.json",
          "web.config", 
          "aws-windows-deployment-manifest.json"
        ]
      }
    }

Now that you've declared the manifest so that it's included in the app bundle, you can further 
configure how you want to deploy the application. You can customize deployment beyond what the 
deployment wizard supports. AWS has defined a JSON schema for the 
**aws-windows-deployment-manifest.json file**, and when you installed the |TVS|, the setup 
registered the URL for the schema. 

When you open :file:`windows-deployment-manifest.json`, you'll see the schema URL selected in the 
Schema drop down box. You can navigate to the URL to get a full description of what can be set in the 
manifest. With the schema selected, Visual Studio will provide IntelliSense while you're editing the 
manifest. 
 
One customization you can do is to configure the IIS application pool under 
which the application will run. The following example  shows how you can define an IIS Application 
pool ("customPool") that recycles the process every 60 minutes, and assigns it to the application 
using :code:`"appPool": "customPool"`.

.. code-block:: json

  {
    "manifestVersion": 1,
    "iisConfig": {
      "appPools": [
        {
          "name": "customPool", 
          "recycling": {
            "regularTimeInterval": 60
          }
        }
      ]
    },
    "deployments": {
      "aspNetCoreWeb": [ 
        {
          "name": "app", 
          "parameters": { 
            "appPool": "customPool"
          }
        }
      ]
    }
  }
 
Additionally, the manifest can declare Windows PowerShell scripts to run before and after the install, 
restart and uninstall actions. For example, the following manifest runs the Windows PowerShell script 
:file:`PostInstallSetup.ps1` to do further setup work after the ASP.NET Core application is 
deployed to IIS. When adding scripts like this, make sure the scripts are added to the include 
section under publishOptions in the :file:`project.json` file, just as you did with the 
:file:`aws-windows-deployment-manifest.json` file. If you don't, the scripts won't be included as 
part of the dotnet CLI **publish** command. 

.. code-block:: json

  {
    "manifestVersion": 1,
    "deployments": {
      "aspNetCoreWeb": [ 
        {
          "name": "app", 
          "scripts": { 
            "postInstall": {
              "file": "SetupScripts/PostInstallSetup.ps1" 
            }
          }
        }
      ]
    }
  }
 
.. _tkv-deploy-beanstalk-custom-netcore-ebextensions:
 
What about ebextensions? 
------------------------

The |EB| **ebextensions** configuration files are supported as with all the other 
|EB| containers. To include ebextensions in an ASP.NET Core application, add the 
:file:`.ebextensions` directory to the :code:`include` section under :code:`publishOptions` in the 
:file:`project.json` file. For further information about ebextensions checkout the 
:eb-dg:`Elastic Beanstalk Developer Guide <ebextensions>`. 
