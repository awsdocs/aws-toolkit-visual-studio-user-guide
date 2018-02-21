.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

#########################
Providing AWS Credentials
#########################

.. meta::
    :description: Different ways to supply AWS credentials when using the AWS SDK for .NET.
    :keywords: configuration, prerequisites, region, credentials, uninstall

Before you can use the |TVS|, you must provide one or more sets of valid AWS credentials. These
credentials allow you to access your AWS resources through the |TVS|. They're also used to sign
programmatic web services requests, so AWS can verify that the request comes from an authorized source.

.. important:: AWS credentials consist of an access key and a secret key. We recommend that you do
   not use your account's root credentials. Instead, create one or more |IAM| users, and then use
   those credentials. For more information, see `Using IAM Users <https://aws.amazon.com/blogs/developer/using-iam-users-access-key-management-for-net-applications-part-2/>`_ and :aws-gr:`Best Practices for Managing AWS Access Keys <aws-access-keys-best-practices>`.

The |TVS| supports multiple sets of credentials from any number of accounts. Each set is referred to
as a *profile*. When you add a profile to |TVS|, the credentials are encrypted and stored in the SDK
Credential Store. This is also used by the |sdk-net|_ and the `AWS Tools for Windows PowerShell <TWP-ug_>`_.
The SDK Credential Store is specific to your Windows user account on your machine and can't be decrypted
or used elsewhere.

In addition to the encrypted SDK Credential Store, the |TVS| can also read credentials from
the plain-text shared credentials file used by other AWS SDKs and the AWS CLI. To use the |TVS|, at least
one credential profile must be available from either the SDK Credential Store or the shared credential
file.

.. note:: Credential profiles created using the |TVS| are saved only to the encrypted SDK Credential
   Store. Multi-Factor Authentication (MFA) profiles are not supported by the |TVS|.


.. _tkv-creds-add-profile

Adding a profile to the SDK Credential Store
============================================

To add a profile to the SDK Credential Store:

1. Open AWS Explorer in Visual Studio. On the :guilabel:`View` menu, choose
   :guilabel:`AWS Explorer`. Or press :kbd:`Ctrl+K`, and then press :kbd:`A`.

2. Choose the :guilabel:`New Account Profile` icon to the right of the :guilabel:`Profile` list.

   .. image:: images/add_profile.png
      :scale: 85

   The New Account Profile dialog box opens.

   .. figure:: images/tkv-account-add.png
      :scale: 100

3. To create a credential profile, enter the following data into the dalog box. When you create an account
   in the |console|, or create an |IAM| user and set up credentials for the user, you are prompted to download
   and save the generated credentials. You can choose :guilabel:`Import from cvs file` to browse
   to the
   file containing the access and secret key credentials, and automatically import them into the dialog
   box.

   :guilabel:`Profile Name`
      (Required) The profile's display name.

   :guilabel:`Access Key ID`
      (Required) The access key.

   :guilabel:`Secret Access Key`
      (Required) The secret key.

   :guilabel:`Account Number`
      (Optional) The credential's account number. The |TVS| uses the account number to construct
      Amazon Resource Names (ARNs).

   Account Type
     (Required) The account type. This entry determines which regions are displayed in AWS
     Explorer when you specify this profile. For :guilabel:`Standard AWS Account`:

     * If you choose |GOVCLOUD-US| Account, AWS Explorer displays only the
       |GOVCLOUD-US| region.

     * If you choose :guilabel:`Amazon AWS Account - China (Beijing) Region`, AWS Explorer
       displays only the |cnnorth1-name|.

4. To add the profile to the SDK Credential Store, choose :guilabel:`OK`.

After you add the first profile, you can also do the following:

* To add another profile, repeat the procedure.

* To delete a profile, choose it, and then choose the :guilabel:`Delete Profile` icon.

* To edit a profile, choose the :guilabel:`Edit Profile` icon to open the :guilabel:`Edit Profile dialog box.

  For example, if you have :aws-gr:`rotated an IAM user's credentials
  <aws-access-keys-best-practices>` |mdash| a recommended
  practice |mdash| you can edit the profile to update the user's credentials in the SDK Credential Store. For
  more information, see `IAM Credential Rotation  <https://aws.amazon.com/blogs/developer/iam-credential-rotation-access-key-management-for-net-applications-part-3/>`_.

You can also add profiles to the SDK Credential Store when you create an AWS project. Before Visual Studio
creates the project files, it displays the :guilabel:`AWS Access Credentials` dialog box. You can
choose an existing profile from the SDK Credential Store or create one.

.. figure:: images/specify_creds.png
    :scale: 100

.. topic:: Adding a profile to the AWS credentials profile file

Adding a profile to the AWS credentials profile file
=====================================================

You can set your credentials in the AWS credentials profile file on your local system, located 
at |aws-credfile-loc-windows| on Windows

This file should contain lines in the following format:

    .. code-block:: cfg

        [default]
        aws_access_key_id = your_access_key_id
        aws_secret_access_key = your_secret_access_key
     
Substitute your own AWS credentials values for the values *your_access_key_id* and
*your_secret_access_key*.

You can use a role by creating a profile for the role. 
The following example shows a role profile named ``assumed-role`` that is assumed by the default profile.

    .. code-block:: cfg
    
        [assume-role-test]
        role_arn = arn:aws:iam::123456789012:role/assumed-role
        source_profile = default

In this case, the default profile is an |IAM| user with credentials and permission to assume a role named ``assumed-role``. 
To access the role, you create a named profile, in this case ``assume-role-test``. Instead of configuring this profile with credentials, 
you specify the ARN of the role and the name of the profile that has access to it. 

For an EC2 instance, specify an IAM role and then give your EC2 instance access to that role. 
See :ec2-ug:`IAM Roles for Amazon EC2 <iam-roles-for-amazon-ec2>` in the |EC2-ug| for a detailed discussion about how this works.
