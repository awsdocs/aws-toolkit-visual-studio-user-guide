.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _deployment-ecs-aspnetcore-ec2:

################################################
Deploying an ASP.NET Core 2.0 App to |ECS| (EC2)
################################################

.. meta::
   :description: Deploying ASP.NET Core 2.0 application to EC2 Container Service.
   :keywords: deployment, EC2 Container Service, .NET Core, Docker

This section describes how to use the :guilabel:`Publish Container to AWS` wizard,
provided as part of the |TVS|, to deploy a containerized ASP.NET Core 2.0 application targeting
Linux through |ECS| using the EC2 launch type. Because a web application is meant run continuously, 
it will deployed as a service.

.. _tkv-deploy-ecs-netcore-prerequisites:

Before you publish your container
=================================

Before using the :guilabel:`Publish Container to AWS` to deploy your ASP.NET Core 2.0  
application:

* :ref:`Specify your AWS credentials <deployment-ecs-specify-credentials>`_ and 
  :ECS-dg:`get setup with Amazon ECS <get-set-up-for-amazon-ecs>`. 

* `Install Docker <https://docs.docker.com/engine/installation>`_. You have a few
  different installation options including 
  `Docker for Windows <https://docs.docker.com/docker-for-windows/install/>`_.

* :ECS-dg:`Create an Amazon ECS cluster <create-cluster>` based on the needs
  of your web application. It only takes a few steps.

* Create (or open) an ASP.NET Core 2.0 containerized app targeting Linux project in
  Visual Studio 2017. 


.. _tkv_deployment-ecs-netcore-accessing:

Accessing the Publish Container to AWS wizard
=============================================

To deploy an ASP.NET Core 2.0 containerized application targeting Linux, right-click the project 
in the Solution Explorer and select :guilabel:`Publish Container to AWS`. 

You can also select :guilabel:`Publish Container to AWS` on the Visual Studio Build menu.

.. _tkv-deploy-ecs-pubtoaws:

Publish Container to AWS Wizard
===============================

**Account profile to use** - Select an account profile to use. 

**Region** - Choose a deployment region. Profile and region are used to set up your deployment environment
resources and select the default Docker registry.  

**Configuration** - Select the Docker image build configuration. 

**Docker Repository** - Choose an existing Docker repository or type in the name of a new repository 
and it will be created. This is the repository the built container image is pushed to.

**Tag** - Select an existing tag or type in the name of a new tag. Tags can track important
details like version, options or other unique configuration elements of the Docker container.

**Deployment** - Select :guilabel:`Service on an ECS Cluster`. Use this deployment option when your
application is meant to be long-running (like an ASP.NET Core 2.0 web application).

**Save settings to aws-docker-tools-defaults.json and configure project for command line deployment** - Check 
this option if you want the flexibility of deploying from the command line. Use :code:`dotnet ecs deploy` from
your project directory to deploy and :code:`dotnet ecs publish` the container. 

.. _tkv-deploy-ecs-launch-config:

Launch Configuration page
=========================

**ECS Cluster** - Pick the cluster that will run your Docker image. You can :ECS-dg:`create an ECS cluster <create_cluster>` 
using the AWS Management Console.


**Launch Type** - Choose EC2. To use the Fargate launch type, see 
`Deploying an ASP.NET Core 2.0 Application to Amazon ECS (Fargate) <deployment-ecs-aspnetcore-fargate>`_.

.. _tkv-deploy-ecs-service:

Service Configuration page
==========================

**Service** - Select one of the services in the drop-down to deploy your container into an 
existing service. Or choose :guilabel:`Create New` to create a new service. Service 
names must be unique within a cluster, but you can have similarly named services 
in multiple clusters within a region or across multiple regions.

**Number of Tasks** - The number of tasks to deploy and keep running on your cluster. Each 
task is one instance of your container.

**Minimum Healthy Percent** - The percentage of tasks that must remain in :code:`RUNNING`
state during a deployment rounded up to the nearest integer.

**Maximum Percent** - The percentage of tasks that are allowed in the :code:`RUNNING` or 
:code:`PENDING` state during a deployment rounded down to the nearest integer. 

**Placement Templates** - Select a task placement template. 

When you launch a task into a cluster, Amazon ECS must determine where to place the task
based on the requirements specified in the task definition, such as CPU and memory. 
Similarly, when you scale down the task count, Amazon ECS must determine which tasks to terminate. 
 
The placement template controls how tasks are launched into a cluster:  

* AZ Balanced Spread - distribute tasks across Availability Zones and across container instances in the Availability Zone.

* AZ Balanced BinPack - distribute tasks across Availability Zones and across container instances with the least available memory.

* BinPack - distribute tasks based on the least available amount of CPU or memory.

* One Task Per Host - place, at most, one task from the service on each container instance.

For more information, see :ecs-dg:`Amazon ECS Task Placement <task-placement>`. 

.. _tkv-deploy-ecs-app-load-balancer:

Application Load Balancer page
==============================

**Configure Application Load Balancer** - Check to configure an application load balancer.

**Select IAM role for service** - Select an existing role or choose :guilabel:`Create New` and 
a new role will be created.

**Load Balancer** - Select an existing load balancer or choose :guilabel:`Create New` and 
type in the name for the new load balancer. 

**Listener Port** - Select an existing listener port or choose :guilabel:`Create New` and 
type in a port number. The default, port :code:`80`, is appropriate for most web applications. 

**Target Group** - By default, the load balancer sends requests to registered targets using the port and 
protocol that you specified for the target group. You can override this port when you 
register each target with the target group. 

**Path Pattern** - The load balancer will use path-based routing. Accept the default 
:code:`/` or provide a different pattern. The path pattern is case-sensitive, 
can be up to 128 characters in length, and contains a  
`select set of characters <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/application/load-balancer-listeners#path-conditions>`_.

**Health Check Path** - The ping path that is the destination on the targets for health checks.
By default, it is :code:`/` and is appropriate for web applications. Enter a different path
if needed. If the path you enter is invalid, the health check will fail and it will be considered unhealthy.

If you deploy multiple services, and each service will be deployed to a different path or location, 
you might need custom check paths.


.. _tkv-deploy-ecs-task-definition:

ECS Task Definition page
========================

**Task Definition** - Select an existing task definition or choose :guilabel:`Create New` and 
type in the new task definition name. 

**Container** - Select an existing container or choose :guilabel:`Create New` and 
type in the new container name. 

**Memory (MiB)** - Provide values for **Soft Limit** or **Hard Limit** or both.

The *soft limit* (in MiB) of memory to reserve for the container. Docker attempts to
keep the container memory under the soft limit. The container can consume more memory,
up to either the hard limit specified with the memory parameter (if applicable), 
or all of the available memory on the container instance, whichever comes first. 

The *hard limit* (in MiB) of memory to present to the container. If your container attempts to exceed 
the memory specified here, the container is killed.

**Task Role** - Select a task role for an IAM role that allows the container permission to call the 
AWS APIs that are specified in its associated policies on your behalf. This is how credentials are
passed in to your application. See `how to specify AWS security credentials for your application <deployment-ecs-specify-credentials>`_.

**Port Mapping** - Add, modify or delete port mappings for the container. If a load balancer is on, 
the host port will be default to 0 and port assignment will be dynamic.

**Environment Variables** - Add, modify, or delete environment variables for the container.

When you are satisfied with the configuration, click :guilabel:`Publish` to begin the deployment
process. 

.. _tkv-deploy-ecs-publishing:

Publishing Container to AWS
===========================

Events are displayed during deployment. The wizard is automatically closed on 
successful completion. You can override this by unchecking the box at the bottom of the page.

You can find the URL of your new instances in the AWS Explorer. Expand Amazon ECS and Clusters,
then click on your cluster. 
