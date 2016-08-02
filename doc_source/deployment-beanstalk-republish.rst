.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-republish-application:

#########################################################
How to Republish Your Application to an |EB| Environment
#########################################################

You can iterate on your application by making discrete changes and then republishing a new version
to your already launched |EB| environment.

1. In Solution Explorer, open the context (right-click) menu for the project node and then choose 
   :guilabel:`Republish to Environment '<environment_name>'`.

   .. figure:: images/tkv-republish-to-aws-console.png
        :scale: 100

2. On the page that appears, choose :guilabel:`Deploy`. The new version of your application will be
   published to the current environment.

When you republish, you do not have the option to use a new or different environment. If you need to
change any aspect of your deployment other than the options offered on the settings page, you must
choose :guilabel:`Publish to AWS` (instead of :guilabel:`Republish to Environment 
'<environment_name>'`) in step 1 and use the deployment wizard to make changes.

You cannot republish if your application is in the process of launching or terminating.