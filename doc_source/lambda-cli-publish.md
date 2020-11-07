# Deploying an AWS Lambda Project with the \.NET Core CLI<a name="lambda-cli-publish"></a>

The AWS Toolkit for Visual Studio includes AWS Lambda \.NET Core project templates for Visual Studio\. You can deploy Lambda functions built in Visual Studio using the \.NET Core command line interface \(CLI\)\.

**Topics**
+ [Prerequisites](#lambda-cli-prereqs)
+ [Related topics](#lambda-cli-related)
+ [Listing the Lambda Commands Available through the \.NET Core CLI](#listing-the-lam-commands-available-through-the-cli)
+ [Publishing a \.NET Core Lambda Project from the \.NET Core CLI](#publishing-a-net-core-lam-project-from-the-net-core-cli)

## Prerequisites<a name="lambda-cli-prereqs"></a>

Before you start using the \.NET Core CLI to deploy Lambda functions, you must meet the following prerequisites:
+ Be sure Visual Studio 2015 Update 3 is installed\.
+ Install [\.NET Core for Windows](https://dotnet.microsoft.com/download#windowsvs2015)\.
+ Set up the \.NET Core CLI to work with Lambda\. For more information, see [\.NET Core CLI](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-cli.html) in the *AWS Lambda Developer Guide*\.
+ Install the Toolkit for Visual Studio\. For more information, see [Install the Toolkit for Visual Studio](setup.md#install)\.

## Related topics<a name="lambda-cli-related"></a>

The following related topics can be helpful as you use the \.NET Core CLI to deploy Lambda functions:
+ For more information about Lambda functions, see [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) in the *AWS Lambda Developer Guide*\.
+ For information about creating Lambda functions in Visual Studio, see [ Using the AWS Lambda Templates in the AWS Toolkit for Visual Studio](lambda-index.md)\.
+ For more information about Microsoft \.NET Core, see [\.NET Core](https://docs.microsoft.com/en-us/dotnet/articles/core/) in Microsoft's online documentation\.

## Listing the Lambda Commands Available through the \.NET Core CLI<a name="listing-the-lam-commands-available-through-the-cli"></a>

To list the Lambda commands that are available through the \.NET Core CLI, do the following\.

1. Open a command prompt window, and navigate to the folder containing a Visual Studio \.NET Core Lambda project\.

1. Enter `dotnet lambda --help`\.

```
C:\Lambda\AWSLambda1\AWSLambda1>dotnet lambda --help
    AWS Lambda Tools for .NET Core functions
    Project Home: https://github.com/aws/aws-lambda-dotnet
    .
    Commands to deploy and manage Lambda functions:
    .
            deploy-function         Deploy the project to Lambda
            invoke-function         Invoke the function in Lambda with an optional input
            list-functions          List all of your Lambda functions
            delete-function         Delete a Lambda function
            get-function-config     Get the current runtime configuration for a Lambda function
            update-function-config  Update the runtime configuration for a Lambda function
    .
    Commands to deploy and manage AWS serverless applications using AWS CloudFormation:
    .
            deploy-serverless       Deploy an AWS serverless application
            list-serverless         List all of your AWS serverless applications
            delete-serverless       Delete an AWS serverless application
    .
    Other Commands:
    .
            package                 Package a Lambda project into a .zip file ready for deployment
    .
    To get help on individual commands, run the following:

            dotnet lambda help <command>
```

## Publishing a \.NET Core Lambda Project from the \.NET Core CLI<a name="publishing-a-net-core-lam-project-from-the-net-core-cli"></a>

The following instructions assume you've created an AWS Lambda \.NET Core function in Visual Studio\.

1. Open a command prompt window, and navigate to the folder containing your Visual Studio \.NET Core Lambda project\.

1. Enter `dotnet lambda deploy-function`\.

1. When prompted, enter the name of the function to deploy\. It can be a new name or the name of an existing function\.

1. When prompted, enter the AWS Region \(the Region to which your Lambda function will be deployed\)\.

1. When prompted, select or create the IAM role that Lambda will assume when executing the function\.

On successful completion, the message **New Lambda function created** is displayed\.

```
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
```

If you deploy an existing function, the deploy function asks only for the AWS Region\.

```
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
```

After your Lambda function is deployed, it's ready to use\. For more information, see [Examples of How to Use AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/use-cases.html)\.

Lambda automatically monitors Lambda functions for you, reporting metrics through Amazon CloudWatch\. To monitor and troubleshoot your Lambda function, see [Troubleshooting and Monitoring AWS Lambda Functions with Amazon CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html)\.