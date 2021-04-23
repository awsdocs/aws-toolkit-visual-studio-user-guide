# Basic AWS Lambda Project<a name="lambda-creating-project-in-visual-studio"></a>

Using the AWS Lambda \.NET Core project templates for Visual Studio, you can create a Lambda function using Microsoft \.NET Core\.

For prerequisites and information about setting up the AWS Toolkit for Visual Studio, see [Using the AWS Lambda Templates in the AWS Toolkit for Visual Studio](lambda-index.md)\.

## Create a Visual Studio \.NET Core Lambda Project<a name="create-a-visual-studio-net-core-lam-project"></a>

Built\-in Lambda Visual Studio blueprints enable quick project initialization\. A blueprint is a canned set of files and functions to quickly demonstrate functionality, and provides a good starting\-point for later modifications\. 

**To create a Lambda project**

1. Open Visual Studio, and on the **File** menu, choose **New**, **Project**\.

1. Do one of the following:
   + For Visual Studio 2017, in the **New Project** dialog box, expand **Installed**, expand **Visual C\#**,select **AWS Lambda**, choose the **AWS Lambda Project \(\.NET Core \- C\#\)** template, and then choose **OK**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/CreateNewProject-05-Core-Lambda-VS2017.png)
   + For Visual Studio 2019, in the **New Project** dialog box, ensure that the **Language**, **Platform**, and **Project type** drop\-down boxes are set to "All" and type *aws lambda* in the **Search** field\. Then choose the **AWS Lambda Project \(\.NET Core \- C\#\)** template and choose **Next**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/CreateNewProject-05-Core-Lambda-VS2019.png)

1. Do one of the following:
   + For Visual Studio 2017, for **Name**, enter **AWSLambda1**, enter the desired file **Location**, and then choose **OK**\.
   + For Visual Studio 2019, for **Name**, enter **AWSLambda1**, enter the desired file **Location**, and then choose **Create**\.

1. On the **Select Blueprint** page, choose the **Empty Function** blueprint, and then choose **Finish** to create the Visual Studio project\. You can now review the project's structure and code\.

## Review the Project Files<a name="review-the-project-files"></a>

There are two project files to review: `aws-lambda-tools-defaults.json` and `Function.cs`\.

The folowing example shows the `aws-lambda-tools-defaults.json` file, which is created as part of your project\. You can set build options by using the fields in this file, which the Lambda tooling reads by default\. The project templates in Visual Studio contain many of these fields with default values\. The field **function\-handler** specifies the method that runs when the Lambda function runs\. If you specify the **function\-handler** field, it is pre\-populated in the Publish wizard\. If you rename the function, class or assembly then you also need to update the field in the `aws-lambda-tools-defaults.json` file\.



```
{
  "Information": [
    "This file provides default values for the deployment wizard inside Visual Studio and the AWS Lambda commands added to the .NET Core CLI.",
    "To learn more about the Lambda commands with the .NET Core CLI execute the following command at the command line in the project root directory.",
    "dotnet lambda help",
    "All the command line options for the Lambda command can be specified in this file."
  ],
  "profile": "default",
  "region": "us-east-2",
  "configuration": "Release",
  "framework": "netcoreapp3.1",
  "function-runtime": "dotnetcore3.1",
  "function-memory-size": 256,
  "function-timeout": 30,
  "function-handler": "AWSLambda1::AWSLambda1.Function::FunctionHandler"
}
```

Examine the `Function.cs` file\. `Function.cs` defines the c\# functions to expose as Lambda functions\. This `FunctionHandler` is the Lambda functionality that runs when the Lambda function runs\. In this project, there is one function defined: `FunctionHandler`, which calls `ToUpper()` on the input text\. 

Your project is now ready to publish to Lambda\.

## Publish to Lambda<a name="publish-to-lam"></a>

How and when your Lambda functionality is invoked is not a part of the Lambda deployment itself; the Lambda is just the "what" of your on\-demand functionality\. 

**To publish your function to Lambda**

1. If the AWS Explorer window is not open, choose **View** and then choose **AWS Explorer**\.

1. In **Solution Explorer**, right\-click the project, and then choose **Publish to AWS Lambda**\.

1. On the **Upload Lambda Function** page, do the following:  
![\[Upload screen for Lambda function\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/UploadBasic.png)

   1.  For **Package Type**, choose **Zip**\. A ZIP file will be created as a result of the build process and will be uploaded to Lambda\. The other **Package Type** option is **Image** and [Tutorial: Basic Lambda Project Creating Docker Image](lambda-creating-project-docker-image.md) guides you through that alternative\.

   1.  For **Function Name**, enter a display name for your Lambda instance\. This name is the reference name that both the AWS Explorer within Visual Studio as well as the AWS Management Console display\.

   1.  \(Optional\) For **Description**, enter text to display with your instance in the AWS Management Console\.

   1. Choose **Next**\.

1. In the **Advanced Function Details** page, do the following:

   1.  For **Role Name**, choose a role associated with your account\. The role provides temporary credentials for any AWS service calls made by the code in the function\. If you do not have a role, choose **New Role based on AWS Managed Policy** and then choose **AWSLambdaBasicExecutionRole** which is a role with minimal access permissions\. 
**Note**  
Your account must have permission to run the IAM ListPolicies action, or the **Role Name** list will be empty and you will be unable to continue\.

   1.  \(Optional\) If your Lambda function accesses resources on an Amazon VPC, select the subnets and security groups\.

   1. \(Optional\) Set any environment variables that your Lambda function needs\. The keys are automatically encrypted by the default service key which is free, or you can specify an AWS KMS key, for which there is a charge\. [KMS](https://aws.amazon.com/kms/) is a managed service you can use to create and control the encryption keys used to encrypt your data\. If you have an AWS KMS key, you can select it from the list\.

1. Choose **Upload**\.

   The **Uploading Function** page displays while the function is uploading to AWS\. To keep the wizard open after uploading so that you can view the report, clear **Automatically close wizard on successful completion** at the bottom of the form before the upload completes\. 

   After the function uploads, your Lambda function is live\. The **Function:** view page opens and displays your new Lambda function’s configuration\.

1. To manually invoke the Lambda function, on the **Test Function** tab enter `hello lambda!` in the free\-text input field and then choose **Invoke**\. Your text, converted to uppercase, will appear in **Response**\.   
![\[Invoking the test function page\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/invokeBasic.PNG)

   You can reopen the **Function:** view at any time by double\-clicking on your deployed instance located in the **AWS Explorer** under the **AWS Lambda** node\.

1. \(Optional\) To confirm once more that you successfully published your Lambda function, log into the AWS Management Console and then choose Lambda\. The console displays all of your published Lambda functions, including the one you just created\.  
![\[Viewing Lamda Functions on AWS Management Console\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/AwsManagementConsoleLambdaBasic.PNG)

## Clean\-up<a name="cleanup-lam"></a>

If you are not going to continue developing with this example, delete the function you deployed so that you do not get billed for unused resources in your account\.

**To delete your function**
+  In the **AWS Explorer**, under the **AWS Lambda** node, open the context \(right\-click\) menu for your deployed instance, and then choose **Delete**\.

## Next Steps<a name="next-steps-lam"></a>

This example demonstrated how to create a project with a \.NET 3\.1 managed runtime\. For information about how to create a project with a \.NET 5\.0 custom runtime for your Lambda function, see [Exploring \.NET 5 with the AWS Toolkit for Visual Studio](https://aws.amazon.com/blogs/developer/exploring-net-5-with-the-aws-toolkit-for-visual-studio/)\.

For additional use cases, see [Examples of How to Use AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/use-cases.html)\.

Lambda automatically monitors Lambda functions for you, reporting metrics through Amazon CloudWatch\. To monitor and troubleshoot your function, see [Troubleshooting and Monitoring AWS Lambda Functions with Amazon CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html)\.

