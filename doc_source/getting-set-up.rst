.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv_setup:

########################
Setting Up the |TVSlong|
########################


.. meta::
   :description: How to set up the AWS Toolkit for Visual Studio.
   :keywords: configuration, prerequisites, region, credentials, uninstall

This topic describes how to install and configure the |TVS|.

.. _prereqs:

Prerequisites
=============

To install and configure the |TVS|, you must:

* Have an AWS account. This account enables you to use AWS services. To get an AWS account, on
  the `AWS home page <http://aws.amazon.com/>`_, choose :guilabel:`Create an AWS Account`.

* Run a supported operating system: Windows 10, Windows 8, or Windows 7.

  We recommend that you install the latest service packs and updates for the Windows version
  you're using.

* Visual Studio 2013 or later (including Community editions).

  We recommend that you install the latest service packs and updates.

.. note:: The |TVS| is still available if you're using Visual Studio versions 2008, 2010, and 2012 (including
   Express editions where available). However, it is not supported. For Express editions, the
   installation includes only the AWS project templates and the :ref:`standalone deployment tool
   <tkv-deployment-tool>`. Visual Studio Express editions don't support third-party extensions, such as
   AWS Explorer. Find links to these older versions of the |TVS| at the bottom of this page.

.. _install:

Install the |TVS|
=================

The |TVS| 2017 is distributed in the Visual Studio Marketplace. You can download and install 
the toolkit at https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2017.
You can also install and update the toolkit using the Extensions and Updates dialog within Visual Studio.

The |TVS| 2013 and 2015 versions is part of the |TFW|. You can install the |TFW| for these versions as
follows.

.. topic:: To install the |TFW|

1. Navigate to the page `AWS Toolkit for Visual Studio <https://aws.amazon.com/visualstudio>`_.

2. In the :guilabel:`Download` section, choose |TVS| to download the installer.

3. To start the installation, run the downloaded installer and follow the instructions.

.. tip:: By default, the |TVS| is installed in the Program Files directory, which requires
   administrator privileges. To install the |TVS| as a non-administrator, specify a different
   installation directory.

.. _creds:

Specify Credentials
===================

Before you can use the |TVS|, you must provide one or more sets of valid AWS credentials. These
credentials allow you to access your AWS resources through the |TVS|. They're also used to sign
programmatic web services requests, so AWS can verify that the request comes from an authorized source.

.. important:: AWS credentials consist of an access key and a secret key. We recommend that you do
   not use your account's root credentials. Instead, create one or more |IAM| users, and then use
   those credentials. For more information, see
   :aws-blogs-net:`Using IAM Users <Tx2O8RZZ1RLE898Using-IAM-Users-Access-Key-Management-for-NET-Applications-Part-2>`
   and :aws-gr:`Best Practices for Managing AWS Access Keys <aws-access-keys-best-practices>`.

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
   Store.


.. topic:: To add a profile to the SDK Credential Store

1. Open AWS Explorer in Visual Studio. On the :guilabel:`View` menu, choose
   :guilabel:`AWS Explorer`. Or press :kbd:`Ctrl+K`, and then press :kbd:`A`.

2. Choose the :guilabel:`New Account Profile` icon to the right of the :guilabel:`Profile` list.

   .. image:: images/add_profile.png
      :scale: 85

   The New Account Profile dialog box opens.

   .. figure:: images/tkv-account-add.png
      :scale: 100

4. To create a credential profile, enter the following data into the dalog box. When you create an account
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

5. To add the profile to the SDK Credential Store, choose :guilabel:`OK`.

After you add the first profile, you can also do the following:

* To add another profile, repeat the procedure.

* To delete a profile, choose it, and then choose the :guilabel:`Delete Profile` icon.

* To edit a profile, choose the :guilabel:`Edit Profile` icon to open the :guilabel:`Edit Profile dialog box.

  For example, if you have :aws-gr:`rotated an IAM user's credentials
  <aws-access-keys-best-practices>` |mdash| a recommended
  practice |mdash| you can edit the profile to update the user's credentials in the SDK Credential Store. For
  more information, see :aws-blogs-net:`IAM Credential Rotation
  <Tx2DJQU2MKGR463/IAM-Credential-Rotation-Access-Key-Management-for-NET-Applications-Part-3>`.

You can also add profiles to the SDK Credential Store when you create an AWS project. Before Visual Studio
creates the project files, it displays the :guilabel:`AWS Access Credentials` dialog box. You can
choose an existing profile from the SDK Credential Store or create one.

.. figure:: images/specify_creds.png
    :scale: 100

.. _uninstall:

Uninstall the |TVS|
===================

To uninstall the |TVS|, you must uninstall the |TFW|.

.. topic:: To uninstall the |TFW|

1. In Control Panel, open :guilabel:`Programs and Features`.

  .. tip:: To open :guilabel:`Programs and Features` directly, from a command prompt, run the following:
     :code:`appwiz.cpl`

2. Choose |TFW|, and then choose :guilabel:`Uninstall`.

   .. figure:: images/uninstall.png
      :scale: 100

3. If prompted, choose :guilabel:`Yes`.

Uninstalling the |TFW| doesn't remove the Samples directory. This directory is preserved in case
you have modified the samples. You have to manually remove this directory.


.. _older_versions:

Older Versions of the |TVS|
===========================

**Visual Studio 2008** |mdash| Install the |TVS| for Visual Studio 2008 from
https://sdk-for-net.amazonwebservices.com/latest/AWSToolkitForVisualStudio2008.msi.

**Visual Studio 2010 and 2012** |mdash| Install the |TVS| for Visual Studio 2010 and 2012
from https://sdk-for-net.amazonwebservices.com/latest/AWSToolkitForVisualStudio2010-2012.msi.


