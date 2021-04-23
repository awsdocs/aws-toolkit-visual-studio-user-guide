# Providing AWS credentials<a name="credentials"></a>

Before you can use the Toolkit for Visual Studio, you must provide one or more sets of valid AWS credentials\. These credentials allow you to access your AWS resources through the Toolkit for Visual Studio\. They're also used to sign programmatic web services requests so that AWS can verify that the request comes from an authorized source\.

**Important**  
AWS credentials consist of an access key ID and secret access key\. We recommend that you do NOT use your account's root credentials\. Instead, [create one or more IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html), and then use those credentials\. For additional information, see [Using IAM Users](http://aws.amazon.com/blogs/developer/using-iam-users-access-key-management-for-net-applications-part-2/) and [Best Practices for Managing AWS Access Keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)\.

## Credentials locations<a name="credentials-locations"></a>

The Toolkit for Visual Studio supports multiple sets of credentials from any number of AWS accounts\. Each credentials set is referred to as a *profile*\. The Toolkit for Visual Studio works with profiles stored in the following locations: 
+ **Shared AWS files:** By default, these files are located in the `.aws` directory in your home directory and are named `config` and `credentials`\. \(The location of your home directory varies based on the operating system, but is referred to using the environment variables `%UserProfile%` in Windows and `$HOME` or `~` \(tilde\) in Unix\-based systems\.\) 

  Credentials stored in these files are in plaintext, and are accessible by the AWS CLI and the AWS SDKs\.

  For more information, see [Where Are Configuration Settings Stored?](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where) in the *AWS Command Line Interface User Guide*\.
+ **SDK Store:** On Windows systems, the SDK Store is another place to create profiles and store encrypted credentials for your AWS for \.NET applications\. It's located in `%USERPROFILE%\AppData\Local\AWSToolkit\RegisteredAccounts.json`\. You can use the SDK Store during development as an alternative to the shared AWS credentials file\.

  Credentials stored here are encrypted on your machine, and are specific to your Windows user account\. They can't be decrypted or used elsewhere\.

   For more information, see [Configuring AWS credentials](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-config-creds.html) in the *AWS SDK for \.NET Developer Guide*\.

## Options for configuring credentials<a name="configuring-credentials"></a>

To work with AWS services using the Toolkit for Visual Studio, you need to configure **at least one credential profile** that's available in either the shared AWS credentials file or the SDK Store\.

 For options for obtaining the necessary access keys and adding them to a profile that's stored in either a shared AWS credentials file or SDK Store, see [Creating profiles for your AWS credentials](keys-profiles-credentials.md)\. And you can enhance your access credentials by adding entries to profiles that define how to use [AWS Single Sign\-On \(AWS SSO\)](sso-credentials.md) and [multi\-factor authentication \(MFA\)](mfa-credentials.md)\.

**Topics**
+ [Credentials locations](#credentials-locations)
+ [Options for configuring credentials](#configuring-credentials)
+ [Creating profiles for your AWS credentials](keys-profiles-credentials.md)
+ [Using AWS SSO credentials in AWS Toolkit for Visual Studio](sso-credentials.md)
+ [Using multi\-factor authentication \(MFA\) in Toolkit for Visual Studio](mfa-credentials.md)
+ [Using external credentials](external-credentials.md)