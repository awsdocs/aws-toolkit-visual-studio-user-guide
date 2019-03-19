.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tkv_setup:

########################
Setting Up the |TVSlong|
########################

.. meta::
   :description: How to set up the AWS Toolkit for Visual Studio.
   :keywords: configuration, prerequisites, region, credentials, uninstall

This topic describes how to install and configure the |TVS|.

.. _prereqs:

Prerequisites
=============

To install and configure the |TVS|, you must:

* Have an AWS account. This account enables you to use AWS services. To get an AWS account, on
  the `AWS home page <http://aws.amazon.com/>`_, choose :guilabel:`Create an AWS Account`.

* Run a supported operating system: Windows 10, Windows 8, or Windows 7.

  We recommend that you install the latest service packs and updates for the Windows version
  you're using.

* Visual Studio 2013 or later (including Community editions).

  We recommend that you install the latest service packs and updates.

.. note:: The |TVS| is still available if you're using Visual Studio versions 2008, 2010, and 2012 (including
   Express editions where available). However, it is not supported. For Express editions, the
   installation includes only the AWS project templates and the :ref:`standalone deployment tool
   <tkv-deployment-tool>`. Visual Studio Express editions don't support third-party extensions, such as
   AWS Explorer. Find links to these older versions of the |TVS| at the bottom of this page.

.. _install:

Install the |TVS|
=================

The |TVS| 2017 is distributed in the 
`Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2017>`_. 
You can also install and update the toolkit using the Extensions and Updates dialog within Visual Studio.

The |TVS| 2013 and 2015 versions are part of the |TFW|. You can install the |TFW| for these versions as
follows.

.. topic:: To install the |TFW|

1. Navigate to the page `AWS Toolkit for Visual Studio <https://aws.amazon.com/visualstudio>`_.

2. In the :guilabel:`Download` section, choose |TVS| 2013-2015 to download the installer.

3. To start the installation, run the downloaded installer and follow the instructions.

.. tip:: By default, the |TVS| is installed in the Program Files directory, which requires
   administrator privileges. To install the |TVS| as a non-administrator, specify a different
   installation directory.

.. _uninstall:

Uninstall the |TVS|
===================

To uninstall the |TVS|, you must uninstall the |TFW|.

.. topic:: To uninstall the |TFW|

1. In Control Panel, open :guilabel:`Programs and Features`.

  .. tip:: To open :guilabel:`Programs and Features` directly, from a command prompt, run the following:
     :code:`appwiz.cpl`

2. Choose |TFW|, and then choose :guilabel:`Uninstall`.

   .. figure:: images/uninstall.png
      :scale: 100

3. If prompted, choose :guilabel:`Yes`.

Uninstalling the |TFW| doesn't remove the Samples directory. This directory is preserved in case
you have modified the samples. You have to manually remove this directory.


.. _older_versions:

Older Versions of the |TVS|
===========================

**Visual Studio 2008** |mdash| Install the |TVS| for Visual Studio 2008 from
https://sdk-for-net.amazonwebservices.com/latest/AWSToolkitForVisualStudio2008.msi.

**Visual Studio 2010 and 2012** |mdash| Install the |TVS| for Visual Studio 2010 and 2012
from https://sdk-for-net.amazonwebservices.com/latest/AWSToolkitForVisualStudio2010-2012.msi.
