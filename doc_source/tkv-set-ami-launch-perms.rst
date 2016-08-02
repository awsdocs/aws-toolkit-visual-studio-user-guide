.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-set-launch-permissions-on-ami:

#####################################################
Setting Launch Permissions on an Amazon Machine Image
#####################################################

You can set launch permissions on your Amazon Machine Images (AMIs) from the :guilabel:`AMIs` view
in AWS Explorer. You can use the :guilabel:`Set AMI Permissions` dialog box to copy permissions from
AMIs.

*To set permissions on an AMI*

1. In the :guilabel:`AMIs` view in AWS Explorer, open the context (right-click) menu on an AMI, and
   then choose :guilabel:`Edit Permission`.

   .. figure:: images/tkv-ami-edit-permissions-menu.png
       :scale: 85

2. There are three options available in the :guilabel:`Set AMI Permissions` dialog box:

   * To give launch permission, choose :guilabel:`Add`, and type the account number for the AWS user to
     whom you are giving launch permission.

   * To remove launch permission, choose the account number for the AWS user from whom you are removing
     launch permission, and choose :guilabel:`Remove`.

   * To copy permissions from one AMI to another, choose an AMI from the list, and choose :guilabel:`Copy
     from`. The users who have launch permissions on the AMI you chose will be given launch
     permissions on the current AMI. You can repeat this process with other AMIs in the
     :guilabel:`Copy-from` list to copy permissions from multiple AMIs into the target AMI.

     The :guilabel:`Copy-from` list contains only those AMIs owned by the account that was active
     when the :guilabel:`AMIs` view was displayed from AWS Explorer. As a result, the
     :guilabel:`Copy-from` list might not display any AMIs if no other AMIs are owned by the
     active account.

    .. figure:: images/tkv-ami-copy-permissions-dlg.png
        :scale: 85

    :guilabel:`Copy AMI permissions` dialog box


