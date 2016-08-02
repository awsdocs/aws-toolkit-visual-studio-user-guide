.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-cfn-editor-new-project:

###################################################
Creating an |CFN| Template Project in Visual Studio
###################################################

**To create an CFN template project**

1. In Visual Studio, choose :guilabel:`File`, choose :guilabel:`New`, and then choose
   :guilabel:`Project`.

2. In the :guilabel:`New Project` dialog box, choose :guilabel:`Installed Templates`, choose
   :guilabel:`CFN`, and then choose :guilabel:`CFN Template`.

  .. figure:: images/vs-editor-new-template.png
      :scale: 85

3. In :guilabel:`Name`, type the name of your template project.

4. In the :guilabel:`Solution` drop-down list, choose one of the following:

  * :guilabel:`Create new solution`. To create a new solution for your template, type a name for the
    solution in :guilabel:`Solution Name`. (Optional) Choose a location for your project in
    :guilabel:`Location`.
  
    .. figure:: images/vs-editor-new-template-lp-new.png
       :scale: 85

  * :guilabel:`Add to solution`. If you choose to add this template to your currently open solution, 
    the :guilabel:`Location` field will be set to the location of your current solution
    automatically, and the :guilabel:`Solution Name` field will be unavailable.

    .. figure:: images/vs-editor-new-template-lp-add.png
       :scale: 85

5. Choose :guilabel:`OK`.

6. On the :guilabel:`Select Project Source` page, choose the source of the template you will create:

   * :guilabel:`Create with empty template` generates a new, empty |CFN| template.

   * :guilabel:`Create from existing CFN stack` generates a template from an existing stack in your 
     AWS account. (The stack doesn't need to have a status of :code:`CREATE_COMPLETE`.)

   * :guilabel:`Select sample template` generates a template from one of the |CFN| sample templates.

   .. figure:: images/vs-editor-new-template-empty.png
      :scale: 85

7. To complete the creation of your |CFN| template project, choose :guilabel:`Finish`.
