.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-amazon-rds-security-groups:

#####################
|RDS| Security Groups
#####################

.. meta::
   :description: Amazon RDS security groups.
   :keywords: Amazon RDS, security group

|RDS| security groups enable you to manage network access to your |RDS| instances. With security
groups, you specify sets of IP addresses using CIDR notation, and only network traffic originating
from these addresses is recognized by your |RDS| instance.

Although they function in a similar way, |RDS| security groups are different from |EC2| security
groups. It is possible to add an EC2 security group to your RDS security group. Any EC2 instances
that are members of the EC2 security group are then able to access the RDS instances that are
members of the RDS security group.

For more information about |RDS| security groups, go to the :rds-ug:`RDS Security Groups
<Overview.RDSSecurityGroups>`. For more information about |EC2| security groups, go to the
:ec2-ug:`EC2 User Guide <using-network-security>`.

.. _tkv-create-an-amazon-rds-security-group:

Create an |RDS| Security Group
------------------------------

You can use the |TVS| to create an RDS security group. If you use the AWS Toolkit to launch an RDS
instance, the wizard will allow you to specify an RDS security group to use with your instance. You
can use the following procedure to create that security group before you start the wizard.

.. topic:: To create an Amazon RDS security group

    #. In AWS Explorer, expand the :guilabel:`Amazon RDS` node, open the context (right-click) menu for the
       :guilabel:`DB Security Groups` subnode and choose :guilabel:`Create`.

       .. figure:: images/rds-sg-create-menu.png
            :scale: 85

       Alternatively, on the :guilabel:`Security Groups` tab, choose :guilabel:`Create Security Group`.
       If this tab isn't displayed, open the context (right-click) menu for the :guilabel:`DB Security
       Groups` subnode and choose :guilabel:`View`.

       .. figure:: images/rds-sg-create-dashboard.png
            :scale: 85

    #. In the :guilabel:`Create Security Group` dialog box, type a name and description for the security
       group, and then choose :guilabel:`OK`.

       .. figure:: images/rds-sg-create.png
            :scale: 85


.. _tkv-set-access-permissions-for-rds-security-group:

Set Access Permissions for an |RDS| Security Group
--------------------------------------------------

By default, a new |RDS| security group provides no network access. To enable access to |RDS|
instances that use the security group, use the following procedure to set its access permissions.

.. topic:: To set access for an Amazon RDS security group

    #. On the :guilabel:`Security Groups` tab, choose the security group from the list view. If your
       security group does not appear in the list, choose :guilabel:`Refresh`. If your security group
       still does not appear in the list, verify you are viewing the list for the correct AWS region.
       :guilabel:`Security Group` tabs in the AWS Toolkit are region-specific.

       If no :guilabel:`Security Group` tabs appear, in AWS Explorer, open the context (right-click)
       menu for the :guilabel:`DB Security Groups` subnode and choose :guilabel:`View`.

    #. Choose :guilabel:`Add Permission`.

       .. figure:: images/rds-sg-add-permission.png
            :scale: 85

       :guilabel:`Add Permissions` button on the :guilabel:`Security Groups` tab

    #. In the :guilabel:`Add Permission` dialog box, you can use CIDR notation to specify which IP
       addresses can access your RDS instance, or you can specify which EC2 security groups can access
       your RDS instance. When you choose :guilabel:`EC2 Security Group`, you can specify access for
       all EC2 instances associated with an AWS account have access, or you can choose a EC2 security
       group from the drop-down list.

       .. figure:: images/rds-sg-cidr-ec2.png
            :scale: 85

       The AWS Toolkit attempts to determine your IP address and auto-populate the dialog box with the
       appropriate CIDR specification. However, if your computer accesses the Internet through a
       firewall, the CIDR determined by the Toolkit may not be accurate.

