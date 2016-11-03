.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-cfn-editor-deploy-template:

############################################
Deploying a |CFN| Template in Visual Studio
############################################

.. meta::
   :description: Deploy a |CFN| template using the |TVS|.
   :keywords: deployment, |CFN|, template

**To deploy an CFN template**

1. In Solution Explorer, open the context (right-click) menu for the template you want to deploy, and
   choose :guilabel:`Deploy to AWS CloudFormation`.

   .. figure:: images/vs-editor-solution-explorer-deploy.png
       :scale: 65

   Alternatively, to deploy the template you're currently editing, from the :guilabel:`Template`
   menu, choose :guilabel:`Deploy to AWS CloudFormation` .

   .. figure:: images/vs-editor-template-menu-deploy.png
        :scale: 65

2. On the :guilabel:`Deploy Template` page, choose the AWS account to use to launch the stack and the
   region where it will be launched.

   .. figure:: images/vs-editor-cfn-deploy.png
       :scale: 65

3. Choose :guilabel:`Create New Stack` and type a name for your stack.

4. Choose any (or none) of the following options:

   * To receive notifications about the stack's progress, from the :guilabel:`SNS Topic` drop-down 
     list, choose an SNS topic. You can also create an SNS topic by choosing 
     :guilabel:`Create New Topic` and typing an email address in the box.

   * Use :guilabel:`Creation Timeout` to specify how long |CFN| should allow for the stack to be 
     created before it is declared failed (and rolled back, unless the 
     :guilabel:`Rollback on failure` option is cleared).

   * Use :guilabel:`Rollback on failure` if you want the stack to roll back (that is, delete itself) 
     on failure. Leave this option cleared if you would like the stack to remain active for
     debugging purposes, even if it has failed to complete the launch.

5. Choose :guilabel:`Finish` to launch the stack.
