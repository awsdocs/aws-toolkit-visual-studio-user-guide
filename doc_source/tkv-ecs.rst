.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _working-with-aws-tkv-ecs:

#############################
Managing Amazon ECS Instances
#############################

.. meta::
   :description: Using the Toolkit for Visual Studio to work with AWS ECS.
   :keywords: services, usage, EC2 Container Service, Docker, repository, cluster

AWS Explorer provides detailed views of |ECSlong| (|ECS|) clusters and container 
repositories. You can create, delete and manage cluster and container details
from within the Visual Studio development environment. 

.. _tkv-ecs-clusters-service-props:

Modifying service properties
====================================

You can vew service details, service events and service properties from the 
cluster view.

1. In AWS Explorer, open the context (right-click) menu for the cluster to manage, 
   and then choose :guilabel:`View`. 

2. In the ECS Cluster view, click :guilabel:`Services` on the left, and then click the
   :guilabel:`Details` tab in the details view. You can click :guilabel:`Events` 
   to see event messages and :guilabel:`Deployments` to deployment status.

3. Click :guilabel:`Edit`. You can change the desired task count and the minimum and maximum
   helathy percent.  

4. Click :guilabel:`Save` to accept changes or :guilabel:`Cancel` to revert to existing values.

.. _tkv-ecs-clusters-tasks-stop:

Stopping a task
===============

You can see the current status of tasks and stop one or more tasks in the cluster view.

*To stop a task*

1. In AWS Explorer, open the context (right-click) menu for the cluster with tasks you wish to stop, 
   and then choose :guilabel:`View`. 

2. In the ECS Cluster view, click :guilabel:`Tasks` on the left. 

3. Make sure :guilabel:`Desired Task Status` is set to :code:`Running`.  Choose the individual 
   tasks to stop and then click :guilabel:`Stop` or click :guilabel:`Stop All` to select and stop
   all running tasks.

4. In the :guilabel:`Stop Tasks` dialog box, choose :guilabel:`Yes`.

.. _tkv-ecs-clusters-service-delete:

Deleting a service
==================

You can delete services from a cluster from the cluster view.

*To delete a cluster service*

1. In AWS Explorer, open the context (right-click) menu for the cluster with a service you want to delete, 
   and then choose :guilabel:`View`. 

2. In the ECS Cluster view, click :guilabel:`Services` on the left, and then click :guilabel:`Delete`.

3. In the :guilabel:`Delete Cluster` dialog box, if there is a load balancer and target group
   in your cluster, you can choose to delete them with the cluster. They will not be used
   when the service is deleted. 

4. In the :guilabel:`Delete Cluster` dialog box, choose :guilabel:`OK`. When the cluster
   is deleted, it will be removed from the AWS Explorer.

.. _tkv-ecs-cluster-view:

Deleting a cluster
==================

You can delete an |ECSlong| cluster from AWS Explorer. 

*To delete a cluster*

1. In AWS Explorer, open the context (right-click) menu for the cluster you want to delete
   under the :guilabel:`Clusters` node of :guilabel:`Amazon ECS`, and then
   choose :guilabel:`Delete`.

2. In the :guilabel:`Delete Cluster` dialog box, choose :guilabel:`OK`. When the cluster
   is deleted, it will be removed from the AWS Explorer.

.. _tkv-ecs-repository-create:

Creating a repository
=====================

You can create an |ECRlong| repository from AWS Explorer. 

*To create a repository*

1. In AWS Explorer, open the context (right-click) menu of the :guilabel:`Repositories` node 
   under :guilabel:`Amazon ECS`, and then choose :guilabel:`Create Repository`.

2. In the :guilabel:`Create Repository` dialog box, provide a repository name and then 
   choose :guilabel:`OK`. 

.. _tkv-ecs-repository-create:

Deleting a repository
=====================

You can delete an |ECRlong| repository from AWS Explorer. 

*To delete a repository*

1. In AWS Explorer, open the context (right-click) menu of the :guilabel:`Repositories` node 
   under :guilabel:`Amazon ECS`, and then choose :guilabel:`Delete Repository`.

2. In the :guilabel:`Delete Repository` dialog box, you can choose to delete the repository
   even if it contains images. Otherwise, it will only be deleted if it is empty. Click
   :guilabel:`Yes`.

