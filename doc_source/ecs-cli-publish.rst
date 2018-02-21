.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _working-with-dotnet-cli:



#####################################################
Deploying an |ECSlong| Project with the .NET Core CLI
#####################################################

.. meta::
   :description: Using the .NET Core CLI to manage an AWS ECS Container
   :keywords: Management, Publish, Deployment, EC2 Container Service, .NET Core, Docker, CLI

The |TVSlong| includes |ECSlong| .NET Core project templates for Visual Studio. You must have Visual
Studio 2017 installed with the .NET Core cross-platform development workload, 
`Docker <https://docs.docker.com/engine/installation>`_ and the |TVS|. You can deploy Docker containers 
built in Visual Studio using the .NET Core command line interface (CLI).

.. toctree::
    :titlesonly:
    :maxdepth: 1

Listing the |ECS| Commands Available through the CLI
====================================================

The .NET CLI include commands for deploying to |ECS| and managing Docker images. 

#. Open a command prompt and navigate to the folder containing a Visual Studio ASP.NET Core 2.0 project with
   Docker support.

#. Type :code:`dotnet ecs --help`.

 .. code:: sh

    C:\ECS\ASPNETCoreSample\ASPNETCoreSample>dotnet ecs --help

        Amazon EC2 Container Service Tools for .NET Core applications (0.8.0)
        Project Home: http://github.com/aws/aws-dotnetcli-extensions

        Commands to deploy to Amazon EC2 Container Service:

            deploy-service          Push the application to ECR and runs the application as a long lived service on the ECS Cluster.
            deploy-scheduled-task   Push the application to ECR and then sets up CloudWatch Event Schedule rule to run the application.
            deploy-task             Push the application to ECR and then runs it as a task on the ECS Cluster.

        Commands to manage docker images to Amazon EC2 Container Registry:

            push-image              Execute "dotnet publish", "docker build" and then push the image to Amazon ECR.

        To get help on individual commands execute:

            dotnet ecs help <command>            


Deploying an ASP.NET Core 2.0 Project as a Service from the .NET Core CLI
=========================================================================

The following instructions assume you've used Visual Studio to create an ASP.NET Core 2.0 project with
Docker support.

#. Open a command prompt and navigate to the folder containing your Visual Studio .NET Core |LAM| project.

#. Type :code:`dotnet ecs deploy-service`.

Pushing an Image to the |ECR|
=============================

The following instructions assume you've used Visual Studio to create an ASP.NET Core 2.0 project with
Docker support.

#. Open a command prompt and navigate to the folder containing your Visual Studio .NET Core |LAM| project.

#. Type :code:`dotnet ecs push-image`.

