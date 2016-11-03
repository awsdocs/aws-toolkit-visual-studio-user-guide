.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-deploy-beanstalk-traditional:

##################################################
Deploy a Traditional ASP.NET Application to |EB|
##################################################


.. meta::
   :description: Deploying traditional ASP.NET apps to Elastic Beanstalk.
   :keywords: deployment, Elastic Beanstalk

This section describes how to use the :guilabel:`Publish to Elastic Beanstalk` wizard, provided as
part of the |TVS|, to deploy an application through |EB|. To practice, you can use an
instance of a web application starter project that is built in to Visual Studio or you can use your
own project.

.. note:: This topic describes using the wizard to deploy traditional ASP.NET applications. The 
   wizard also supports deploying ASP.NET Core applications. For information about ASP.NET Core, 
   see :ref:`tkv-deploy-beanstalk-netcore`.

.. note:: Before you can use the :guilabel:`Publish to Elastic Beanstalk` wizard, you must download and
   install `Web Deploy <http://www.microsoft.com/en-us/download/details.aspx?id=39277>`_. The
   wizard relies on Web Deploy to deploy web applications and websites to Internet Information
   Services (IIS) web servers.


To create a sample web application starter project
==================================================

1. In Visual Studio, from the :guilabel:`File` menu, choose :guilabel:`New`, and then choose
   :guilabel:`Project`.

2. In the navigation pane of the :guilabel:`New Project` dialog box, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of web project templates, choose any template containing the words :code:`Web` and
   :code:`Application` in its description. For this example, choose :guilabel:`ASP.NET Web Forms 
   Application`.

   .. figure:: images/tkv-new-web-project-console.png
       :scale: 85

4. In the :guilabel:`Name` box, type :code:`AEBWebAppDemo`.

5. In the :guilabel:`Location` box, type the path to a solution folder on your development machine or
   choose :guilabel:`Browse`, and then browse to and choose a solution folder, and choose
   :guilabel:`Select Folder`.

6. Confirm the :guilabel:`Create directory for solution` box is selected. In the :guilabel:`Solution` 
   drop-down list, confirm :guilabel:`Create new solution` is selected, and then choose
   :guilabel:`OK`. Visual Studio will create a solution and project based on the ASP.NET Web Forms
   Application project template. Visual Studio will then display Solution Explorer where the new
   solution and project appear.

   .. figure:: images/tkv-web-app-solution-explorer-console.png
       :scale: 85


To deploy an application by using the Publish to Elastic Beanstalk wizard
=========================================================================

1. In Solution Explorer, open the context (right-click) menu for the :guilabel:`AEBWebAppDemo` project
   folder for the project you created in the previous section, or open the context menu for the
   project folder for your own application, and choose :guilabel:`Publish to AWS`.

   .. figure:: images/tkv-publish-to-aws-console.png
       :scale: 85

   The :guilabel:`Publish to Elastic Beanstalk` wizard appears.

   .. figure:: images/tkv-aeb-wizard-app-console.png
       :scale: 85

2. In :guilabel:`Profile`, from the :guilabel:`Account profile to use for deployment` drop-down list,
   choose the AWS account profile you want to use for the deployment.

   Optionally, if you have an AWS account you want to use, but you haven't yet created an AWS
   account profile for it, you can choose the button with the plus symbol (:code:`+`) to add an AWS
   account profile.

3. From the :guilabel:`Region` drop-down list, choose the region to which you want |EB| to deploy the
   application.

4. In :guilabel:`Deployment Target`, you can choose either :guilabel:`Create a new application 
   environment` to perform an initial deployment of an application or :guilabel:`Redeploy to an 
   existing environment` to redeploy a previously deployed application. (The previous deployments
   may have been performed with either the wizard or the :ref:`tkv-deployment-tool`.) If you choose
   :guilabel:`Redeploy to an existing environment`, there may be a delay while the wizard retrieves
   information from previous deployments that are currently running.

   .. note:: If you choose :guilabel:`Redeploy to an existing environment`, choose an environment in the list,
      and then choose :guilabel:`Next`, the wizard will take you directly to the
      :guilabel:`Application Options` page. If you go this route, skip ahead to the instructions
      later in this section that describe how to use the :guilabel:`Application Options` page.

5. Choose :guilabel:`Next`.

   .. figure:: images/tkv-aeb-wizard-env-console.png
       :scale: 85

6. On the :guilabel:`Application Environment` page, in the :guilabel:`Application` area, the
   :guilabel:`Name` drop-down list proposes a default name for the application. You can change the
   default name by choosing a different name from the drop-down list.

7. In the :guilabel:`Environment` area, in the :guilabel:`Name` drop-down list, type a name for your
   |EB| environment. In this context, the term *environment* refers to the infrastructure |EB|
   provisions for your application. A default name may already be proposed in this drop-down list.
   If a default name is not already proposed, you can type one or choose one from the drop-down
   list, if any additional names are available. The environment name cannot be longer than 23
   characters.

8. In the :guilabel:`URL` area, the box proposes a default subdomain of :code:`.elasticbeanstalk.com`
   that will be the URL for your web application. You can change the default subdomain by typing a
   new subdomain name.

9. Choose :guilabel:`Check availability` to make sure the URL for your web application is not already
   in use.

10. If the URL for your web application is okay to use, choose :guilabel:`Next`.

   .. figure:: images/tkv-aeb-wizard-ec2-console.png
       :scale: 85

11. On the :guilabel:`AWS Options` page, in :guilabel:`Amazon EC2 Launch Configuration`, from the
    :guilabel:`Container type` drop-down list, choose an Amazon Machine Image (AMI) type that will
    be used for your application.

12. In the :guilabel:`Instance type` drop-down list, specify an |EC2| instance type to use. For this
    example, we recommend you use :guilabel:`Micro`. This will minimize the cost associated with
    running the instance. For more information about |EC2| costs, go to the |ec2-pricing|_ page.

13. In the :guilabel:`Key pair` drop-down list, choose an |EC2| instance key pair to use to sign in to
    the instances that will be used for your application.

14. Optionally, in the :guilabel:`Use custom AMI` box, you can specify a custom AMI that will override
    the AMI specified in the :guilabel:`Container type` drop-down list. For more information about
    how to create a custom AMI, go to :eb-dg:`Using Custom AMIs <using-features.customami>` in the
    |EB-dg|_ and :ref:`tkv-create-ami-from-instance`.

15. Optionally, if you want to launch your instances in a VPC, select the :guilabel:`Use a VPC` box.

16. Optionally, if you want to launch a single |EC2| instance and then deploy your application to it,
    select the :guilabel:`Single instance environment` box.

    If you select this box, |EB| will still create an |AS| group, but will not configure it. If you
    want to configure the |AS| group later, you can use the |console|.

17. Optionally, if you want to control the conditions under which your application is deployed to the
    instances, select the :guilabel:`Enable Rolling Deployments` box. You can select this box only
    if you have not selected the :guilabel:`Single instance environment` box.

18. If your application uses AWS services such as |S3| and |DDB|, the best way to provide credentials is
    to use an |IAM| role. In the :guilabel:`Deployed Application Permissions` area, you can either
    choose an existing |IAM| role or create one the wizard will use to launch your environment.
    Applications using the |sdk-net| will automatically use the credentials provided by this |IAM|
    role when making a request to an AWS service.

19. If your application accesses an |RDS| database, in the drop-down list in the :guilabel:`Relational 
    Database Access` area, select the boxes next to any |RDS| security groups the wizard will update
    so that your |EC2| instances can access that database.

20. Choose :guilabel:`Next`.

    * If you selected :guilabel:`Use a VPC`, the :guilabel:`VPC Options` page will appear.

    * If you selected :guilabel:`Enable Rolling Deployments`, but did not select :guilabel:`Use a VPC`,
      the :guilabel:`Rolling Deployments` page will appear. Skip ahead to the instructions later
      in this section that describe how to use the :guilabel:`Rolling Deployments` page.

    * If you did not select :guilabel:`Use a VPC` or :guilabel:`Enable Rolling Deployments`, the
      :guilabel:`Application Options` page will appear. Skip ahead to the instructions later in
      this section that describe how to use the :guilabel:`Application Options` page.

21. If you selected :guilabel:`Use a VPC`, specify information on the :guilabel:`VPC Options` page to
    launch your application into a VPC.

    .. figure:: images/tkv-aeb-wizard-vpc-console.png
        :scale: 85

    The VPC must have already been created. If you created the VPC in the |TVS|, the |TVS| will
    populate this page for you. If you created the VPC in the :eb-dg:`AWS Management Console <AWSHowTo-vpc-basic>`, 
    type information about your VPC into this page.


Key considerations for deployment to a VPC
==========================================

    * Your VPC needs at least one public and one private subnet.

    * In the *ELB Subnet* drop-down list, specify the public subnet. The |TVS| deploys the |ELB| load
      balancer for your application to the public subnet. The public subnet is associated with a
      routing table that has an entry that points to an Internet gateway. You can recognize an
      Internet gateway because it has an ID that begins with :code:`igw-` (for example,
      :code:`igw-83cddaex`). Public subnets that you create by using the |TVS| have tag values
      that identify them as public.
     
    * In the *Instances Subnet* drop-down list, specify the private subnet. The |TVS| deploys the |EC2|
      instances for your application to the private subnet.

    * The |EC2| instances for your application communicate from the private subnet to the Internet through
      an |EC2| instance in the public subnet that performs network address translation (NAT). To
      enable this communication, you will need a :console:`VPC security group <vpc>` that allows 
      traffic to flow from the private subnet to the NAT instance. Specify this VPC security group 
      in the *Security Group* drop-down list.

    For more information about how to deploy an |EB| application to a VPC, go to the |EB-dg|_.

22. After you have filled in all of the information on the :guilabel:`VPC Options` page, choose
    :guilabel:`Next`.

    * If you selected :guilabel:`Enable Rolling Deployments`, the :guilabel:`Rolling Deployments` page
      will appear.

    * If you did not select :guilabel:`Enable Rolling Deployments`, the :guilabel:`Application Options`
      page will appear. Skip ahead to the instructions later in this section that describe how to
      use the :guilabel:`Application Options` page.

23. If you selected :guilabel:`Enable Rolling Deployments`, you specify information on the
    :guilabel:`Rolling Deployments` page to configure how new versions of your applications are
    deployed to the instances in a load-balanced environment. For example, if you have four
    instances in your environment and you want to change the instance type, you can configure the
    environment to change two instances at a time. This helps ensure your application is still
    running while changes are being made.

    .. figure:: images/tkv-aeb-wizard-rolling-console.png
        :scale: 85

24. In the *Application Versions* area, choose an option to control deployments to either a percentage
    or number of instances at a time. Specify either the desired percentage or number.

25. Optionally, in the *Environment Configuration* area, select the box if you want to specify the
    number of instances that remain in service during deployments. If you select this box, specify
    the maximum number of instances that should be modified at a time, the minimum number of
    instances that should remain in service at a time, or both.

26. Choose *Next*.

27. On the :guilabel:`Application Options` page, you specify information about build, Internet
    Information Services (IIS), and application settings.

    .. figure:: images/tkv-aeb-wizard-options-console.png
        :scale: 85

28. In the :guilabel:`Build and IIS Deployment Settings` area, in the :guilabel:`Project build
    configuration` drop-down list, choose the target build configuration. If the wizard can find it,
    :guilabel:`Release` appears otherwise, the active configuration is displayed in this box.

29. In the :guilabel:`App pool` drop-down list, choose the version of the .NET Framework required by
    your application. The correct .NET Framework version should already be displayed.

30. If your application is 32-bit, select the :guilabel:`Enable 32-bit applications` box.

31. In the :guilabel:`App path` box, specify the path IIS will use to deploy the application. By
    default, :guilabel:`Default Web Site/` is specified, which typically translates to the path
    :file:`c:\\inetpub\\wwwroot`. If you specify a path other than :guilabel:`Default Web Site/`, the
    wizard will place a redirect in the :guilabel:`Default Web Site/` path that points to the path
    you specified.

32. In the :guilabel:`Application Settings` area, in the :guilabel:`Health check URL` box, type a URL
    for |EB| to check to determine if your web application is still responsive. This URL is
    relative to the root server URL. The root server URL is specified by default. For example, if
    the full URL is :code:`example.com/site-is-up.html`, you would type :code:`/site-is-up.html`.

33. In the area for :guilabel:`Key` and :guilabel:`Value`, you can specify any key and value pairs you
    want to add to your application's :file:`Web.config` file.

    .. note:: Although not recommended, you can use the area for :guilabel:`Key` and :guilabel:`Value`, to specify
       AWS credentials under which your application should run. The preferred approach is to
       specify an |IAM| role in the :guilabel:`Identity and Access Management Role` drop-down list
       on the :guilabel:`AWS Options` page. However, if you must use AWS credentials instead of an
       |IAM| role to run your application, in the :guilabel:`Key` row, choose
       :guilabel:`AWSAccessKey`. In the :guilabel:`Value` row, type the access key. Repeat these
       steps for :guilabel:`AWSSecretKey`.

34. Choose :guilabel:`Next`.

    .. figure:: images/tkv-aeb-wizard-review-console.png
        :scale: 85

35. On the :guilabel:`Review` page, review the options you configured, and select the :guilabel:`Open
    environment status window when wizard closes` box.

36. Optionally, you can save the deployment configuration to a text file that you can then use with the
    :ref:`standalone deployment tool <tkv-deployment-tool>`. To save the configuration, select
    :guilabel:`Generate AWSDeploy configuration`, choose :guilabel:`Choose File`, and then specify a
    file to which to save the configuration. You can also save the deployment configuration to a
    text file after the deployment is complete. In AWS Explorer, open the context (right-click) menu
    for the deployment and then choose :guilabel:`Save Configuration`. 

37. If everything looks correct, choose :guilabel:`Deploy`.

    .. note:: When you deploy the application, the active account will incur charges for the AWS 
       resources used by the application.

    Information about the deployment will appear in the Visual Studio status bar and the
    :guilabel:`Output` window. It may take several minutes. When the deployment is complete, a
    confirmation message will appear in the :guilabel:`Output` window.

38. To delete the deployment, in AWS Explorer, expand the :guilabel:`Elastic Beanstalk` node, open the
    context (right-click) menu for the subnode for the deployment, and then choose
    :guilabel:`Delete`. The deletion process might take a few minutes.

