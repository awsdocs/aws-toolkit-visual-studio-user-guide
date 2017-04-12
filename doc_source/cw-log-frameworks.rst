.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _using_logging_frameworks_with_awslambda:



###################################################################################
Tutorial: Using Amazon Logging Frameworks with |LAMlong| to Create Application Logs
###################################################################################

.. meta::
   :description: Using Amazon Logging Frameworks with |LAMlong|

You can use |CWLlong| to monitor, store, and access your application’s logs. To get log data into
|CWL|, you can use an AWS SDK or install the |CWL| agent to monitor certain log folders. Today, we’ve
made it even easier to use |CWL| with .NET applications by integrating |CWL| with several popular
.NET logging frameworks.

The supported .NET logging frameworks are `NLog <https://www.nuget.org/packages/AWS.Logger.NLog//>`_,
`Log4net <https://www.nuget.org/packages/AWS.Logger.Log4net/>`_, and the new built-in
`ASP.NET Core logging Framework <https://www.nuget.org/packages/AWS.Logger.AspNetCore/>`_. For each
framework, all you need to do is add the appropriate NuGet package, add |CWL| as an output source,
and then use your logging library as you normally would.

For example to use |CWL| with a .NET application using NLog, add the :code:`AWS.Logger.NLog` NuGet package,
and then add the AWS target into your :code:`NLog.config` file. Here is an example of an :code:`NLog.config`
file that enables both |CWL| and the console as output for the log messages.

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8" ?>
    <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          throwExceptions="true">
      <targets>
        <target name="aws" type="AWSTarget" logGroup="NLog.ConfigExample" region="us-east-1"/>
        <target name="logfile" xsi:type="Console" layout="${callsite} ${message}" />
      </targets>
      <rules>
        <logger name="*" minlevel="Info" writeTo="logfile,aws" />
      </rules>
    </nlog>


After performing these steps, when you run your application the log messages written with NLog are sent
to |CWL|. Then you can view your application’s log messages in near real time from the |CWL| console.
You can also set up metrics and alarms from the |CWL| console, based on your application’s log messages.

These logging plugins are all built on top of the |sdk-net|, and use the same behavior used by the
SDK to find AWS credentials. The credentials used by the logging plugins must have the following
permissions to access |CWL|.

.. code-block:: JavaScript

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "logs:DescribeLogGroups"
          ],
          "Resource": [
            "arn:aws:logs:*:*:*"
          ]
        }
      ]
    }

The AWS .NET logging plugins are a new open source project on `GitHub <https://github.com/aws/aws-logging-dotnet>`_. 
All of the plugins are there, including `samples <https://github.com/aws/aws-logging-dotnet/tree/master/samples>`_ 
and `instructions <https://github.com/aws/aws-logging-dotnet/blob/master/README.md>`_ on how to configure 
|CWL| for each of the supported .NET logging frameworks.

