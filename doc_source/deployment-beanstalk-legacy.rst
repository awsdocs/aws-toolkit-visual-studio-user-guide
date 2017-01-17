.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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

.. note:: The information in this section refers to the :guilabel:`Publish to Amazon Web Services` 
   wizard, which has been replaced by the :guilabel:`Publish to Elastic Beanstalk` wizard. The 
   following information is provided for those who prefer to, or must, use the legacy wizard.

   For information about using the :guilabel:`Publish to Elastic Beanstalk` wizard, see
   :ref:`tkv-deploy-beanstalk`.

|AEBlong| is a service that simplifies the process of provisioning AWS resources for your
application. |EB| provides all of the AWS infrastructure required to deploy your application. This
infrastructure includes:

* |EC2| instances that host the executables and content for your application.

* An |AS| group to maintain the appropriate number of |EC2| instances to support your application.

* An |ELB| load balancer that routes incoming traffic to the |EC2| instance with the most bandwidth.

For more information about |EB|, go to the :eb-dg:`Elastic Beanstalk documentation <Welcome>`.

.. _tkv-deploy-beanstalk-legacy-howto:

How to Deploy a Web Application Using |EB| (Legacy)
===================================================

This section describes how to use the legacy :guilabel:`Publish to Amazon Web Services` wizard,
provided as part of the |TVS|, to deploy a web application through |EB|. To practice, you can
use an instance of a web application starter project that is built in to Visual Studio or you can
use your own project.

.. note:: Before you can use the legacy :guilabel:`Publish to Amazon Web Services` wizard, you must 
   download and install `Web Deploy <http://www.microsoft.com/en-us/download/details.aspx?id=39277>`_. 
   The wizard relies on Web Deploy to deploy web applications and websites to Internet Information 
   Services (IIS) web servers.


To deploy an application by using the legacy Publish to Amazon Web Services wizard
----------------------------------------------------------------------------------

.. note:: If you don't have a project ready to deploy, follow the steps in :ref:`tkv-starter-project` 
   and then follow the steps below.

1. Specify the AWS security credentials for the web application. For instructions, see 
   :ref:`tkv-deploy-specify-credentials-for-application`.

   These credentials might be different from the credentials you use to do the deployment. The
   credentials for the deployment are specified in the deployment wizard described later.

2. In Solution Explorer, open the context (right-click) menu for the :guilabel:`AEBWebAppDemo` project
   folder or for the project folder for your own application, and choose :guilabel:`Publish to
   AWS`.

   .. figure:: images/tkv-publish-to-aws-console.png
      :scale: 85

3. On the :guilabel:`Publish to AWS Elastic Beanstalk` page, choose :guilabel:`Use legacy wizard`.

   .. figure:: images/tkv-use-legacy-wizard-console.png
      :scale: 85

4. On the :guilabel:`Template` page of the wizard, choose the AWS account you want to use for the
   deployment. To add a new account, choose the button with the plus sign (+).

   There are options to perform an initial deployment of an application or redeploy a previously
   deployed application. Previous deployments may have been performed with either the deployment
   wizard or the :ref:`tkv-deployment-tool`. If you choose a redeployment, there may be a delay
   while the wizard retrieves information from previous deployments that are currently running.

   For this example, choose :guilabel:`Deploy new application with template`, choose :guilabel:`AWS
   Elastic Beanstalk`, and then choose :guilabel:`Next`.

   .. figure:: images/tkv-cloudform-aeb-template-dlg.png
      :scale: 85

5. On the :guilabel:`Application` page, the Toolkit has already provided a default name for the
   application. You can change the default name. You can also provide an optional description in
   the :guilabel:`Application Details` area.

   The Toolkit also provides a deployment version label, which is based on the current date and
   time. You can change this version label, but the Toolkit checks it for uniqueness.

   If you are using incremental deployment, :guilabel:`Deployment version label` is unavailable.
   For incremental deployments, the version label is formed from the Git commit ID. In this case,
   the version label is unique because the commit ID is derived from a SHA-1 cryptographic hash.

   With incremental deployment, the first time that you deploy your application, all application
   files are copied to the server. If you later update some of your application files and redeploy,
   only the changed files are copied, which potentially reduces the amount of time required for
   redeployment. Without incremental deployment, all of your application files, whether they were
   changed or not, are copied to the server with each redeployment.

   Select :guilabel:`Deploy application incrementally` and then choose :guilabel:`Next`.

   .. figure:: images/tkv-aeb-application-dlg.png
      :scale: 85

6. On the :guilabel:`Environment` page, type a name and description for your |EB| environment. In this
   context, *environment* refers to the infrastructure |EB| provisions for your application. The
   Toolkit has already provided a default name, which you can change. The environment name cannot
   be longer than 23 characters. In :guilabel:`Description`, type any text you choose.

   You can also provide a subdomain of :code:`.elasticbeanstalk.com` that will be the URL for your
   application. The Toolkit provides a default subdomain based on the environment name.

7. Choose :guilabel:`Check availability` to make sure the URL for your web application is okay to use.

8. Choose :guilabel:`Next`.

   .. figure:: images/tkv-aeb-environment-dlg.png
      :scale: 85

9. On the :guilabel:`AWS Options` page, configure the following.

   * From the :guilabel:`Container type` drop-down list, choose a container type. The container type
     specifies an Amazon Machine Image (AMI) for your application and configurations for the |AS|
     group, the load balancer, and other aspects of the environment in which your application
     will run.

   * Optional. In the :guilabel:`Use custom AMI` field, you can specify a custom AMI. If you specify a
     custom AMI, it will override the AMI in :guilabel:`Container type`. For more information
     about how to create a custom AMI go to :eb-dg:`Using Custom AMIs <using-features.customami>` 
     in the |EB-dg|_ and :ref:`tkv-create-ami-from-instance`.

   * From the :guilabel:`Instance Type` drop-down list, choose an |EC2| instance type. For this
     application, we recommend you use :guilabel:`Micro` because this will minimize the cost
     associated with running the instance. For more information about |EC2| costs, go to the
     |ec2-pricing|_ page.

   * From the :guilabel:`Key pair` drop-down list, choose a key pair.

   * The :guilabel:`IAM Role` drop-down list displays the roles available for your |EB| environment. If
     you do not have an |IAM| role, you can choose :guilabel:`Use the default role` from the
     list. In this case, |EB| creates a default |IAM| role and updates the |S3| bucket policy to
     allow log rotation.

     An |IAM| role provides applications and services access to AWS resources using temporary
     security credentials. For example, if your application requires access to |DDB|, it must use
     AWS security credentials to make an API request. The application can use these temporary
     security credentials so you do not have to store long-term credentials on an |EC2| instance
     or update the instance every time the credentials are rotated. |EB| requires an |IAM| role
     to rotate logs to |S3|.

     If you choose not to use the |IAM| role, you need to grant permissions for |EB| to rotate
     logs. For instructions, see 
     :eb-dg-deep:`Using a Custom Instance Profile <AWSHowTo.iam.roles.logs.html#AWSHowTo.iam.roles.logs-custom>`. 
     For more information about log rotation, see :eb-dg:`Configuring Containers with Elastic Beanstalk 
     <using-features.managing.container>` For more information about using |IAM| roles
     with |EB|, see :eb-dg:`Using IAM Roles with Elastic Beanstalk <AWSHowTo.iam.roles.aeb>`.

     The credentials you use for deployment must have permission to create the default |IAM| 
     role.

     Choose :guilabel:`Next`.

     .. figure:: images/tkv-aeb-aws-options.png
        :scale: 85

10. The :guilabel:`VPC Options` page provides the option to launch your application to a VPC. The VPC
    must have already been created. You can use the |TVS| or the 
    :eb-dg:`AWS Management Console <AWSHowTo-vpc-basic>` to create a VPC. If you created the VPC in 
    the Toolkit, the Toolkit will populate this page for you. If you created the VPC in the console, 
    type information about your VPC into this page.

.. _tkv-deploy-beanstalk-legacy-considerations:

Key considerations for deployment to a VPC
==========================================

    * Your VPC needs at least one public and one private subnet.

    * In the *ELB Subnet* drop-down list, specify the public subnet. The |TVS| deploys the |ELB| load
      balancer for your application to the public subnet. The public subnet is associated with a
      :console:`routing table <vpc>` that has an entry that points to an Internet
      gateway. You can recognize an Internet gateway because it has an ID that begins with
      :code:`igw-`(for example, :code:`igw-83cddaea`). Public subnets that you create by using the
      Toolkit have tag values that identify them as public.
    
    * In the *Instances Subnet* drop-down list, specify the private subnet. The Toolkit deploys the |EC2|
      instances for your application to the private subnet.
    
    * The |EC2| instances for your application communicate from the private subnet to the Internet 
      through an |EC2| instance in the public subnet that performs network address translation (NAT). 
      To enable this communication, you will need a :console:`VPC security group <vpc>` that allows 
      traffic to flow from the private subnet to the NAT instance. Specify this VPC security group 
      in the *Security Group* drop-down list.

    For more information about how to deploy an |EB| application to a VPC, go to the |EB-dg|_.

    .. figure:: images/tkv-aeb-aws-options-vpc.png
       :scale: 100
    
11. On the :guilabel:`Application Options` page, configure the following.

    * Under :guilabel:`Application Pool Options`, in the :guilabel:`Target framework` drop-down list,
      choose the version of the .NET Framework required by your application (for example, .NET
      Framework 2.0, .NET Framework 3.0, .NET Framework 3.5, .NET Framework 4.0, .NET Framework
      4.5).

      For this walkthrough, select :guilabel:`Enable 32-bit applications`.

    * Under :guilabel:`Miscellaneous`, in the :guilabel:`Application health-check URL` box, type a URL for
      |EB| to check to determine if your application is still responsive. This URL is relative to
      the root server URL. For example, if the full URL is , you would type
      :code:`/site-is-up.html`. For this sample application, leave the default setting of a
      forward slash (:code:`/`).

    * In :guilabel:`Application Environment`, use the parameter fields (PARAM1-5) to provide input data to
      your application. These values are made available to the deployed application through the
      :code:`appSettings` element in the :code:`Web.config` file. For more information, go to the
      `Microsoft MSDN library <http://msdn.microsoft.com/en-us/library/610xe886.aspx>`_.

    * In :guilabel:`Application Credentials`, choose the AWS credentials under which the application
      should run. These could be different from the credentials used to deploy to |EB|.

      * To use a different set of credentials, choose :guilabel:`Use these credentials` and type the access
        key and secret key in the fields provided.

      * To use the same credentials as those used to deploy to |EB|, choose :guilabel:`Use credentials from
        profile '<account name>'` where {<account name>} is the account selected on the first
        page of the wizard.

      * To use the credentials for an |IAMlong| (|IAM|) user, choose :guilabel:`Use an IAM user` and then
        specify the user.
  
        To use an |IAM| user, you must have:
  
        * created the |IAM| user in the |TVS|.
  
        * stored the secret key for the user with the |TVS|.
  
        For more information, see :ref:`tkv-create-an-iam-user` and
        :ref:`generate-credentials-for-an-iam-user-tkv`.
  
        An |IAM| user could have more than one set of credentials stored with the Toolkit. If
        that is the case, you will need to choose the credentials to use. The root account could
        rotate the credentials for the |IAM| user, which would invalidate the credentials. In
        this scenario, you would need to redeploy the application and then manually enter new
        credentials for the |IAM| user.

    Choose :guilabel:`Next`.

    .. figure:: images/tkv-cloudform-pub-creds.png
       :scale: 85

       :guilabel:`Application Options` page

12. If you have deployed |RDS| instances, a page similar to the following will appear as part of the
    deployment wizard. You can use this page to add the |EC2| instances for your deployment to one
    or more of the |RDS| security groups associated with your RDS instances. If your application
    needs to access your RDS instances, you will need to enable this access here or by setting the
    permissions on your RDS security groups. For more information, see
    :ref:`tkv-amazon-rds-security-groups`.

    If you are deploying to a VPC, this page will not appear because for VPCs, RDS instances are
    managed by |EC2| security groups.

    .. figure:: images/tkv-aeb-rds-sg.png
       :scale: 85

13. On the :guilabel:`Review` page, review the options you configured earlier, and select
    :guilabel:`Open environment status window when wizard closes`.

    If everything looks correct, choose :guilabel:`Deploy`.

    .. note:: When you deploy the application, the active account will incur charges for the AWS 
       resources used by the application.

    You can save the deployment configuration to a text file to use with standalone deployment tool.
    To save the configuration, select :guilabel:`Generate AWSDeploy configuration`. Choose
    :guilabel:`Choose File` and then specify a file to which to save the configuration. You can also
    save the deployment configuration after the deployment is complete. In AWS Explorer, open the
    context (right-click) menu for the deployment and choose :guilabel:`Save Configuration`.

    .. note:: When you deploy the application, the active account will incur charges for the AWS 
       resources used by the application. 

    .. figure:: images/tkv-aeb-review-dlg.png
       :scale: 85

       :guilabel:`Review` page

14. A status page for the deployment will open. The deployment may take a few minutes.

    When the deployment is complete, the Toolkit will display an alert. This is useful because it
    allows you to focus on other tasks while the deployment is in progress.

    .. figure:: images/tkv-aeb-launch-toast.png
       :scale: 85

    Choose the :guilabel:`Application URL` link to connect to the application.

15. To delete the deployment, in AWS Explorer, expand the :guilabel:`Elastic Beanstalk` node, open the
    context (right-click) menu for the subnode for the deployment, and choose :guilabel:`Delete`.
    |EB| will begin the deletion process, which might take a few minutes. If you specified a
    notification email address in the deployment, |EB| will send status notifications to this
    address.

.. _tkv-starter-project:

To create a sample web application starter project
--------------------------------------------------

Follow these steps to create a sample application if you do not have a project ready to deploy. 

1. In Visual Studio, from the :guilabel:`File` menu, choose :guilabel:`New`, and then choose
   :guilabel:`Project`.

2. In the :guilabel:`New Project` dialog box, in the navigation pane, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of available web project templates, choose any template containing the words :code:`Web`
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
      :scale: 100
      
Return to :ref:`tkv-deploy-beanstalk-legacy-howto` and complete your deployment.


