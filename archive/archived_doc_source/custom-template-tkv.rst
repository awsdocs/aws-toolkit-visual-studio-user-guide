.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-custom-templates:

###############################################################
Customizing the AWS CloudFormation Template Used for Deployment
###############################################################

In addition to modifying a deployment by specifying parameters in the deployment wizard |mdash| or
in the configuration file for the standalone deployment tool |mdash| you can also modify the
deployment by providing your own custom AWS CloudFormation template. By default, the deployment
automatically uses one of a set of templates that are stored in |S3long| (|S3|). This default set of 
templates includes two templates for each :rande:`AWS region`. One of these two 
is for deployment to a single |EC2long| (|EC2|) instance; the other is for deployment to a 
load-balanced set of |EC2| instances. You can use these templates as a starting point for creating 
your own.

To create your own custom template
==================================

1. Copy the template that corresponds to your region and the type of deployment that you want to do.
   Links to each of the templates is provided below.

   .. note:: Templates are available only for the regions listed below.

   |region-us-east-1|

   .. list-table:: 
   
      * - `SingleInstance.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance.template>`_ 
        - `LoadBalanced.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced.template>`_ 

   |region-us-west-2|
   
   .. list-table:: 
   
      * - `SingleInstance-us-west-2.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-us-west-2.template>`_ 
        - `LoadBalanced-us-west-2.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-us-west-2.template>`_ 
   
   |region-us-west-1| 
   
   .. list-table:: 
   
      * - `SingleInstance-us-west-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-us-west-1.template>`_ 
        - `LoadBalanced-us-west-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-us-west-1.template>`_ 
   
   |region-eu-west-1| 
   
   .. list-table:: 
   
      * - `SingleInstance-eu-west-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-eu-west-1.template>`_ 
        - `LoadBalanced-eu-west-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-eu-west-1.template>`_ 
   
   |region-ap-southeast-1|
   
   .. list-table:: 
   
      * - `SingleInstance-ap-southeast-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-ap-southeast-1.template>`_ 
        - `LoadBalanced-ap-southeast-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-ap-southeast-1.template>`_ 
   
   |region-ap-northeast-1|
   
   .. list-table:: 
   
      * - `SingleInstance-ap-northeast-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-ap-northeast-1.template>`_ 
        - `LoadBalanced-ap-northeast-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-ap-northeast-1.template>`_ 
   
   |region-ap-southeast-2|
   
   .. list-table:: 
   
      * - `SingleInstance-ap-southeast-2.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-ap-southeast-2.template>`_ 
        - `LoadBalanced-ap-southeast-2.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-ap-southeast-2.template>`_ 
   
   |region-sa-east-1|
   
   .. list-table:: 
     
      * - `SingleInstance-sa-east-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-sa-east-1.template>`_ 
        - `LoadBalanced-sa-east-1.template <http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/LoadBalanced-sa-east-1.template>`_ 

        
If you need to create your own links to the templates, the format for each link is as follows:

.. code-block:: none

   http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/{template-name}

For example, for the single instance template for the |region-us-west-1| region, the link would be:

.. code-block:: none

   http://vstoolkit.amazonwebservices.com/CloudFormationTemplates/SingleInstance-us-west-1.template

The links in the table show the HTTP protocol. The HTTPS protocol is also supported.

2. Edit the template to modify it for your specific needs. The templates are text files, so you can
   edit them with any standard text editor. The deployment information in the templates is
   represented in |JSONlong|_ format. After editing the file, it's wise to
   revalidate the JSON formatting using a tool such as `JSONLint <http://jsonlint.com/>`_.
 
   The template file has three sections: :cf-dg:`Parameters <parameters-section-structure>`,
   :cf-dg:`Resources <resources-section-structure>`, and :cf-dg:`Outputs <outputs-section-structure>`.
 
   To add resources to your deployment, add them to the :code:`Resources` section of the template.
   For example, you could add an |RDS|_ database or an |SNS|_ topic. To configure these
   resources at deployment time, add parameters to the :code:`Parameters` section of the template.
   When you add new parameters to the template, the AWS Toolkit adds them to the parameters that
   are displayed in the deployment wizard. You can specify values for these parameters either in
   the deployment wizard or in the config file for the standalone deployment tool.
 
   Similarly, data that you specify in the :code:`Output` section of the template is also displayed
   in the deployment wizard |mdash| as well as in the AWS Management Console. You can use the
   :code:`Output` section to display post-deployment information about your resources. For example,
   if you add an Amazon S3 bucket to the :code:`Resources` section of the template, you can use the
   :code:`Outputs` section to display the autogenerated name for the bucket.
 
   For more information about editing AWS CloudFormation templates, go to the 
   :cf-dg:`CloudFormation User Guide <template-guide>`.

3. Set the :code:`Template` parameter in the deployment configuration file to the path to your
   customized template. The :code:`Template` parameter is located under :code:`General Settings` in
   the config file. The path that you specify could be the path to the file on your local hard
   drive or it could be a URL that points to the location of the configuration file on a remote
   server. When you next run a deployment, the tool will use your template.

Required Data in the Template File
----------------------------------

The deployment process requires that certain data be specified in the template file. While editing
your version of the template, you must ensure that it continues to provide this data. The required
data is located only in the :code:`Parameters` and :code:`Outputs` sections of the template.


Parameters Section of Template
==============================

The following table shows the required parameters in the :cf-dg:`Parameters <parameters-section-structure>` 
section of the template.

.. list-table:: 
    :header-rows: 1 

    * -  Name 
      -  Meaning 

    * - InstanceType 
      - The "API name" for the type of the Amazon EC2 instances to use for the deployment. Examples 
        are t1.micro for Micro   instances or m1.xlarge for Extra Large instances. For a list of 
        instance types and corresponding API names, see the Amazon EC2 
        `detail page <ec2-instance-types_>`_. 
      
    * - KeyPair 
      - Which of your key pairs to use for the Amazon EC2 instances. 

    * - Security Group 
      - The security group to use for the Amazon EC2 instances. 

    * - BucketName 
      - Amazon S3 bucket where the deployment files are uploaded. 

    * - ConfigFile 
      - Name of the config file that the deployment uses. 
      
    * - AmazonMachineImage 
      - The Amazon Machine Image (AMI) that is used for the deployment. For more information about 
        how to create a custom AMI, go to :eb-dg:`Using Custom AMIs <using-features.customami>` in 
        the Elastic Beanstalk Developer Guide and :ref:`tkv-create-ami-from-instance`. Note that the 
        Host Manager software that is installed on AMIs that are used in CloudFormation deployments 
        is now auto-updating. Therefore, if you derive a custom AMI from one of the CloudFormation 
        AMIs, you do not need to maintain the Host Manager software. However, you still need to keep 
        the operating system and application software up to date. 

    * - UserData 
      - The user data that the deployment provides to the deployed application. 


Outputs Section of Template
===========================

The following table shows the required outputs in the :cf-dg:`Outputs <outputs-section-structure>` 
section of the template.

.. list-table:: 
    :header-rows: 1

    * - Name 
      - Meaning 

    * - Bucket 
      - The Amazon S3 bucket to which the deployment files were uploaded. 

    * - ConfigFile 
      - The name of the configuration file that was used for the deployment. 

    * - VSToolkitDeployed 
      - Boolean flag set to :code:`true`, which indicates that this stack was created as part of a 
        deployment from the AWS   Toolkit for Visual Studio. This flag is also set to :code:`true` 
        if the deployment is done from the standalone deployment tool. 

    * - URL 
      - The URL for the deployed application. 
