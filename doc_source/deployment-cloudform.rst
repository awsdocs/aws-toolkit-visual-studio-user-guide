.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-cloudform:

###########################
Deploying to |CFN| (Legacy)
###########################

.. note:: The information in this topic refers to the :guilabel:`Publish to Amazon Web Services` 
   wizard, which has been replaced by deploying through |EB| through the use of the 
   :guilabel:`Publish to Elastic Beanstalk` wizard. The following information is provided for those 
   who prefer to, or must, use the legacy wizard to deploy through |CFN|.

   For information about using the preferred :guilabel:`Publish to Elastic Beanstalk` wizard, see
   :ref:`tkv-deploy-beanstalk`.

|CFN| is a service that simplifies the process of provisioning AWS resources for your application.
The AWS resources are described in a template file. The |CFN| service consumes this template and
automatically provisions the required resources for you. For more information, go to |CFN|_.

We'll deploy an application to AWS and use |CFN| to provision the resources for the application. To
practice, you can use an instance of a web application starter project that is built in to Visual
Studio or you can use your own project.

To create a sample web application starter project
--------------------------------------------------

Follow these steps if you do not have project ready to deploy.

1. In Visual Studio, from the :guilabel:`File` menu, choose :guilabel:`New`, and then choose 
   :guilabel:`Project`.

2. In the navigation pane of the :guilabel:`New Project` dialog box, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of available web project templates, select any template containing the words :code:`Web`
   and :code:`Application` in its description. For this example, choose :guilabel:`ASP.NET Web
   Forms Application`.

   .. figure:: images/tkv-new-web-project-console.png
      :scale: 85

4. In the :guilabel:`Name` box, type :code:`AEBWebAppDemo`.

5. In the :guilabel:`Location` box, type the path to a solution folder on your development machine or
   choose :guilabel:`Browse`, and then browse to and choose a solution folder, and choose
   :guilabel:`Select Folder`.

6. Confirm the :guilabel:`Create directory for solution` box is selected. In the :guilabel:`Solution`
   drop-down list, confirm :guilabel:`Create new solution` is selected, and then choose
   :guilabel:`OK`. Visual Studio will create a solution and project based on the ASP.NET Web Forms
   Application project template.
 
   .. figure:: images/tkv-web-app-solution-explorer-console.png
      :scale: 85


To deploy an application by using the legacy Publish to Amazon Web Services wizard
----------------------------------------------------------------------------------

1. In Solution Explorer, open the context (right-click) menu for the :guilabel:`AEBWebAppDemo` project
   folder (or your own project folder), and then choose :guilabel:`Publish to AWS`.

   .. figure:: images/tkv-publish-to-aws-console.png
      :scale: 85

2. On the :guilabel:`Publish to AWS Elastic Beanstalk` page, choose :guilabel:`Use legacy wizard`.

   .. figure:: images/tkv-use-legacy-wizard-console.png
      :scale: 85


3. On the :guilabel:`Template` page of the wizard, choose the profile you will use for the deployment.
   To add a new profile, choose :guilabel:`Other`. For more information about profiles, see 
   :ref:`creds`.

4. There are options to deploy a new application or redeploy an application that was deployed
   previously through either the deployment wizard or the standalone deployment tool. If you choose
   a redeployment, there may be a delay while the wizard retrieves information from the previous
   deployment.

   The :guilabel:`Load Balanced Template` and :guilabel:`Single Instance Template` are included
   with the |TVS|. :guilabel:`Load Balanced Template` provisions an |EC2| instance with an |ELB|
   load balancer and an |AS| group. :guilabel:`Single Instance Template` provisions just a single
   |EC2| instance.

   For this example, choose :guilabel:`Load Balanced Template`, and then choose :guilabel:`Next`.

    .. figure:: images/tkv-cloudform-pub-dlg.png
       :scale: 85

5. On the :guilabel:`AWS Options` page, configure the following:

   * From the :guilabel:`Key pair` drop-down list, choose an |EC2| key pair.

   * Leave :guilabel:`SNS Topic` blank. If you specify an SNS topic, |CFN| will send status notifications
     during the deployment.

   * Leave the :guilabel:`Custom AMI` field blank. The |CFN| template includes an AMI.

   * From the :guilabel:`Instance type` drop-down list, leave the default set to :guilabel:`Micro`. This
     will minimize the cost associated with running the instance. For more information about
     |EC2| costs, go to the |ec2-pricing|_ page.

   * From the :guilabel:`Security group` drop-down list, choose a security group that has port 80 open.
     If you have already configured a security group with port 80 open, then choose it. The
     :guilabel:`default` selection in this drop-down list does not have port 80 open.

     Applications deployed to |CFN| must have port 80 open because |CFN| uses this port to relay
     information about the deployment. If the security group you choose does not have port 80
     open, the wizard will ask if it should open it. If you say yes, port 80 will be open for any
     |EC2| instances that use that security group. For more information about creating a security
     group, see :ref:`tkv-sg-create`.

   Choose :guilabel:`Next`.

   .. figure:: images/tkv-cloudform-pub-options.png
      :scale: 85

6. On the :guilabel:`Application Options` page, in the :guilabel:`Application Credentials` section,
   choose the profile under which the application (in this example, :code:`PetBoard`) should run.
   It could be different from the profile used to deploy to |CFN| (that is, the profile you
   specified on the first page of the wizard).

   To use a different set of credentials, choose :guilabel:`Use these credentials` and then type
   the access key and secret key in the fields provided.

   To use the same credentials, choose :guilabel:`Use credentials from profile profile_name` where
   {profile_name} is the profile you specified on the first page of the wizard.

   To use the credentials for an |IAMlong| (IAM) user, choose :guilabel:`Use an IAM user`, and then
   specify the user.

   To use an IAM user, you must have:

   * created the IAM user in the |TVS|.

   * stored the secret key for the user with the |TVS|.

   For more information, see :ref:`tkv-create-an-iam-user` and
   :ref:`generate-credentials-for-an-iam-user-tkv`.

   An IAM user could have more than one set of credentials stored with the Toolkit. If that is the
   case, you will need to choose the credentials to use. The root account could rotate the
   credentials for the IAM user, which would invalidate the credentials. In this scenario, you
   would need to redeploy the application and then manually enter new credentials for the IAM user.

   The following table describes other options available on the :guilabel:`Application Options`
   page. For :code:`PetBoard`, you can leave the defaults.

   .. list-table::
      :header-rows: 1
   
      * - Key and Value
        - Description
        
      * - PARAM1, PARAM2, PARAM3, PARAM4, PARAM5 
        - These values are made available to the deployed application through the :code:`appSettings` 
          element in the Web.config file. For more information, go to the Microsoft 
          `MSDN library <http://msdn.microsoft.com/en-us/library/610xe886.aspx>`_. 
        
      * - Target framework 
        - Specifies the version of the .NET Framework targeted by the application. Possible values are: 
          .NET Framework 2.0, .NET Framework 3.0, .NET Framework 3.5, .NET Framework 4.0, .NET Framework 4.5 
        
      * - Enable 32-bit applications 
        - Select if the application is 32-bit. Otherwise, leave the box cleared. 
        
      * - Application health check URL 
        - This URL is relative to the root server URL. For example, if the full path to the URL is 
          :code:`example.com/site-is-up.html`, you would type :code:`/site-is-up.html`. This setting 
          applies only when you use the Load Balanced template. It is ignored when you use the Single 
          Instance template. 

     
   Choose :guilabel:`Finish`.

   .. figure:: images/tkv-cloudform-pub-creds.png
      :scale: 85

7. On the :guilabel:`Review` page, select :guilabel:`Open environment status window when wizard
   closes`.

   You can save the deployment configuration to a text file to use with standalone deployment tool.
   To save the configuration, select :guilabel:`Generate AWSDeploy configuration`. Choose
   :guilabel:`Choose File` and then specify a file to which to save the configuration. You can also
   save the deployment configuration after the deployment is complete. In AWS Explorer, open the
   context (right-click) menu for the deployment and choose :guilabel:`Save Configuration`.

   .. note:: Because the deployment configuration includes the credentials that were used for 
      deployment, you should keep the configuration file in a secure location.

   Choose :guilabel:`Deploy`.

   .. note:: When you deploy the application, the active account will incur charges for the AWS 
      resources used by the application.

   .. figure:: images/tkv-cloudform-review-dlg.png
      :scale: 85

8. A status page for the deployment will open. The deployment may take a few minutes.

   When the deployment is complete, the Toolkit will display an alert. This is useful because it
   allows you to focus on other tasks while the deployment is in progress.

   When the deployment is complete, the status displayed in the |TVS| will be
   :guilabel:`CREATE_COMPLETE`.

   .. figure:: images/tkv-cloudform-complete-click-link.png
      :scale: 65

   Choose the :guilabel:`Application URL` link to connect to the application.

9. To delete the deployment, in AWS Explorer, expand the :guilabel:`CloudFormation` node and open the
   context (right-click) menu for the subnode for the deployment and choose :guilabel:`Delete`.
   |CFN| will begin the deletion process, which might take a few minutes. If you specified an SNS
   topic for the deployment, |CFN| will send status notifications to this topic.


