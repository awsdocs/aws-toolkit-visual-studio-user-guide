# Using AWS SSO credentials in AWS Toolkit for Visual Studio<a name="sso-credentials"></a>

AWS Single Sign\-On \(AWS SSO\) is a cloud\-based single sign\-on \(SSO\) service that makes it easy to centrally manage SSO access to all of your AWS accounts and cloud applications\. 

To connect with AWS Single Sign\-On \(AWS SSO\), you must complete the following prerequisite:
+ **Set up AWS SSO** – This includes choosing your identity source and setting up AWS SSO access to your AWS accounts\. For more information, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS Single Sign\-On User Guide*\.

After AWS SSO is set for your AWS accounts, you can define a named profile in the `credentials` file or `config` file that you use to retrieve temporary credentials for your AWS account\. This profile definition specifies the AWS SSO [user portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html) as well as the AWS account and IAM role associated with the user requesting access\.

## To add an AWS SSO profile<a name="adding-sso-profile"></a>

The following procedure outlines how to add an AWS SSO profile to your `credentials` or `config` file\.

**Adding an AWS SSO profile to your credentials file in AWS Toolkit for Visual Studio**

1. Use your preferred text editor to open the AWS credentials information stored in the `<hone-directory>\.aws\credentials` file\.

1. In either the `credentials` or `config` file, under `[default]`, add a template for a named AWS SSO profile\. An example profile:

   ```
   ... Named profile in credentials file ...
   
   [sso-user-1]
   sso_start_url = https://example.com/start
   sso_region = us-east-2
   sso_account_id = 123456789011
   sso_role_name = readOnly
   region = us-west-2
   ```
**Important**  
Do not use the word *profile* when creating an entry in the `credentials` file\. This is because the `credentials` file uses a different naming format than the `config` file\. Include the prefix word `profile_` only when configuring a named profile in the `config` file\.

When you assign values for your profile, keep the following in mind:
+ **`sso_start_url`**: The URL that points to your organization's AWS SSO user portal\.
+ **`sso_region`**: The AWS Region that contains your AWS SSO portal host\. This can be different from the AWS Region specified later in the default `region` parameter\.
+ **`sso_account_id`**: The AWS account ID that contains the IAM role with the permission that you want to grant to this AWS SSO user\.
+ **`sso_role_name`**: The name of the IAM role that defines the user's permissions when using this profile to get credentials through AWS SSO\.
+ **`region`**: The default AWS Region that this AWS SSO user signs into\.

**Note**  
You can also add an AWS SSO enabled profile to your AWS CLI by running the `aws configure sso` command\. After running this command, you provide values for the AWS SSO start URL \(`sso_start_url`\) and the AWS Region \(`region`\) that hosts the AWS SSO directory\.  
For more information, see [Configuring the AWS CLI to use AWS Single Sign\-On](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*\.

### Signing in with AWS SSO<a name="sso-sign-in"></a>

When signing in with an AWS SSO profile, the default browser is launched to the specified portal\. You must verify your AWS SSO login before you can access your AWS resources in AWS Toolkit for Visual Studio\. If your credentials expire, you'll have to repeat the connection process to obtain new temporary credentials\.