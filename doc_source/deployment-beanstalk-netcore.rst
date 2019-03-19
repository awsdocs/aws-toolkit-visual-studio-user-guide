.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-netcore:

###############################################
Deploying an ASP.NET Core Application to |EB| 
###############################################

.. meta::
   :description: Deploying ASP.NET Core apps to Elastic Beanstalk.
   :keywords: deployment, Elastic Beanstalk, .NET Core

|AEBlong| is a service that simplifies the process of provisioning AWS resources for your
application. |EBlong| provides all of the AWS infrastructure required to deploy your application. 

The |TVS| supports deploying ASP.NET Core applications to AWS using |EB|. 
ASP.NET Core is the redesign of ASP.NET with a modularized architecture that minimizes 
dependency overhead and streamlines your application to run in the cloud. 

|EBlong| makes it easy to deploy applications in a variety of different languages to AWS. 
|EB| supports both traditional ASP.NET applications and ASP.NET Core applications. This topic 
describes deploying ASP.NET Core applications.

.. _tkv-deploy-using-wizard-netcore:

Using the Deployment Wizard
===========================

The easiest way to deploy ASP.NET Core applications to |EB| is with the |TVS|. 

If you have used the toolkit before to deploy traditional ASP. NET applications, you'll find the 
experience for ASP.NET Core to be very similar. In the steps below, we'll walk through the deployment 
experience. 

If you have never used the toolkit before, the first thing you'll need to do after installing the 
toolkit is register your AWS credentials with the toolkit. See 
:ref:`tkv-deploy-specify-credentials-for-application` for Visual Studio documentation for details on 
how to do so. 

To deploy an ASP.NET Core web application, right-click the project in the Solution Explorer and select 
:guilabel:`Publish to AWS…`. 
 
On the first page of the Publish to |EBlong| deployment wizard, choose to create a new |EB| 
application. An |EB| application is a logical collection of |EB| components, including 
environments, versions, and environment configurations. The deployment wizard generates an application 
that in turn contains a collection of application versions and environments. The environments contain the 
actual AWS resources that run an application version. Every time you deploy an application, a new 
application version is created and the wizard points the environment to that version. You can learn more 
about these concepts in :eb-dg:`Elastic Beanstalk Components. <concepts.components>`.
 
Next, set names for the application and its first environment. Each environment has a 
unique CNAME associated with it that you can use to access the application when the deployment is 
complete. 
 
The next page, **AWS Options**, allows you to configure the type of AWS resources to use. 
For this example, leave the default values, except for the :guilabel:`Key pair` section. Key pairs 
allow you retrieve the Windows administrator password so you can log on to the machine. If you 
haven't already created a key pair you might want to select :guilabel:`Create new key pair`. 
 
.. _tkv-deploy-using-wizard-netcore-permissions:

Permissions
===========

The **Permissions** page is used for assigning AWS credentials to the EC2 instance(s) running your 
application. This is important if your application uses the |sdk-net| to access other AWS 
services. If you are not using any other services from your application then you can leave this page 
at its default. 

.. _tkv-deploy-using-wizard-netcore-app-options:

Application Options
===================

The details on the **Application Options** page are different from those specified when deploying 
traditional ASP.NET applications. Here, you specify the build configuration and framework used to 
package the application, and also specify the IIS resource path for the application. 
 
After completing the **Application Options** page, click :guilabel:`Next` to review the settings, then 
click :guilabel:`Deploy` to begin the deployment process. 

.. _tkv-deploy-using-wizard-netcore-check-status:

Checking Environment Status
===========================

After the application is packaged and uploaded to AWS, you can check the status of the |EB| 
environment by opening the environment status view from the AWS Explorer in Visual Studio.
 
Events are displayed in the status bar as the environment is coming online. Once everything is 
complete, the environment status will move to healthy state. You can click on the URL to view the 
site. From here, you can also pull the logs from the environment, or remote desktop into the |EC2| 
instance(s) that are part of your |EB| environment. 
 
The first deployment of any application will take a bit longer than subsequent re-deployments, as it 
creates new AWS resources. As you iterate on your application during development, you can quickly 
re-deploy by going back through the wizard, or selecting the :guilabel:`Republish` option when you 
right click the project. 
 
Republish packages your application using the settings from the previous run through the deployment 
wizard and uploads the application bundle to the existing |EB| environment.


