# Providing AWS Credentials<a name="credentials"></a>

Before you can use the Toolkit for Visual Studio, you must provide one or more sets of valid AWS credentials\. These credentials allow you to access your AWS resources through the Toolkit for Visual Studio\. They're also used to sign programmatic web services requests, so AWS can verify that the request comes from an authorized source\.

**Important**  
AWS credentials consist of an access key and a secret key\. We recommend that you do not use your account's root credentials\. Instead, create one or more IAM users, and then use those credentials\. For more information, see [Using IAM Users](http://aws.amazon.com/blogs/developer/using-iam-users-access-key-management-for-net-applications-part-2/) and [Best Practices for Managing AWS Access Keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)\.

The Toolkit for Visual Studio supports multiple sets of credentials from any number of accounts\. Each set is referred to as a *profile*\. When you add a profile to Toolkit for Visual Studio, the credentials are encrypted and stored in the SDK Credential Store\. This is also used by the [AWS SDK for \.NET](https://aws.amazon.com/sdk-for-net/) and the [AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/)\. The SDK Credential Store is specific to your Windows user account on your machine and can't be decrypted or used elsewhere\.

In addition to the encrypted SDK Credential Store, the Toolkit for Visual Studio can also read credentials from the plain\-text shared credentials file used by other AWS SDKs and the AWS CLI\. To use the Toolkit for Visual Studio, at least one credential profile must be available from either the SDK Credential Store or the shared credential file\.

**Note**  
Credential profiles created using the Toolkit for Visual Studio are saved only to the encrypted SDK Credential Store\. Multi\-Factor Authentication \(MFA\) profiles are not supported by the Toolkit for Visual Studio\.

## Adding a profile to the SDK Credential Store<a name="adding-a-profile-to-the-sdk-credential-store"></a>

To add a profile to the SDK Credential Store:

1. Open AWS Explorer in Visual Studio\. On the **View** menu, choose **AWS Explorer**\. Or press `Ctrl+K`, and then press `A`\.

1. Choose the **New Account Profile** icon to the right of the **Profile** list\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/add_profile.png)

   The New Account Profile dialog box opens\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/tkv-account-add.png)

1. To create a credential profile, enter the following data into the dalog box\. When you create an account in the AWS Management Console, or create an IAM user and set up credentials for the user, you are prompted to download and save the generated credentials\. You can choose **Import from cvs file** to browse to the file containing the access and secret key credentials, and automatically import them into the dialog box\.  
** **Profile Name** **  
\(Required\) The profile's display name\.  
** **Access Key ID** **  
\(Required\) The access key\.  
** **Secret Access Key** **  
\(Required\) The secret key\.  
** **Account Number** **  
\(Optional\) The credential's account number\. The Toolkit for Visual Studio uses the account number to construct Amazon Resource Names \(ARNs\)\.  
**Account Type**  
\(Required\) The account type\. This entry determines which regions are displayed in AWS Explorer when you specify this profile\. For **Standard AWS Account**:  
   + If you choose AWS GovCloud \(US\) Account, AWS Explorer displays only the AWS GovCloud \(US\) region\.
   + If you choose **Amazon AWS Account \- China \(Beijing\) Region**, AWS Explorer displays only the China \(Beijing\) Region\.

1. To add the profile to the SDK Credential Store, choose **OK**\.

After you add the first profile, you can also do the following:
+ To add another profile, repeat the procedure\.
+ To delete a profile, choose it, and then choose the **Delete Profile** icon\.
+ To edit a profile, choose the **Edit Profile** icon to open the **Edit Profile** dialog box\.

  For example, if you have [rotated an IAM user's credentials](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)—a recommended practice—you can edit the profile to update the user's credentials in the SDK Credential Store\. For more information, see [IAM Credential Rotation](http://aws.amazon.com/blogs/developer/iam-credential-rotation-access-key-management-for-net-applications-part-3/)\.

You can also add profiles to the SDK Credential Store when you create an AWS project\. Before Visual Studio creates the project files, it displays the **AWS Access Credentials** dialog box\. You can choose an existing profile from the SDK Credential Store or create one\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/specify_creds.png)

## Adding a profile to the AWS credentials profile file<a name="adding-a-profile-to-the-aws-credentials-profile-file"></a>

You can set your credentials in the AWS credentials profile file on your local system, located at `C:\Users\USERNAME\.aws\credentials` on Windows

This file should contain lines in the following format:

```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```

Substitute your own AWS credentials values for the values *your\_access\_key\_id* and *your\_secret\_access\_key*\.

You can use a role by creating a profile for the role\. The following example shows a role profile named `assumed-role` that is assumed by the default profile\.

```
[assume-role-test]
role_arn = arn:aws:iam::123456789012:role/assumed-role
source_profile = default
```

In this case, the default profile is an IAM user with credentials and permission to assume a role named `assumed-role`\. To access the role, you create a named profile, in this case `assume-role-test`\. Instead of configuring this profile with credentials, you specify the ARN of the role and the name of the profile that has access to it\.

For an EC2 instance, specify an IAM role and then give your EC2 instance access to that role\. See [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon EC2 User Guide for Linux Instances* for a detailed discussion about how this works\.