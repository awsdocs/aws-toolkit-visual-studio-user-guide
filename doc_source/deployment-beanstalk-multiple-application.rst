.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-multiple:

###############################################
Multiple Application Support for .NET and |EB|
###############################################

.. meta::
   :description: Deploying multiple apps to Elastic Beanstalk.
   :keywords: mulitple apps, deployment, Elastic Beanstalk

Using the deployment manifest, you have the ability to deploy multiple applications to the same 
|EB| environment. 

The deployment manifest supports `ASP.NET Core <http://www.asp.net/core>`_ web applications as well 
as msdeploy archives for traditional ASP.NET applications. Imagine a scenario where you have written 
a new amazing application using ASP.NET Core for the frontend and a Web API project for an 
extensions API. You also have an admin app that you wrote using traditional ASP.NET. 
 
The toolkit's deployment wizard focuses on deploying a single project. To take advantage of multiple 
application deployment, you have to construct the application bundle by hand. To start, write the 
manifest. For this example, you will write the manifest at the root of your solution. 

The deployment section in the manifest has two children: an array of ASP.NET Core web applications to 
deploy, and an array of msdeploy archives to deploy. For each application, you set the IIS 
path and the location of the application’s bits relative to the manifest. 

.. code-block:: json

   {
     "manifestVersion": 1,
     "deployments": {
    
       "aspNetCoreWeb": [
         {
           "name": "frontend",
           "parameters": {
             "appBundle": "./frontend",
             "iisPath": "/frontend"
           }
         },
         {
           "name": "ext-api",
           "parameters": {
             "appBundle": "./ext-api",
             "iisPath": "/ext-api"
           }
         }
       ],
       "msDeploy": [
         {
           "name": "admin",
           "parameters": {
             "appBundle": "AmazingAdmin.zip",
             "iisPath": "/admin"
           }
         }
       ]
     }
   }

With the manifest written, you’ll use Windows PowerShell to create the application bundle and update an 
existing |EB| environment to run it. The script is written assuming that it will be run from the 
folder containing your Visual Studio solution. 

The first thing you need to do in the script is setup a workspace folder in which to create the 
application bundle. 

.. code-block:: ps1con

   $publishFolder = "c:\temp\publish"
   
   $publishWorkspace = [System.IO.Path]::Combine($publishFolder, "workspace")
   $appBundle = [System.IO.Path]::Combine($publishFolder, "app-bundle.zip")
   
   If (Test-Path $publishWorkspace){
   	Remove-Item $publishWorkspace -Confirm:$false -Force
   }
   If (Test-Path $appBundle){
   	Remove-Item $appBundle -Confirm:$false -Force
   }

Once you've created the folder, it is time to get the frontend ready. As with the deployment wizard, 
use the dotnet CLI to publish the application. 

.. code-block:: ps1con

   Write-Host 'Publish the ASP.NET Core frontend'  
   $publishFrontendFolder = [System.IO.Path]::Combine($publishWorkspace, "frontend")
   dotnet publish .\src\AmazingFrontend\project.json -o $publishFrontendFolder -c Release -f netcoreapp1.0

Notice that the subfolder "frontend" was used for the output folder, matching the folder you set in 
the manifest. Now you need to do the same for the Web API project.

.. code-block:: ps1con

   Write-Host 'Publish the ASP.NET Core extensibility API'
   $publishExtAPIFolder = [System.IO.Path]::Combine($publishWorkspace, "ext-api")
   dotnet publish .\src\AmazingExtensibleAPI\project.json -o $publishExtAPIFolder -c Release -f netcoreapp1.0

The admin site is a traditional ASP.NET application, so you can't use the dotnet CLI. For the admin 
application, you should use msbuild, passing in the build target package to create the msdeploy 
archive. By default the package target creates the msdeploy archive under the 
:code:`obj\Release\Package` folder, so you will need to copy the archive to the publish workspace.

.. code-block:: ps1con

   Write-Host 'Create msdeploy archive for admin site'
   msbuild .\src\AmazingAdmin\AmazingAdmin.csproj /t:package /p:Configuration=Release
   Copy-Item .\src\AmazingAdmin\obj\Release\Package\AmazingAdmin.zip $publishWorkspace

To tell the |EB| environment what to do with all these applications, copy the 
manifest from your solution to the publish workspace and then zip up the folder. 

.. code-block:: ps1con

   Write-Host 'Copy deployment manifest'
   Copy-Item .\aws-windows-deployment-manifest.json $publishWorkspace

   Write-Host 'Zipping up publish workspace to create app bundle'
   Add-Type -assembly "system.io.compression.filesystem"
   [io.compression.zipfile]::CreateFromDirectory( $publishWorkspace, $appBundle)

Now that you have the application bundle, you could go to the web console and upload the archive to 
a |EB| environment. Alternatively, you can continue to use the AWS PowerShell cmdlets to update the 
|EB| environment with the application bundle. Make sure you have set the current profile and region 
to the profile and region that contains your |EB| environment by using :code:`Set-AWSCredentials` 
and :code:`Set-DefaultAWSRegion` cmdlets. 

.. code-block:: ps1con

   Write-Host 'Write application bundle to S3'
   # Determine S3 bucket to store application bundle
   $s3Bucket = New-EBStorageLocation
   Write-S3Object -BucketName $s3Bucket -File $appBundle
   
   
   $applicationName = "ASPNETCoreOnAWS"
   $environmentName = "ASPNETCoreOnAWS-dev"
   $versionLabel = [System.DateTime]::Now.Ticks.ToString()
   
   Write-Host 'Update Beanstalk environment for new application bundle'
   New-EBApplicationVersion -ApplicationName $applicationName -VersionLabel $versionLabel -SourceBundle_S3Bucket $s3Bucket -SourceBundle_S3Key app-bundle.zip
   Update-EBEnvironment -ApplicationName $applicationName -EnvironmentName $environmentName -VersionLabel $versionLabel

Now, check the status of the update using either the |EB| environment status page in either the 
toolkit or the web console. Once complete you will be able to navigate to each of the 
applications you deployed at the IIS path set in the deployment manifest. 
