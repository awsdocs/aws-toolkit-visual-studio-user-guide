.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _lambda-tutorials-index:


##############################################
Using the |LAMlong| Templates in the |TVSlong|
##############################################

.. meta::
   :description: Using the Toolkit for Visual Studio to create an Amazon Lambda projects
   :keywords: AWS SDK for .NET code examples

The |TVSlong| includes |LAMlong| .NET Core project templates for Visual Studio. Use the
templates to quickly develop and deploy .NET Core-based C# |LAM| functions. .NET Core is cross-platform,
supporting Windows, macOS, and Linux, and can be used to develop device, cloud,
and embedded applications.

To install the |TVS|_ you must have either Visual Studio 2017 or Visual Studio 2015 Update 3 and `.NET Core for Windows <https://www.microsoft.com/net/core#windowsvs2015>`_ 
installed.

For more information, see the following:

* For Microsoft .NET Core, see `.NET Core <https://docs.microsoft.com/en-us/dotnet/articles/core/>`_.
* For .NET Core prerequisites and installation instructions for Windows, macOS, and Linux
  platforms, see `.NET Core Downloads <https://www.microsoft.com/net/download/core>`_.
* For information about |LAMlong| functions, see
  `What Is AWS Lambda? <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_

Prerequisites
=============

To do the following tutorials, you must first:

* Install Visual Studio 2015 Update 3 or Visual Studio 2017.
* Install `.NET Core for Windows <https://www.microsoft.com/net/download/core>`_ (not necessary for Visual Studio 2017).
* Install the `AWS Toolkit for Visual Studio <https://aws.amazon.com/visualstudio/>`_. and specify 
  your credentials. See :doc:`getting-set-up`.

Tutorials
=========

.. toctree::
    :titlesonly:
    :maxdepth: 1
    
    lambda-creating-project-in-visual-studio
    lambda-build-test-severless-app
    lambda-rekognition-example
    cw-log-frameworks