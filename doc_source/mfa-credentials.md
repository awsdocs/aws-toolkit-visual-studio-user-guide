# Using multi\-factor authentication \(MFA\) in Toolkit for Visual Studio<a name="mfa-credentials"></a>

Multi\-factor authentication \(MFA\) offers increased security because it requires users to provide unique authentication from an AWS supported MFA mechanism in addition to their regular sign\-in credentials when they access AWS websites or services\.

AWS supports a range of both virtual and hardware devices for MFA authentication\. The example that's documented here is a virtual MFA device that's enabled by a smartphone application\. For more information on MFA device options, see [Using multi\-factor authentication \(MFA\) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the *IAM User Guide*\.

## Step 1: Creating an IAM role to delegate access to IAM users<a name="create-mfa-role"></a>

This task uses [role delegation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) to allow an IAM to delegate permissions to an IAM user\. First, you define an IAM role that requires signing in with MFA\. You also attach policies to that role that grant permissions to access specific AWS services\. Next, you create an IAM user that has no permissions to start with\. But you then attach to that user a policy that includes the `AssumeRole` operation, which delegates all the role's permissions to the user\.

1. Go to the IAM console at [https://console\.aws\.amazon\.com/iam](https://console.aws.amazon.com/iam)\.

1. Choose **Roles** in the navigation bar, and then choose **Create Role**\.

1. In the **Create role** page, choose **Another AWS account**\.

1. Enter your required **Account ID** and mark the **Require MFA** check box\. 
**Note**  
To find your 12\-digit account number \(ID\), go to the navigation bar in the console, and then choose **Support**, **Support Center**\.

1. Choose **Next: Permissions**\.

1. Attach existing policies to your role or create a new policy for it\. The policies that you choose on this page determine which AWS services the IAM user can access with the Toolkit\.

1. After attaching policies, choose **Next: Tags** for the option of adding IAM tags to your role\. Then choose **Next: Review** to continue\.

1. In the **Review** page, enter a required **Role name** \(*toolkit\-role*, for example\)\. You can also add an optional **Role description**\. 

1. Choose **Create role**\.

1. When the confirmation message displays \("The role **toolkit\-role** has been created", for example\), choose the name of the role in the message\.

1. In the **Summary** page, choose the copy icon to copy the **Role ARN** and paste it into a file\. \(You need this ARN when configuring the IAM user to assume the role\.\)\.

## Step 2: Creating an IAM user that assumes the role's permissions<a name="create-mfa-user"></a>

In this step, you first create the IAM user without permissions\. Then you create an in\-line policy that allows the user to assume the role \(and that role's permissions\) that you created in the previous step\.

## To create the IAM user

1. Go to the IAM console at [https://console\.aws\.amazon\.com/iam](https://console.aws.amazon.com/iam)\.

1. Choose **Users** in the navigation bar and then choose **Add user**\.

1. In the **Add user** page, enter a required **User name** \(*toolkit\-user*, for example\) and mark the **Programmatic access** check box\.

1. Choose **Next: Permissions**, **Next: Tags**, and **Next: Review** to move through the next pages\. You're not adding permissions at this stage because the user is going to assume the role's permissions\.

1. In the **Review** page, you're informed that **This user has no permissions**\. Choose **Create user**\.

1. In the **Success** page, choose **Download \.csv** to download the file containing the access key ID and secret access key\. \(You need both when defining the user's profile in the credentials file\.\)

1. Choose **Close**\.

## To add a policy to allow the IAM user to assume the role

1. In the **Users** page of the IAM console, choose the IAM user you've just created \(*toolkit\-user*, for example\)\.

1. In the **Permissions** tab of the **Summary** page, choose **Add inline policy**\. 

1. In the **Create policy** page, choose **Choose a service**, enter **STS** in **Find a service**, and then choose **STS** from the results\. 

1. For **Actions**, start entering the term *AssumeRole*\. Mark the **AssumeRole** check box when it appears\. 

1. In the **Resource section**, ensure **Specific** is selected, and click **Add ARN** to restrict access\.

1. In the **Add ARN\(s\)** dialog box, for the **Specify ARN for role** add the ARN of the role you that you created in Step 1\.

   After you add the role's ARN, the trusted account and role name associated with that role are displayed in **Account** and **Role name with path**\.

1. Choose **Add**\.

1. Back in the **Create policy** page, choose **Specify request conditions \(optional\)**, mark the **MFA required** check box, and then choose **close** to confirm\.\.

1. Choose **Review policy**

1. In **Review policy** page, enter a **Name** for the policy, and then choose **Create policy**\.

   The **Permissions** tab displays the new inline policy attached directly to IAM user\.

## Step 3: Managing a virtual MFA device for the IAM user<a name="manage-virtual-mfa"></a>

1. Download and install a virtual MFA application to your smartphone\.

    For a list of supported applications, see the [Multi\-factor Authentication](https://aws.amazon.com/iam/features/mfa/?audit=2019q1) resource page\.

1. In the IAM console, choose **Users** from the navigation bar and then choose the user that's assuming a role \(*toolkit\-user*, in this case\)\. 

1. In the **Summary** page, choose the **Security credentials** tab, and for **Assigned MFA device** choose **Manage**\.

1. In the **Manage MFA device** pane, choose **Virtual MFA device**, and then choose **Continue**\.

1. In the **Set up virtual MFA device** pane, choose **Show QR code** and then scan the code using the virtual MFA application that you installed on your smartphone\.

1. After you scan the QR code, the virtual MFA application generates one\-time MFA codes\. Enter two consecutive MFA codes in **MFA code 1** and **MFA code 2**\.

1. Choose **Assign MFA**\.

1. Back in the **Security credentials** tab for the user, copy the ARN of the new **Assigned MFA device**\.

   The ARN includes your 12\-digit account ID and the format is similar to the following: `arn:aws:iam::123456789012:mfa/toolkit-user`\. You need this ARN when defining the MFA profile in the next step\.

## Step 4: Creating profiles to allow MFA<a name="mfa-profiles"></a>

In this step, you create the profiles that allow users of the Toolkit for Visual Studio to use MFA when accessing AWS services\.

The profiles that you create include three pieces of information that you've copied and stored during the previous steps:
+ Access keys \(access key ID and secret access key\) for the IAM user
+ ARN of the role that's delegating permissions to the IAM user 
+ ARN of the virtual MFA device that's assigned to the IAM user 

In the AWS shared credential file or SDK Store that contain your AWS credentials, add the following entries:

```
[toolkit-user]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[mfa]
source_profile = toolkit-user
role_arn = arn:aws:iam::111111111111:role/toolkit-role
mfa_serial = arn:aws:iam::111111111111:mfa/toolkit-user
```

There are two profiles defined in the example provided:
+ `[toolkit-user]` profile includes the access key and secret access key that were generated and saved when you created the IAM user in Step 2\.
+ `[mfa]` profile defines how multi\-factor authentication is supported\. There are three entries:

  ◦ `source_profile`: Specifies the profile whose credentials are used to assume the role specified by this `role_arn` setting in this profile\. In this case, it's the `toolkit-user` profile\.

  ◦ `role_arn`: Specifies the Amazon Resource Name \(ARN\) of the IAM role that you want to use to perform operations requested using this profile\. In this case, it's the ARN for the role you created in Step 1\.

  ◦ `mfa_serial`: Specifies the identification or serial number of the MFA device that the user must use when assuming a role\. In this case, it's the ARN of the virtual device you set up in Step 3\.