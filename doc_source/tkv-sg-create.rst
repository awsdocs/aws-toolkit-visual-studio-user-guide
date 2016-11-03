.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-sg:

##########################################
Managing Security Groups from AWS Explorer
##########################################

.. meta::
   :description: How to manage security groups using the |TVS|.
   :keywords: security groups, permissions

The AWS Toolkit for Visual Studio enables you to create and configure security groups to use with
|EC2long| (|EC2|) instances and |CFN|. When you launch |EC2| instances or deploy an application to
|CFN|, you specify a security group to associate with the |EC2| instances. (Deployment to |CFN|
creates |EC2| instances.)

A security group acts like a firewall on incoming network traffic. The security group specifies
which types of network traffic are allowed on an |EC2| instance. It can also specify that incoming
traffic will be accepted from certain IP addresses only or from specified users or other security
groups only.

.. _tkv-sg-create:

Creating a Security Group
=========================

In this section, we'll create a security group. After it has been created, the security group will
not have any permissions configured. Configuring permissions is handled through an additional
operation.

*To create a security group*

1. In AWS Explorer, under the :guilabel:`Amazon EC2` node, open the context (right-click) menu on the
   :guilabel:`Security Groups` node, and then choose :guilabel:`View`.

2. On the :guilabel:`EC2 Security Groups` tab, choose :guilabel:`Create Security Group`.

3. In the :guilabel:`Create Security Group` dialog box, type a name and description for the security
   group, and then choose :guilabel:`OK`.

   .. figure:: images/tkv-ec2-sg-create.png
       :scale: 85


.. _tkv-permission-sg:

Adding Permissions to Security Groups
=====================================

In this section, we'll add permissions to the security group to allow web traffic through the HTTP
and HTTPS protocols. We'll also allow other computers to connect by using Windows Remote Desktop
Protocol (RDP).

*To add permissions to a security group*

1. On the :guilabel:`EC2 Security Groups` tab, choose a security group and then choose the
   :guilabel:`Add Permission` button.

2. In the :guilabel:`Add IP Permission` dialog box, choose the :guilabel:`Protocol, Port and Network`
   radio button, and then from the :guilabel:`Protocol` drop-down list, choose :guilabel:`HTTP`.
   The port range automatically adjusts to port 80, the default port for HTTP. The
   :guilabel:`Source CIDR` field defaults to 0.0.0.0/0, which specifies that HTTP network traffic
   will be accepted from any external IP address. Choose :guilabel:`OK`.

   .. figure:: images/tkv-ec2-sg-http.png
       :scale: 75

   Open port 80 (HTTP) for this security group

3. Repeat this process for HTTPS and RDP. Your security groups permissions should now look like the
   following.

   .. figure:: images/tkv-ec2-sg-display.png
       :scale: 75

You can also set permissions in the security group by specifying a user ID and security group name.
In this case, |EC2| instances in this security group will accept all incoming network traffic from
|EC2| instances in the specified security group. You must also specify the user ID as a way to
disambiguate the security group name; security group names are not required to be unique across all
of AWS. For more information about security groups, go to the 
:ec2-ug:`EC2 documentation <using-network-security>`.



