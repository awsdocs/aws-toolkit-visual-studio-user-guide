.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _working-with-lambda:



##################################
Using |LAMlong| with the |TVSlong|
##################################

.. meta::
   :description: Using the Toolkit for Visual Studio to work with AWS Lambda

The |TVSlong| includes |LAMlong| .NET Core project templates for Visual Studio. You can use the
templates to quickly develop and deploy .NET Core-based C# |LAM| functions. .NET Core is cross-platform,
supporting Windows, macOS, and Linux, and can be used to develop device, cloud,
and embedded applications. You must have Visual Studio 2015 Update 3 installed to install `.NET Core for Windows <https://www.microsoft.com/net/core#windowsvs2015>`_
and the |TVS|_.

.. note:: For more information about Microsoft .NET Core, see `.NET Core <https://docs.microsoft.com/en-us/dotnet/articles/core/>`_.

          For .NET Core prerequisites and installation instructions for the three platforms, see `.NET Core Downloads <https://www.microsoft.com/net/download/core>`_.

          For more information about |LAMlong| functions, see
          `What Is AWS Lambda? <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_

.. toctree::
    :titlesonly:
    :maxdepth: 1

Creating a Visual Studio .NET Core |LAM| Project
=================================================

Open Visual Studio and create a new project.

#. In Visual Studio, on the :guilabel:`File` menu, choose :guilabel:`New`, :guilabel:`Project`.
#. In the :guilabel:`Installed` pane, choose  Visual C# and the |LAMlong| Project template.

   There are two categories of projects, |LAMlong| projects for creating a project to develop and
   deploy an individual |LAM| function, and AWS Serverless Applications for creating |LAM|
   functions with a serverless |CFNlong| template. AWS Serverless Applications
   enable you to define more than just the function. For example, you can simultaneously
   create a database, add |IAM| roles, etc., with serverless deployment. AWS Serverless Applications
   also enable you to deploy multiple functions at one time.

   .. image:: images/projectlist.png
      :alt: Project types for AWS Lambda projects

#. After you select the project type, choose a blueprint. For the
   :guilabel:`AWS Lambda Project (.NET Core)`, you should see the :guilabel:`Select Blueprint` page
   showing several |LAM| function templates.

   .. image:: images/blueprints.png
      :alt: Blueprints for an AWS Lambda project

#. Choose the type of |LAM| function you want to develop, and then choose :guilabel:`Finish`
   to create the Visual Studio project.

#. Review the project's structure and code. Your project is now ready to publish to |LAM|.

Publishing to |LAM|
--------------------

When your function is complete, you can publish it to |LAM|.

#. In :guilabel:`Solution Explorer`, right-click
   the project and choose :guilabel:`Publish to AWS Lambda`.

   .. image:: images/publish.png
      :alt: Publishing a Visual Studio project to AWS Lambda

#.  On the :guilabel:`Upload Lambda Function` page, in :guilabel:`Function Name`, type a name for
    the function or select a previously published function to republish.

    Choose :guilabel:`Next`.

    .. image:: images/upload.png
         :alt: Upload screen for Lambda function


#.  Set the fields you want in the :guilabel:`Advanced Function Details` page, as follows:

    * **Required:** You must provide a :guilabel:`Role Name`. Select a role associated with
      your account. You can choose either an existing role or a new role based on an AWS managed policy
      or your own managed policy. The role will be used to provide credentials for any AWS service
      calls the code in the function makes. Your account must have permission to run the IAM
      ListPolicies action, or the :guilabel:`Role Name` list will be empty and you will be unable to
      continue.
    * *Optional:* If your Lambda function accesses resources on an |VPC|, select the subnets and
      security groups.
    * *Optional:* Set any environment variables that your |LAM| function requires. The keys are
      automatically encrypted by the default service key (free) or you can specify an |KMS| key (a charge).
      `KMS <https://aws.amazon.com/kms/>`_ is a managed service you can use to create and control the
      encryption keys used to encrypt your data. If you have an |KMS| key, you can select it from the list.

    After you set the environment variables in the list that your function needs, choose :guilabel:`Upload`.

    .. image:: images/advancedfunction.png
         :alt: Set Lambda function details in the Advanced Function form

#. While the function is uploading, the :guilabel:`Uploading Function` page is shown. The page will
   automatically close upon completion.  To keep the wizard open so you can view the report, clear
   :guilabel:`Automatically close wizard on successful completion` at the bottom of the form before
   the upload completes. Close the page when you are finished viewing the report.

   .. image:: images/uploading.png
       :alt: Uploading Function page

#. After the function is uploaded, the :guilabel:`Function view` page opens. Tabs on
   the left side of the page enable you to test the function, add event sources, and view the log. The
   configuration tab enables you to add VPC subnets and security groups, memory, timeout, and environment variables.

   .. image:: images/functionPage.png
       :alt: Function page showing an example request for testing a function

#. To add event sources that can be used to establish a connection between an AWS Resource (such an
   |S3| bucket, |SNS| topic, or |AKSlong| streams) and a |LAM| function, choose :guilabel:`Event Sources`.
   On the :guilabel:`Add Event Sources` page, choose :guilabel:`Add` to add the event sources.

   On the :guilabel:`Add Event Sources` page, from :guilabel:`Source Type`, choose the appropriate
   event source.

   .. image:: images/eventSources.png
       :alt: Add event source page

#. To test the function, in :guilabel:`Example Requests`, choose an example request.

   .. image:: images/testfunction.png
       :alt: Function page showing an example request for testing a function

#. To run the test, choose :guilabel:`Invoke`.

   .. image:: images/invoke.png
       :alt: Invoking the test function page

#. View the output from the test in :guilabel:`Log output`.

   .. image:: images/logoutput.png
       :alt: Function test output log


After your |LAM| function is published, it is ready to use. For example use cases,
see
`Examples of How to Use AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/use-cases.html>`_.

|LAM| automatically monitors |LAM| functions for you, reporting metrics through
|CWlong|. To monitor and troubleshoot your |LAM| function, see `Troubleshooting and Monitoring
AWS Lambda Functions with Amazon CloudWatch <http://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html>`_.



