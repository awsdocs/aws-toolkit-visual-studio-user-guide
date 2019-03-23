.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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

.. meta::
   :description: How to republish apps to Elastic Beanstalk.
   :keywords: republish, Elastic Beanstalk

You can iterate on your application by making discrete changes and then republishing a new version
to your already launched |EB| environment. 

1. In Solution Explorer, open the context (right-click) menu for the :guilabel:`AEBWebAppDemo` project 
   folder for the project you published in the previous section, and choose :guilabel:`Publish to AWS Elastic Beanstalk`.   

   .. figure:: images/tkv-publish-to-aws-console.png
       :scale: 85
       
   The :guilabel:`Publish to Elastic Beanstalk` wizard appears.

   .. figure:: images/tkv-aeb-wizard-app-console2.png
       :scale: 85
       
2. Select :guilabel:`Redeploy to an existing environment` and choose the environment you previously 
   published to. Click :guilabel:`Next`.

   The :guilabel:`Review` wizard appears.

   .. figure:: images/tkv-aeb-wizard-app-review.png
       :scale: 85

3.  Click :guilabel:`Deploy`.  The application will redploy to the same environment.

You cannot republish if your application is in the process of launching or terminating.


