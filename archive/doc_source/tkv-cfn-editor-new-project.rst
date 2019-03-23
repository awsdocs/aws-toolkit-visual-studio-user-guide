.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-cfn-editor-new-project:

###################################################
Creating a |CFN| Template Project in Visual Studio
###################################################

.. meta::
   :description: Create a CloudFormation template project using the Tookit for Visual Studio.
   :keywords: template project, CloudFormation


**To create a template project**

1. In Visual Studio, choose :guilabel:`File`, choose :guilabel:`New`, and then choose
   :guilabel:`Project`.

2. In the :guilabel:`New Project` dialog box, choose :guilabel:`Installed`, choose
   :guilabel:`AWS`, and then choose :guilabel:`AWS Cloud Formation Project`.

   .. figure:: images/vs-editor-new-template-2.png
      :scale: 85

3. In :guilabel:`Name`, type the name of your template project.

4. On the :guilabel:`Select Project Source` page, choose the source of the template you will create:

   * :guilabel:`Create with empty template` generates a new, empty |CFN| template.

   * :guilabel:`Create from existing AWS |CFN| stack` generates a template from an existing stack in your 
     AWS account. (The stack doesn't need to have a status of :code:`CREATE_COMPLETE`.)

   * :guilabel:`Select sample template` generates a template from one of the |CFN| sample templates.

   .. figure:: images/vs-editor-new-template-empty-2.png
      :scale: 85

5. To complete the creation of your |CFN| template project, choose :guilabel:`Finish`.
