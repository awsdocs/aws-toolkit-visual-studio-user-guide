.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deployment:

################################
Deployment Using the AWS Toolkit
################################

.. meta::
   :description: Deployment using the Toolkit for Visual Studio.
   :keywords: deployment, Elastic Beanstalk, CloudFormation

The |TVS| supports application deployment to |AEBlong| containers or |CFN| stacks.

* :ref:`tkv-deploy-beanstalk` describes how to use the Visual Studio IDE to deploy applications to |EB|.

* :ref:`tkv-deployment-tool` describes how to use the standalone deployment tool to deploy to either 
  |EB| containers or |CFN| stacks from a command window.

.. note:: If you are using Visual Studio Express Edition:

    * You can use the :ref:`standalone deployment tool <tkv-deployment-tool>` to deploy applications 
      to |EB| containers.

    * You can use the :eb-dg:`AWS Management Console <using-features.deployment.newapp>` to deploy
      applications to |EB| containers.

    For either approach, you must first create a web deployment package. For more information, see
    `How to: Create a Web Deployment Package in Visual Studio <http://msdn.microsoft.com/en-us/library/dd465323.aspx>`_.


.. toctree::
    :titlesonly:
    :maxdepth: 1

    deployment-beanstalk
    deployment-tool


