.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-ecs-deploy-credentials:

############################################################
Specify AWS  Credentials for Your ASP.NET Core 2 Application
############################################################

.. meta::
   :description: Specify security credentials using the Toolit for Visual Studio.
   :keywords: deployment, security, credentials, EC2 Container Service, .NET Core, Docker

There are two types of credentials in play when you deploy your application to a Docker
container: deployment credentials and instance credentials. 

Deployment credentials are used by the Publish Container to AWS wizard
to create the environment in |ECS|. This includes things like tasks, services, IAM roles,
a Docker container repository, and if you choose, a load balancer. 

Instance credentials are used by the instance (including your application) to access
different |AWS| services. For example, if your an ASP.NET Core 2.0 application 
reads and writes to |S3| objects, it will need appropriate permissions. You can
provide different credentials using different methods based on the environment. 
For example, your ASP.NET Core 2 application might target *Development* and *Production* 
environments. You could use a local Docker instance and credentials for development and  
a defined role in production.

.. _tkv-ecs-deploy-creds:

Specifying deployment credentials   
=================================

The AWS account you specify in the :guilabel:`Publish Container to AWS` wizard 
is the AWS account the wizard will use for deployment to |ECS|. The account
profile must have permissions to |EC2long|, |ECSLong|, and |IAMlong|.

If you notice options missing from drop-down lists, it may be because you lack
permissions. For example, if you created a cluster for your application but do not 
see it on the :guilabel:`Publish Container to AWS` wizard Cluster page. If this happens,
add the missing permissions and try the wizard again.

.. _tkv-ecs-dev-creds:

Specifying development instance credentials
===========================================

For non-production environments, you can configure your credentials in the
appsettings.<environment>.json file. For example, to configure your credentials 
in the appsettings.Development.json file in Visual Studio 2017:

#. Add the AWSSDK.Extensions.NETCore.Setup NuGet package to your project.

#. Add AWS settings to appsettings.Development.json. 
   The configuration below sets :code:`Profile` and :code:`Region`. 

    .. code-block:: js

        {                                                                                   
            "AWS": {
                "Profile": "local-test-profile",
                "Region": "us-west-2"
            }
        }


.. _tkv-ecs-dev-creds:

Specifying production instance credentials
===========================================

For production instances, we recommend you use an |IAM| role to control what your application
(and the service) can access. For example, to configure an |IAM| role with |ECS| as the 
service principal with permissions to |S3long| and |DDBlong| from the |console|:

#. Sign in to the |console| and open the |IAM| console at https://console.aws.amazon.com/iam/.

#. In the navigation pane of the |IAM| console, choose Roles, and then choose Create role.

#. Choose the :guilabel:`AWS Service` role type, and then choose 
   :guilabel:`EC2 Container Service`.

#. Choose the :guilabel:`EC2 Container Service Task` use case. Use cases are defined by the 
   service to include the trust policy that the service requires. Then choose 
   :guilabel:`Next: Permissions`.

#. Choose the :guilabel:`AmazonS3FullAccess` and :guilabel:`AmazonDynamoDBFullAccess` permissions 
   policies. Check the box next to each policy, and then choose :guilabel:`Next: Review`,

#. For :guilabel:`Role name`, type a role name or role name suffix to help you identify the purpose 
   of this role. Role names must be unique within your AWS account. They are not distinguished by 
   case. For example, you cannot create roles named both :code:`PRODROLE` and :code:`prodrole`. 
   Because various entities might reference the role, you cannot edit the name of the role after 
   it has been created.

#. (Optional) For :guilabel:`Role description`, type a description for the new role.

#. Review the role and then choose :guilabel:`Create role`.

You can use this role as the :guilabel:`task role` on the :guilabel:`ECS Task Definition` page 
of the :guilabel:`Publish Container to AWS` wizard. 

For more information, see :IAM-ug:`Using Service-Based Roles <using-service-linked-roles>`.

