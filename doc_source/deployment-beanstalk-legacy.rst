.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-legacy:

###########################
Deploying to |EB| (Legacy)
###########################

.. note:: The information in this section refers to the :guilabel:`Publish to Amazon Web Services` wizard,
   which has been replaced by the :guilabel:`Publish to Elastic Beanstalk` wizard. The following
   information is provided for those who prefer to, or must, use the legacy wizard.

   For information about using the :guilabel:`Publish to Elastic Beanstalk` wizard, see
   :ref:`tkv-deploy-beanstalk`.

|AEBlong| is a service that simplifies the process of provisioning AWS resources for your
application. |EB| provides all of the AWS infrastructure required to deploy your application. This
infrastructure includes:

* |EC2| instances that host the executables and content for your application.

* An |AS| group to maintain the appropriate number of |EC2| instances to support your application.

* An |ELB| load balancer that routes incoming traffic to the |EC2| instance with the most bandwidth.

For more information about |EB|, go to the :eb-dg:`Elastic Beanstalk documentation <Welcome>`.

.. toctree::
    :titlesonly:
    :maxdepth: 1

    deployment-beanstalk-legacy-howto




