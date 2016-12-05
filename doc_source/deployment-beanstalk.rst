.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk:

####################################################
Deploying to |EB|
####################################################


.. meta::
   :description: Deploying to Elastic Beanstalk using the Toolkit for Visual Studio.
   :keywords: deployment, Elastic Beanstalk

|AEBlong| is a service that simplifies the process of provisioning AWS resources for your
application. |EB| provides all of the AWS infrastructure required to deploy your application. This
infrastructure includes:

* |EC2| instances that host the executables and content for your application.

* An |AS| group to maintain the appropriate number of |EC2| instances to support your application.

* An |ELB| load balancer that routes incoming traffic to the |EC2| instance with the most bandwidth.

The |TVS| provides a wizard that simplifies publishing applications through |EB|. This wizard
is described in the following sections.

For more information about |EB|, go to the :eb-dg:`Elastic Beanstalk documentation <Welcome>`.


.. toctree::
    :titlesonly:
    :maxdepth: 1

    Deploy an ASP.NET App (Traditional) <deployment-beanstalk-traditional>
    Deploy an ASP.NET App (.NET Core) <deployment-beanstalk-netcore>
    Specify AWS Credentials <deployment-beanstalk-specify-credentials>
    Republish to Elastic Beanstalk <deployment-beanstalk-republish>
    Custom Deployments (Traditional) <deployment-beanstalk-custom>
    Custom Deployments (.NET Core) <deployment-beanstalk-custom-netcore>
    Multiple Application Support <deployment-beanstalk-multiple-application>
    Publish to AWS Wizard (Legacy) <deployment-beanstalk-legacy>
    deployment-cloudform
