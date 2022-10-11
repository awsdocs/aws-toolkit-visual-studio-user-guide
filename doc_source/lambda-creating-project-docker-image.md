# Basic AWS Lambda Project Creating Docker Image<a name="lambda-creating-project-docker-image"></a>

You can use the Toolkit for Visual Studio to deploy your Lambda function as a Docker image\. Using Docker, you have more control over your runtime, for example you can choose custom runtimes like \.NET 5\.0\. You deploy your Docker image in the same way as any other container image\. This tutorial closely mimics [Tutorial: Basic Lambda Project](lambda-creating-project-in-visual-studio.md), with two differences:
+ A Dockerfile is included in the project
+ An altered Publish configuration

For information about Lambda container images, see [Lambda Deployment Packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) in the *AWS Lambda Developer Guide*\.

For prerequisites and information about setting up the AWS Toolkit for Visual Studio, see [Using the AWS Lambda Templates in the AWS Toolkit for Visual Studio](lambda-index.md)\. 

## Create a Visual Studio \.NET Core Lambda Project<a name="create-a-visual-studio-net-core-lam-project"></a>

Built\-in Lambda Visual Studio blueprints enable quick project initialization\. A blueprint is a canned set of files and functions to quickly demonstrate functionality, and provides a good starting\-point for later modifications\. 

**To create a Visual Studio \.NET Core Lambda project**

1. Open Visual Studio, and on the **File** menu, choose **New**, **Project**\.

1. Do one of the following:
   + For Visual Studio 2017, in the **New Project** dialog box, expand **Installed**, expand **Visual C\#**, choose **AWS Lambda**, choose the **AWS Lambda Project \(\.NET Core \- C\#\)** template, and then choose **OK**\.
   + For Visual Studio 2019, in the **New Project** dialog box, ensure that the **Language**, **Platform**, and **Project type** drop\-down boxes are set to "All" and type *aws lambda* in the **Search** field\. Then choose the **AWS Lambda Project \(\.NET Core \- C\#\)** template and choose **Next**\.

1. Do one of the following:
   + For Visual Studio 2017, for **Name**, enter **AWSLambdaDocker**, enter the desired file **Location**, and then choose **OK**\.
   + For Visual Studio 2019, for **Name**, enter **AWSLambdaDocker**, enter the desired file **Location**, and then choose **Create**\.

1. On the **Select Blueprint** page, choose the **\.NET 5 \(Container Image\)** blueprint, and then choose **Finish** to create the Visual Studio project\. You can now review the project's structure and code\.

## Review the Project Files<a name="review-the-project-files"></a>

There are three project files to review: `Dockerfile`, `aws-lambda-tools-defaults.json`, and `Function.cs`\.

The following code shows the `Dockerfile` which is created by using the selected blueprint\. It performs three actions: 

**FROM:**  
 Establishes the base image to utilize for this image\. This base image provides \.NET Runtime, Lambda runtime, and a shell script that provides an entry point for the Lambda \.NET process\. 

**WORKDIR**  
Establishes the image's internal work directory as `/var/task`\. 

**COPY**  
Will copy the files generated from the build process from their local location into the work directory of the image\.

```
FROM ecr.aws/lambda/dotnet:5.0

WORKDIR /var/task

# This COPY command copies the .NET Lambda project's build artifacts from the host machine into the image. 
# The source of the COPY should match where the .NET Lambda project publishes its build artifacts. If the Lambda function is being built 
# with the AWS .NET Lambda Tooling, the `--docker-host-build-output-dir` switch controls where the .NET Lambda project
# will be built. The .NET Lambda project templates default to having `--docker-host-build-output-dir`
# set in the aws-lambda-tools-defaults.json file to "bin/Release/net5.0/linux-x64/publish".
#
# Alternatively Docker multi-stage build could be used to build the .NET Lambda project inside the image.
# For more information on this approach checkout the project's README.md file.
COPY "bin/Release/net5.0/linux-x64/publish"  .
```

To further customize your Dockerfile, you could also utilize:
+ `ENTRYPOINT`: The base image already includes an `ENTRYPOINT`, which is the startup process executed when the image is started\. If you wish to specify your own, then you are overriding that base entry point\. 
+  `CMD`: `CMD` instructs AWS which custom code you want executed\. It expects a fully\-qualified name to your custom method\. This line either needs to be included directly in the Dockerfile or can be specified during the publish process\. 

```
# Example of alternative way to specify the Lambda target method rather than during the publish process.
CMD [ "AWSLambdaDocker::AWSLambdaDocker.Function::FunctionHandler"]
```

 

Examine the `aws-lambda-tools-defaults.json` file\.
+ Field `docker-host-build-output-dir` sets the output directory of the build process that correlates with the instructions in the `Dockerfile`\.
+ Field `image-command` is a fully\-qualified name to your method, the code you want the Lambda function to run\. The syntax is: `{Assembly}::{Namespace}.{ClassName}::{MethodName}`\. For more information, see [Handler signatures](https://docs.aws.amazon.com/lambda/latest/dg/csharp-handler.html#csharp-handler-signatures)\. Setting `image-command` here pre\-populates this value in Visual Studio's Publish wizard later on\. 

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
  "package-type": "image",
  "function-memory-size": 256,
  "function-timeout": 30,
  "image-command": "AWSLambdaDocker::AWSLambdaDocker.Function::FunctionHandler",
  "docker-host-build-output-dir": "./bin/Release/net5.0/linux-x64/publish"
}
```

Examine the `Function.cs` file\. `Function.cs` defines the c\# functions to expose as Lambda functions\. The `FunctionHandler` is the Lambda functionality that runs when the Lambda function runs\. In this project, there is one function defined: `FunctionHandler`, which calls ToUpper\(\) on the input text\. 

Your project is now ready to publish to Lambda\.

## Publish to Lambda<a name="publish-to-lam"></a>

Docker images that are generated by the build process are uploaded to Amazon Elastic Container Registry \(Amazon ECR\)\. Amazon ECR is a fully\-managed Docker container registry that you use to store, manage, and deploy Docker container images\. Amazon ECR hosts the image, which Lambda then references to provide the programmed Lambda functionality when invoked\. 

**To publish your function to Lambda**

1. In **Solution Explorer**, open the context \(right\-click\) menu for the project, and then choose **Publish to AWS Lambda**\.

1. On the **Upload Lambda Function** page, do the following:  
![\[Upload screen for publishing image-based Lambda function to AWS\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/UploadImageBasedLambda.PNG)

   1.  For **Package Type**, **Image** has been automatically selected as your **Package Type** because the publish wizard detected a `Dockerfile` within your project\. 

   1. For **Function Name**, enter a display name for your Lambda instance\. This name is the reference name displayed in the both the AWS Explorer in Visual Studio and the AWS Management Console\.

   1.  For **Description**, enter text to display with your instance in the AWS Management Console\.

   1. For **Image Command**, enter a fully\-qualified path to the method you want the Lambda function to run: **AWSLambdaDocker::AWSLambdaDocker\.Function::FunctionHandler** 
**Note**  
Any method name entered here will override any CMD instruction within the Dockerfile\. Entering **Image Command** is optional only IF your `Dockerfile` includes a `CMD` to instruct how to launch the Lambda function\.

   1. For **Image Repo**, enter the name of a new or existing Amazon Elastic Container Registry\. The Docker image the build process creates is uploaded to this registry\. The Lambda definition that is being published will reference that Amazon ECR image\.

   1.  For **Image Tag**, enter a Docker tag to associate with your image in the repository\. 

   1. Choose **Next**\.

1. On the **Advanced Function Details** page, in **Role Name** choose a role associated with your account\. The role is used to provide temporary credentials for any AWS service calls made by the code in the function\. If you do not have a role, choose **New Role based on AWS Managed Policy** and then choose **AWSLambdaBasicExecutionRole**\. 
**Note**  
Your account must have permission to run the IAM ListPolicies action, or the **Role Name** list will be empty\.

1. Choose **Upload**\.

   The **Uploading Function** page displays while the function is uploading\. The publish process then builds the image based on the configuration parameters, creates the Amazon ECR repository if necessary, uploads the image into the repository, and creates the Lambda referencing that repo with that image\. 

   After the function is uploaded, the **Function** page opens and displays your new Lambda function’s configuration\. 

1. To manually invoke the Lambda function, on the **Test Function** tab, enter `hello image based lambda` into the request free\-text input field and then choose **Invoke**\. Your text, converted to uppercase, will appear in **Response**\.   
![\[The Test Function tab of the published Function view page has button to manually invoke Lambda method.\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/invokeLambda.png)

1. To view the repository, in the **AWS Explorer**, under **Amazon Elastic Container Service**, choose **Repositories**\.

   You can reopen the **Function:** view at any time by double\-clicking on your deployed instance located in the **AWS Explorer** under the **AWS Lambda** node\.
**Important**  
If your AWS Explorer window is not open, you can dock it via **View** \-> **AWS Explorer**

1. Note additional image\-specific configuration options on the **Configuration** tab\. This tab provides a way to override the `ENTRYPOINT`, `CMD`, and `WORKDIR` that may have been specified within the Dockerfile\. **Description** is the description you entered \(if any\) during upload/publish\.

## Clean\-up<a name="cleanup-lam"></a>

If you are not going to continue developing with this example, remember to delete the function and ECR image that was deployed so that you do not get billed for unused resources in your account\. 
+ Functions can be deleted by right\-clicking your deployed instance located in the **AWS Explorer** under the **AWS Lambda** node\. 
+ Repositories can be deleted in the **AWS Explorer** under the **Amazon Elastic Container Service** \-> **Repositories**\.

## Next Steps<a name="next-steps-lam"></a>

For information about creating and testing Lambda images, see [Using Container Images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html)\.

For information about container image deployment, permissions, and overriding configuration settings, see [Configuring Functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-images.html)\.
