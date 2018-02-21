.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-specify-credentials-for-application:

################################################################
How to Specify the AWS Security Credentials for Your Application
################################################################

.. meta::
   :description: Specify security credentials using the Toolit for Visual Studio.
   :keywords: deployment, security, credentials, Elastic Beanstalk

The AWS account you specify in the :guilabel:`Publish to Elastic Beanstalk` wizard (or the legacy
version of this wizard, :guilabel:`Publish to Amazon Web Services`) is the AWS account the wizard
will use for deployment to |EB|. 

Although not recommended, you may also need to specify AWS account
credentials that your application will use to access AWS services after it has been deployed. The
preferred approach is to specify an |IAM| role. In the :guilabel:`Publish to Elastic Beanstalk`
wizard, you do this through the :guilabel:`Identity and Access Management Role` drop-down list on
the :guilabel:`AWS Options` page. In the legacy :guilabel:`Publish to Amazon Web Services` wizard,
you do this through the :guilabel:`IAM Role` drop-down list on the :guilabel:`AWS Options` page.

If you must use AWS account credentials instead of an |IAM| role, you can specify the AWS account
credentials for your application in one of the following ways:

* Reference a profile corresponding to the AWS account credentials in the :code:`appSettings` element
  of the project's :file:`Web.config` file. (To create a profile, see 
  :sdk-net-dg:`Configuring AWS Credentials <net-dg-config-creds>`.) The following example specifies 
  credentials whose profile name is :code:`myProfile`.

  .. code-block:: xml

      <appSettings>
        <!-- AWS CREDENTIALS -->
        <add key="AWSProfileName" value="myProfile"/>
      </appSettings>

* If you're using the :guilabel:`Publish to Elastic Beanstalk` wizard, on the :guilabel:`Application 
  Options` page, in the :guilabel:`Key` row of the :guilabel:`Key` and :guilabel:`Value` area,
  choose :guilabel:`AWSAccessKey`. In the :guilabel:`Value` row, type the access key. Repeat these
  steps for :guilabel:`AWSSecretKey`.

  
* If you're using the legacy :guilabel:`Publish to Amazon Web Services` wizard, on the
  :guilabel:`Application Options` page, in the :guilabel:`Application Credentials` area, choose
  :guilabel:`Use these credentials`, and then type the access key and secret access key into the
  :guilabel:`Access Key` and :guilabel:`Secret Key` boxes.


