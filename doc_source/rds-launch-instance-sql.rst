.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv-launch-rds-instance-sql:

#########################################################
Create a Microsoft SQL Server Database in an RDS Instance
#########################################################

.. meta::
   :description: Create Microsoft SQL Server database in Amazon RDS from AWS Explorer.
   :keywords: Amazon RDS, Microsoft, SQL Server, MySQL

Microsoft SQL Server is designed in such a way that, after launching an |RDS| instance, you need to
create an SQL Server database in the RDS instance.

For information about how to create an |RDS| instance, see :ref:`tkv-launch-rds-instance`.

**To create a Microsoft SQL Server database**

1. In AWS Explorer, open the context (right-click) menu for the node that corresponds to your RDS
   instance for Microsoft SQL Server, and choose :guilabel:`Create SQL Server Database`.

   .. figure:: images/rds-ms-sql-create-db.png
      :scale: 85

2. In the :guilabel:`Create SQL Server Database` dialog box, type the password you specified when you
   created the RDS instance, type a name for the Microsoft SQL Server database, and then choose
   :guilabel:`OK`.

   .. figure:: images/rds-spec-ms-sql-db.png
      :scale: 85

3. The |TVS| creates the Microsoft SQL Server database and adds it to the Visual Studio Server
   Explorer.

   .. figure:: images/rds-sql-svr-explorer.png
      :scale: 85
