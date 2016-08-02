.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _welcome:

###################
Using the |TVS|
###################

.. _welcome.about_tkv:

The |TVS|
=============

The |TVS| is a plugin for the Visual Studio IDE that makes it easier for developers to develop,
debug, and deploy .NET applications that use Amazon Web Services. For details on how to download and
install the kit, see :ref:`install`.

The following AWS Toolkit features enhance the development experience:

AWS Explorer
    AWS Explorer enables you to interact with many of the AWS services from inside the Visual Studio
    IDE. Supported data services include |S3long| (|S3|), |SDB|, |SNSlong| (|SNS|), |SQSlong|
    (|SQS|), and |CFlong|. AWS Explorer also provides access to |EC2long| (|EC2|) management,
    |IAMlong| (|IAM|) user and policy management, and deployment to |CFN|. AWS Explorer supports
    multiple AWS accounts, including IAM user accounts, and enables you to easily change the
    displayed view from one account to another.

|EC2|
    From AWS Explorer, you can view available Amazon Machine Images (AMIs), create |EC2| instances
    from those AMIs, and then connect to those instances by using Windows Remote Desktop. AWS
    Explorer also enables supporting functionality, such as the capability to create and manage key
    pairs and security groups.

|DDBlong|
    |DDBlong| is a fast, highly scalable, highly available, cost-effective, nonrelational database
    service. The |TVS| provides functionality for working with |DDBlong| in a development
    context. With the Toolkit, you can create and edit attributes in |DDBlong| tables and run Scan
    operations on tables.

|CFN|
    |CFN| makes it easy for you to deploy your .NET Framework application to AWS. |CFN| provisions
    the AWS resources required by your application, which frees you to focus on developing the
    application's functionality. The |TVS| includes two ready-to-use |CFN| templates.

|IAMlong| (|IAM|)
    From AWS Explorer, you can create IAM users and policies, and attach policies to users.

AWS SDK for .NET 
    The |TVS| installs the latest version of the AWS SDK for .NET. From Visual Studio, you can
    easily modify, build, and run any of the samples included in the SDK.

.. note:: |TVS| for Visual Studio 2008 is still available, but not supported. For more information, see
   :ref:`install`.


.. _tkv-whats-new:

What's New in Version 1.3
=========================

Added support for deployment to |EB|
    In addition to its existing deployment support for |CFN|, the |TVS| now supports deployment of
    web applications and websites to |EB|. To deploy to either service, in Solution Explorer,
    right-click your project and choose :guilabel:`Publish to AWS`. You can then use the deployment
    wizard to choose the required service. If you have |RDS| instances, the deployment wizard for
    |EB| can also be used to allow connectivity between your deployed application and selected
    |RDS| instances.

Fast redeployment
    For previously deployed projects, a new :guilabel:`Republish to` command is available in the
    context menu for a project in Solution Explorer. The command name changes to show where the
    project was last deployed (AWS Elastic Beanstalk environment or |CFN| stack) together with the
    environment or stack name. Choosing the command will display a dialog box that summarizes the
    deployment options that were last used. Choosing the :guilabel:`Deploy` button will start
    project redeployment, without the use the deployment wizard.

Support for |RDS| and Microsoft SQL Server
    |RDS| support has been added to the AWS Explorer to allow you to manage |RDS| assets in Visual
    Studio. |RDS| instances that use Microsoft SQL Server can also be added to Visual Studio's
    Server Explorer.

AWS standalone deployment tool additions
    The standalone AWS deployment tool has been updated to support deployments to |EB| and |CFN|.
    For |CFN| stacks, the tool now also supports :code:`update stack` functionality.


.. _tkv-whats-new-v1-1:

What's New in Version 1.1
=========================

AWS standalone deployment tool
    The |TVS| includes a command-line tool you can use to deploy your application to |CFN| from
    outside of the Microsoft Visual Studio development environment. With the deployment tool, you
    can make deployment an automatic part of your build process or include deployment in other
    scripting scenarios.

Redeployment to CloudFormation
    Both the deployment wizard and the deployment tool can redeploy a new instance of your
    application over an already running instance.

|GOVCLOUD-US| support
    You can designate AWS accounts as |GOVCLOUD-US| users. These users are then able to use
    the |GOVCLOUD-US| region.

Server-side encryption
    You can specify whether an |S3| object should use server-side encryption. You can specify this
    feature at the time you upload the object or afterward in the object's properties dialog box.

Customize columns in AMI, instance, and volume views
    In AWS Explorer, you can customize which columns are displayed when you are viewing Amazon
    Machine Images (AMIs), |EC2| instances, and EBS volumes.

Tagging of AMIs, instances, and volumes
    From AWS Explorer, you can add tags and tag values to AMIs, |EC2| instances, and EBS volumes.
    The tags you add are then added as columns in AWS Explorer views. As with other columns, you can
    hide these columns if you choose.

Pagination of result set returned by SDB
    When you execute a query in |SDB|, the |TVS| displays only a single "page" of results |mdash|
    either the first 100 results or the number of results specified by the :paramname:`LIMIT`
    parameter, if it is included in the query. The |TVS| now enables you to fetch either an
    additional page of results or an additional ten pages of results.

Time-delayed message delivery in SQS
    When you send an |SQS| message from the |TVS|, you can now specify a time delay before the
    message appears in the |SQS| queue.

Export SDB results to CSV
    You can export the results of your |SDB| queries to a CSV file.


.. _welcome.about_aws:

About Amazon Web Services
=========================

Amazon Web Services (AWS) is a collection of digital infrastructure services that developers can
leverage when developing their applications. The services include computing, storage, database, and
application synchronization (messaging and queuing). AWS uses a pay-as-you-go service model. You are
charged only for the services that you |mdash| or your applications |mdash| use. Also, to make AWS
more approachable as a platform for prototyping and experimentation, AWS offers a free usage tier.
On this tier, services are free below a certain level of usage. For more information, go to 
|GSG-free|_.



