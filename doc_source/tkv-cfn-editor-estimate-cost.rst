.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-cfn-editor-estimate-cost:

###################################################################
Estimating the Cost of Your |CFN| Template Project in Visual Studio
###################################################################

.. meta::
   :description: Estimate the cost of CloudFormation templates.
   :keywords: cost, CloudFormation, template

With the |TVS|, you can easily estimate the cost of the |CFN| stack you are working on before
you deploy it. This way you'll have an idea of the monthly operating costs for the resources include
in your template.

**To estimate the cost of your CFN stack**

1. In Solution Explorer, open the context (right-click) menu for the template and choose
   :guilabel:`Estimate Cost`.

   Alternatively, to estimate the cost of the template you're currently editing, from the
   :guilabel:`Template` menu, choose :guilabel:`Estimate Cost`.

   .. figure:: images/vs-editor-template-menu-estimate-cost.png
       :scale: 65

2. Provide values for parameters you have defined for your stack, and choose :guilabel:`Finish`.

   .. figure:: images/vs-editor-cfn-estimate-cost.png
       :scale: 65

3. The `AWS Simple Monthly Calculator <http://calculator.s3./calc5.html>`_ will be displayed. The
   values for the form data will be filled in with information pulled from the template you're
   editing. You can adjust the values, if needed.

   The :guilabel:`Estimate of Your Monthly Bill` tab will display an itemized view of the estimated
   monthly costs of running your stack.

   .. figure:: images/vs-editor-simple-monthly-calc.png
       :scale: 85

.. note:: Cost estimates are calculated using the values you provide and the current rates of AWS 
   services, which can vary over time. For more information, see the `How AWS Pricing Works
   <http://bit.ly/aws-pricing>`_ whitepaper.


