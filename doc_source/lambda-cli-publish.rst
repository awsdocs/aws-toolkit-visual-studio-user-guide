.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _working-with-dotnet-cli:



#####################################################
Deploying an |LAMlong| Project with the .NET Core CLI
#####################################################

.. meta::
   :description: Using the .NET Core CLI to deploy an AWS Lambda function

The |TVSlong| includes |LAMlong| .NET Core project templates for Visual Studio. You must have Visual
Studio 2015 Update 3 installed before you can install `.NET Core for Windows <https://www.microsoft.com/net/core#windowsvs2015>`_
and the |TVS|. You can deploy |LAM| functions built in Visual Studio using the .NET Core command line interface (CLI).


.. note:: For information about creating |LAM| functions in Visual Studio, see :doc:`lambda`.

          For more information about Microsoft .NET Core, see `.NET Core <https://docs.microsoft.com/en-us/dotnet/articles/core/>`_.

          For more information about |LAM| functions, see
          `What Is AWS Lambda? <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_

.. toctree::
    :titlesonly:
    :maxdepth: 1

Listing the |LAM| Commands Available through the CLI
====================================================

There are a variety of |LAM| commands available through the .NET Core CLI.

#. Open a command prompt and navigate to the folder containing a Visual Studio .NET Core |LAM| project.

#. Type :code:`dotnet lambda --help`.

 .. code:: sh

    C:\Lambda\AWSLambda1\AWSLambda1>dotnet lambda --help
        AWS Lambda Tools for .NET Core functions
        Project Home: https://github.com/aws/aws-lambda-dotnet
        .
        Commands to deploy and manage |LAM| functions:
        .
                deploy-function         Deploy the project to |LAM|
                invoke-function         Invoke the function in |LAM| with an optional input
                list-functions          List all of your |LAM| functions
                delete-function         Delete a |LAM| function
                get-function-config     Get the current runtime configuration for a |LAM| function
                update-function-config  Update the runtime configuration for a |LAM| function
        .
        Commands to deploy and manage AWS Serverless applications using |CFNlong|:
        .
                deploy-serverless       Deploy an AWS Serverless application
                list-serverless         List all of your AWS Serverless applications
                delete-serverless       Delete an AWS Serverless application
        .
        Other Commands:
        .
                package                 Package a |LAM| project into a .zip file ready for deployment
        .
        To get help on individual commands execute:

                dotnet lambda help <command>


Publishing a .NET Core |LAM| Project from the .NET Core CLI
===========================================================

The following instructions assume you've created an |LAMlong| .NET Core function in Visual
Studio.

#. Open a command prompt and navigate to the folder containing your Visual Studio .NET Core |LAM| project.

#. Type :code:`dotnet lambda deploy-function`.

#. When prompted, type the name of the function to deploy. It can be a new name or the name of an existing
function.

#. When prompted, enter the AWS Region (the region to which your |LAM| function will be deployed).

#. When prompted, select or create the |IAM| role that |LAM| will assume when executing the function.

#. On successful completion, the message **New Lambda function created** is displayed.

 .. code-block:: sh

        C:\Lambda\AWSLambda1\AWSLambda1>dotnet lambda deploy-function
        Executing publish command
        ... invoking 'dotnet publish', working folder 'C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish'
        ... publish: Publishing AWSLambda1 for .NETCoreApp,Version=v1.0
        ... publish: Project AWSLambda1 (.NETCoreApp,Version=v1.0) will be compiled because expected outputs are missing
        ... publish: Compiling AWSLambda1 for .NETCoreApp,Version=v1.0
        ... publish: Compilation succeeded.
        ... publish:     0 Warning(s)
        ... publish:     0 Error(s)
        ... publish: Time elapsed 00:00:01.2479713
        ... publish:
        ... publish: publish: Published to C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish
        ... publish: Published 1/1 projects successfully
        Zipping publish folder C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish to C:\Lambda\AWSLambda1\AWSLamb
        da1\bin\Release\netcoreapp1.0\AWSLambda1.zip
        Enter Function Name: (AWS Lambda function name)
        DotNetCoreLambdaTest
        Enter AWS Region: (The region to connect to AWS services)
        us-west-2
        Creating new Lambda function
        Select IAM Role that Lambda will assume when executing function:
            1) lambda_exec_LambdaCoreFunction
            2) *** Create new IAM Role ***
        1
        New Lambda function created

If you deploy an existing function, the deploy function asks only for the AWS Region.

 .. code-block:: sh

        C:\Lambda\AWSLambda1\AWSLambda1>dotnet lambda deploy-function
        Executing publish command
        Deleted previous publish folder
        ... invoking 'dotnet publish', working folder 'C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish'
        ... publish: Publishing AWSLambda1 for .NETCoreApp,Version=v1.0
        ... publish: Project AWSLambda1 (.NETCoreApp,Version=v1.0) was previously compiled. Skipping compilation.
        ... publish: publish: Published to C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish
        ... publish: Published 1/1 projects successfully
        Zipping publish folder C:\Lambda\AWSLambda1\AWSLambda1\bin\Release\netcoreapp1.0\publish to C:\Lambda\AWSLambda1\AWSLamb
        da1\bin\Release\netcoreapp1.0\AWSLambda1.zip
        Enter Function Name: (AWS Lambda function name)
        DotNetCoreLambdaTest
        Enter AWS Region: (The region to connect to AWS services)
        us-west-2
        Updating code for existing function


After your |LAM| function is deployed, it is ready to use. See
`Examples of How to Use AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/use-cases.html>`_.

|LAM| automatically monitors |LAM| functions for you, reporting metrics through
|CWlong|. To monitor and troubleshoot your |LAM| function, see `Troubleshooting and Monitoring
AWS Lambda Functions with Amazon CloudWatch <http://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html>`_.



