.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-ecs:

#######################################
Deploying to |EC2| Container Service
#######################################

.. meta::
   :description: Deploying to EC2 Container Service using the Toolkit for Visual Studio.
   :keywords: deployment, EC2 Container Service, Docker

|ECSlong| is a highly scalable, high performance container
management service that supports Docker containers and allows you to easily run 
applications on a managed cluster of Amazon EC2 instances. 

To deploy applications on |ECSlong|, your application components must be developed 
to run in a Docker container. A Docker container is a standardized unit of software development, 
containing everything that your software application needs to run: code, runtime, 
system tools, system libraries, etc. 

The |TVS| provides a wizard that simplifies publishing applications through |ECS|. This wizard
is described in the following sections.

For more information about |ECS|, go to the :ECS-dg:`Elastic Container Service documentation <Welcome>`. 
It includes an overview of :ECS-dg:`Docker basics <docker-basics>` and
:ECS-dg:`creating a cluster <create_cluster>`.

.. toctree::
    :titlesonly:
    :maxdepth: 1

    Specify AWS Credentials <deployment-ecs-specify-credentials>
    Deploy an ASP.NET Core 2.0 App (Fargate) <deployment-ecs-aspnetcore-fargate>
    Deploy an ASP.NET Core 2.0 App (EC2) <deployment-ecs-aspnetcore-ec2>
