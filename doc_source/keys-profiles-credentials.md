# Creating profiles for your AWS credentials<a name="keys-profiles-credentials"></a>

Configuring access credentials for Toolkit for Visual Studio involves obtaining access keys and adding those keys to a set of credentials called a *profile*\. You can store multiple profiles in shared AWS credentials files or in the SDK Store\.

You've several options for adding profiles to your AWS credentials:
+ Using the AWS Explorer interface available in the Toolkit for Visual Studio
+ Editing the credentials file with a text editor
+ Creating a profile with the `aws configure` command

## Obtaining access keys for your profile<a name="accesskeys-for-toolkit"></a>

Toolkit for Visual Studio allows you to interact with a wide range of AWS services, so you should ensure that the IAM entity that's used has the necessary permissions to interact with those services\. You can allow Toolkit for Visual Studio to access your AWS services by manually creating your own set of credentials called a *profile*\. Profiles feature long\-term credentials called access keys, which you can obtain from the IAM console\.

**Note**  
The following procedure shows how you can use the IAM console to create access keys\. You can also manage access keys using AWS CLI commands and AWS API operations\. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) in the *IAM User Guide*\. <a name="manual-credentials"></a>

**To obtain access keys for a profile**

1. To get your access keys \(consisting of an *access key ID* and *secret access key*\), go to the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. Choose **Users** from the navigation bar and then choose your AWS user name \(not the check box\)\.

1. Choose the **Security credentials** tab, and then choose **Create access key**\.
**Note**  
If you already have an access key but you can't access your secret key, make the old key inactive and create a new one\.

1. In the dialog box that shows your access key ID and secret access key, choose **Download \.csv file** to store this information in a secure location\.

After you've stored your access keys securely, you can then add them to the set of credentials defined by a profile\.

## Using AWS Explorer to add a profile to the SDK Store or the shared AWS credentials files<a name="adding-a-profile-to-the-sdk-credential-store"></a>

To add a profile to the SDK Credential Store or the shared AWS credentials file:

1. To open AWS Explorer in Visual Studio, choose **View**, **AWS Explorer**\.

1. Choose the **New Account Profile** icon to the right of the **Credentials:** list\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/credentials_ui.png)

   The New Account Profile dialog box opens\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/tkv-account-add-update.png)

1. To create a credential profile, enter the following data into the dialog box and then choose **OK**\.
**Note**  
When you create an account in the AWS Management Console, or when you [create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) and set up credentials for the user, you are given the opportunity to download and save the generated credentials as a `.csv` file\. \(This is NOT the shared AWS credentials file\.\)  
If you have downloaded this file, you can choose **Import from csv file\.\.\.** to browse for the file and automatically import the access key ID and secret access key into the dialog box\.  
** **Profile Name** **  
\(Required\) The profile's display name\.  
**Storage Location**  
\(Required\) Choose whether to use the SDK Credential Store or the shared AWS credentials file\.  
** **Access Key ID** **  
\(Required\) The access key ID\.  
** **Secret Access Key** **  
\(Required\) The secret access key\.  
** **Region** **  
\(Required\) The default AWS Region that you want to associate this profile with\.  
If the Regions that you're working with are not shown \(for example, if you're working with GovCloud or a China\-based Region\), choose **Show more regions**\. You can then choose a **Partition**, which changes the list of available Regions to choose from\.

After you add the first profile, you can also do the following:
+ To add another profile, repeat the procedure\.
+ To delete a profile, choose it in **Credentials:**, and then choose the **Delete Profile** icon\.
+ To edit a profile, choose it in **Credentials:**, and then choose the **Edit Profile** icon to open the **Edit Profile** dialog box\.

  For example, if you have [rotated an IAM user's credentials](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)—a recommended practice—you can edit the profile to update the user's credentials in the SDK Store or shared AWS credentials file\. For more information, see [IAM Credential Rotation](http://aws.amazon.com/blogs/developer/iam-credential-rotation-access-key-management-for-net-applications-part-3/)\. 
**Important**  
You can't edit a profile that supports advanced access features such as [AWS SSO](sso-credentials.md) or [MFA](mfa-credentials.md) in the **Edit Profile** dialog box\. For these types of profile, use your [preferred text editor](#adding-a-profile-to-the-aws-credentials-profile-file)\.

## Adding a profile by editing the shared AWS credentials file<a name="adding-a-profile-to-the-aws-credentials-profile-file"></a>

Instead of managing profiles with the Toolkit for Visual Studio interface, you can update credentials information by editing the shared AWS credentials file using your preferred text editor\. On Windows systems, this file is called `C:\Users\USERNAME\.aws\credentials`\.

This file should contain lines in the following format:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

You can use a role by creating a profile for the role\. The following example shows a role profile named `assumed-role` that is assumed by the default profile\.

```
[assume-role-test]
role_arn = arn:aws:iam::123456789012:role/assumed-role
source_profile = default
```

In this case, the default profile is an IAM user with credentials and permission to assume a role named `assumed-role`\. To access the role, you create a named profile, in this case `assume-role-test`\. Instead of configuring this profile with credentials, you specify the ARN of the role and the name of the profile that has access to it\.

For an EC2 instance, specify an IAM role and then give your EC2 instance access to that role\. See [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon EC2 User Guide for Linux Instances* for a detailed discussion about how this works\.

## Using `aws configure` to create a profile<a name="aws-configure-profile"></a>

You can also use the AWS CLI command `aws configure` to create a profile named `default` in the `credentials` file\.

When you enter `aws configure` at the command line, you're asked for four pieces of information:
+ Access key ID
+ Secret access key
+ AWS Region
+ Output format

The following example shows sample values:

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

Toolkit for Visual Studio also supports the following configuration properties:

```
aws_access_key_id
aws_secret_access_key
aws_session_token
credential_process
credential_source
external_id
mfa_serial
role_arn
role_session_name
source_profile
sso_account_id
sso_region
sso_role_name
sso_start_url
```

For more information, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide*\.