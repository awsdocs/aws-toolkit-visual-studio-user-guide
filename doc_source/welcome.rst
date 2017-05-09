.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _welcome:

###################
Using the |TVSlong|
###################

.. meta::
   :description: Using the AWS Toolkit for Visual Studio
   :keywords: features, services, what's new

.. _welcome.about_tkv:

|TVS|
=====

The |TVS| is a plugin for the Visual Studio IDE that makes it easier for you to develop,
debug, and deploy .NET applications that use Amazon Web Services. The |TVS| is supported for
Visual Studio versions 2013 and later. For details about how to download and install the kit,
see :ref:`install`.

The |TVS| contains the following features to enhance your development experience.

|Explorer|
----------
    The |Explorer| tool window, available from the IDE's :guilabel:`View` menu, enables you to interact
    with many of the AWS services from inside the Visual Studio IDE. Supported data services
    include |S3long| (|S3|), |SDB|, |SNSlong| (|SNS|), |SQSlong| (|SQS|), and |CFlong|.
    |Explorer| also provides access to |EC2long| (|EC2|) management, |IAMlong| (|IAM|) user and
    policy management, deployment of serverless applications and functions to |LAMlong| and
    deployment of web applications to |EBlong| and |CFNlong|.

Credential and Region Management
--------------------------------
    |Explorer| supports multiple AWS accounts (including IAM user accounts) and regions, and
    enables you to easily change the displayed view from one account to another or view and manage
    resources and services in different regions.

|EC2|
-----
    From |Explorer|, you can view available Amazon Machine Images (AMIs), create |EC2| instances
    from those AMIs, and then connect to those instances by using Windows Remote Desktop. |Explorer| also enables supporting functionality, such as the capability to create and manage key
    pairs and security groups.

|LAMlong|
---------
   You can use |LAM| to host your serverless .NET Core C# functions and serverless applications.
   Use blueprints to quickly create new serverless projects and get a head start
   in developing your serverless application.

|ACClong|
---------
    |ACC| is integrated with Visual Studio Team Explorer. This makes it easy to clone and create
    repositories held in |ACC|, and to work with source code changes from within the IDE.

|DDBlong|
---------
    |DDB| is a fast, highly scalable, highly available, cost-effective, nonrelational database
    service. The |TVS| provides functionality for working with |DDBlong| in a development
    context. With the |TVS|, you can create and edit attributes in |DDB| tables and run scan
    operations on tables.

|S3|
----
    You can quickly and easily upload content to |S3| buckets by dragging and dropping, or download content
    from |S3|. You can also set permissions, metadata, and tags conveniently on objects
    in buckets.

|RDS|
-----
    |Explorer| can help you create and manage |RDS| assets in Visual Studio. |RDS| instances that use
    Microsoft SQL Server can also be added to Visual Studio's :guilabel:`Server Explorer`.

|EBlong|
--------
   You can use |EB| to deploy your .NET web application projects to AWS. You can deploy your
   application
   to a single instance environment or to a fully load balanced, automatically scaled environment from
   within the
   IDE.
   You can also deploy new versions of your application quickly and conveniently without leaving Visual
   Studio. If your application uses SQL Server in |RDS|, the deployment wizard can also
   set up the connectivity between your application environment in |EB| and the database instance in |RDS|.
   The |TVS| also includes the standalone command-line deployment tool. Use the deployment tool to make
   deployment an automatic part of your build process, or to include deployment in other scripting scenarios
   outside of Visual Studio.

|CFN|
-----
    You can use the |TVS| to edit |CFN| JSON-format templates with support for editor IntelliSense
    and
    syntax highlighting. With a |CFN| template you describe the resources you want to instantiate
    to
    host your application. From within the IDE you then deploy the template to |CFN|. The resources
    described in the template are provisioned for you, freeing you to focus on developing the application's
    functionality.

|IAMlong| (|IAM|)
-----------------
    From |Explorer|, you can create |IAM| users, roles, and policies, and attach policies to users.

|sdk-net|
---------
    The |TVS| installs the latest version of the |sdk-net|. From Visual Studio,
    easily modify, build, and run any of the samples included in the SDK.

.. note:: The |TVS| is also available for Visual Studio 2008, 2010, and 2012 versions. However, it is
   not supported.
   For more information, see :ref:`install`.

.. include:: about-aws.txt



