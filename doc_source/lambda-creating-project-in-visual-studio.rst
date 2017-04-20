.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _using-lambda-template-visual-studio:



######################################################
Tutorial: Using the |LAMlong| Project in the |TVSlong|
######################################################

.. meta::
   :description: Working on AWS Lambda projects in Visual Studio

Using the |LAMlong| .NET Core project templates for Visual Studio you can easily create a AWS Lambda 
Function using Microsoft .NET Core.

For prerequisites and information about setting up the |TVSlong|, see :doc:`lambda-index`.

Create a Visual Studio .NET Core |LAM| Project
==============================================

#. Open Visual Studio, and on the :guilabel:`File` menu, choose :guilabel:`New`, :guilabel:`Project`.
#. In the :guilabel:`Installed` pane, choose  Visual C# and the :guilabel:`AWS Lambda  Project (.NET Core)``
   template.

   There are two types of project to choose from:

   * |LAMlong| projects for creating a project to develop and deploy an individual |LAM| function.
   * AWS Serverless Applications projects for creating |LAM| functions with a serverless |CFNlong| template.
     AWS serverless applications enable you to define more than just the function. For example, you 
     can simultaneously create a database, add |IAM| roles, etc., with serverless deployment. AWS 
     serverless applications also enable you to deploy multiple functions at one time.

   .. image:: images/projectlist2.png
      :alt: Project types for AWS Lambda projects

#. After you select the project type, choose a blueprint. For
   :guilabel:`AWS Lambda Project (.NET Core)`, the :guilabel:`Select Blueprint` page
   shows several |LAM| function templates.

   .. image:: images/blueprints.png
      :alt: Blueprints for an AWS Lambda project

#. Choose the type of |LAM| function you want to develop, and then choose :guilabel:`Finish`
   to create the Visual Studio project. You can now review the project's structure and code.
   
Review the Project Files
========================

Examine the :code:`aws-lambda-tools-defaults.json` file, which is created as part of your project. You can set 
the options in this file, which is read by the Lambda tooling by default. The project templates created 
in Visual Studio set many of these fields with default values. This is where the function handler is 
specified which is why you don't have to set it in the wizard. But if you rename the Function, Class 
or Assembly then you will need to update the field in the :code:`aws-lambda-tools-defaults.json` file. 

.. code-block:: js

{                                                                                   
  "profile":"default",                                                            
  "region" : "us-east-2",                                                           
  "configuration" : "Release",                                                      
  "framework" : "netcoreapp1.0",                                                    
  "function-runtime":"dotnetcore1.0",                                               
  "function-memory-size" : 256,                                                     
  "function-timeout" : 30,                                                          
  "function-handler" : "BlogExample::BlogExample.Function::FunctionHandler"         
}

When you use this aws-lambda-tools-default.json file, the only things left that the Lambda tooling needs to deploy the function are the name of the Lambda function and the IAM role.

Your project is now ready to publish to |LAM|.

Publish to |LAM|
================

To publish your function to |LAM|:

#. In :guilabel:`Solution Explorer`, right-click
   the project, and then choose :guilabel:`Publish to AWS Lambda`.

   .. image:: images/publish.png
      :alt: Publishing a Visual Studio project to AWS Lambda

#.  On the :guilabel:`Upload Lambda Function` page, in :guilabel:`Function Name`, type a name for
    the function or select a previously published function to republish. Then choose :guilabel:`Next`.

    .. image:: images/upload.png
         :alt: Upload screen for Lambda function

#.  In the :guilabel:`Advanced Function Details` page, set the fields as follows:

    * **Required:** Provide a :guilabel:`Role Name` for a role associated with
      your account. Choose an existing role or a new role based on an AWS managed policy
      or your own managed policy. The role is used to provide credentials for any AWS service
      calls made by the code in the function. Your account must have permission to run the IAM
      ListPolicies action, or the :guilabel:`Role Name` list will be empty and you will be unable to
      continue.
    * *Optional:* If your Lambda function accesses resources on an |VPC|, select the subnets and
      security groups.
    * *Optional:* Set any environment variables that your |LAM| function needs. The keys are
      automatically encrypted by the default service key (which is free) or you can specify an |KMS| key
      (for which there
      is a charge).
      `KMS <https://aws.amazon.com/kms/>`_ is a managed service you can use to create and control the
      encryption keys used to encrypt your data. If you have an |KMS| key, you can select it from the list.

#. Choose :guilabel:`Upload`.

    .. image:: images/advancedfunction.png
         :alt: Set Lambda function details in the Advanced Function Details page

#. The :guilabel:`Uploading Function` page is shown while the function is uploading, and
   automatically closes when the upload completes. To keep the wizard open so you can view the report,
   clear
   :guilabel:`Automatically close wizard on successful completion` at the bottom of the form before
   the upload completes. Close the page when you finish viewing the report.

   .. image:: images/uploading.png
       :alt: Uploading Function page

#. After the function is uploaded, the :guilabel:`Function` page opens. Use the tabs on
   the left side of the page to test the function, add event sources, and view the log. Use
   the :guilabel:`Configuration` tab to add VPC subnets and security groups, memory, timeout,
   and environment variables.

   .. image:: images/functionpage.png
       :alt: Function page showing an example request for testing a function

#. To add event sources to establish a connection between an AWS resource (such as an
   |S3| bucket, |SNS| topic, or |AKSlong| streams) and a |LAM| function, choose :guilabel:`Event Sources`.
   This will display the :guilabel:`Add Event Source` page.

   On the :guilabel:`Add Event Source` page, from :guilabel:`Source Type`, choose the appropriate
   event source and choose :guilabel:`OK` to add the event source.

   .. image:: images/eventsources.png
       :alt: Add Event Source page

#. To test the function, in :guilabel:`Example Requests`, choose an example request.

   .. image:: images/testfunction.png
       :alt: Function page showing an example request for testing a function

#. To run the test, choose :guilabel:`Invoke`.

   .. image:: images/invoke.png
       :alt: Invoking the test function page

#. View the output from the test in :guilabel:`Log output`.

   .. image:: images/logoutput.png
       :alt: Function test output log

After your |LAM| function is published, it's ready to use. For use cases,
see `Examples of How to Use AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/use-cases.html>`_.

|LAM| automatically monitors |LAM| functions for you, reporting metrics through
|CWlong|. To monitor and troubleshoot your function, see `Troubleshooting and Monitoring
AWS Lambda Functions with Amazon CloudWatch <http://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html>`_.



