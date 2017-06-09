.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _example-lambda-amazon-rekognition:



###########################################################
Tutorial: Creating an Amazon Rekognition Lambda Application
###########################################################

.. meta::
   :description: Using the Toolkit for Visual Studio to create an Amazon Recognition Lambda example
   :keywords: AWS SDK for .NET code examples

This tutorial shows you how to create an |LAM| application that uses Amazon Rekognition
to tag |S3| objects with detected labels.

For prerequisites and information about setting up the |TVSlong|, see :doc:`lambda-index`.

Create a Visual Studio .NET Core |LAM| Image Rekognition Project
================================================================

#. Open Visual Studio, and on the :guilabel:`File` menu, choose :guilabel:`New`, :guilabel:`Project`.
#. In the :guilabel:`Installed` pane, choose  Visual C# and the |LAMlong| Project template.
   Choose AWS Lambda Project with Tests (.NET Core), name the project ImageRekognition, and then choose
   :guilabel:`OK`.

    .. image:: images/ProjectList.png
       :alt: Project types for AWS Lambda projects


#. After you select the project type, choose a blueprint. Blueprints provide starting code to help
   you write your Lambda functions. For this example, choose the :guilabel:`Detect Image Labels` blueprint.

   This blueprint provides code for listening to |S3| events and uses Amazon Rekognition
   to detect labels and add them to the S3 object as tags.

    .. image:: images/lambda-blueprints.png
       :alt: Blueprints for an AWS Lambda project


#. Choose the type of |LAM| function you want to develop, and then choose :guilabel:`Finish`
   to create the Visual Studio project.


When the project is complete, you have a solution with two projects, as shown: the source project
that contains your Lambda function code to deploy to |LAM|, and a test project using
xUnit for testing your function locally.

   .. image:: images/lambda-solution-explorer.png
      :alt: Blueprints for an AWS Lambda project


You might notice when you first create your projects that Visual Studio doesn't find all the NuGet
references. This happens because these blueprints require dependencies that must be retrieved from
NuGet. When new projects are created, Visual Studio only pulls in local references and not remote
references from NuGet. You can fix this easily by right-clicking your references and choosing
:guilabel:`Restore Packages`.

Examine the Files
=================

#. Open the :code:`1Function.cs` file and look at the code that came with the blueprint. The first
   segment of code is the assembly attribute that is added to the top of the file.

   .. code-block:: C#

        // Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
        [assembly: LambdaSerializerAttribute(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]

   By default, Lambda accepts only input parameters and return types of type :code:`System.IO.Stream`.
   To use typed classes for input parameters and return types, you have to register a serializer. This
   assembly attribute is registering the Lambda JSON serializer, which uses :code:`Newtonsoft.Json` to convert
   the streams to typed classes. You can set the serializer at the assembly or method level.

   The class has two constructors. The first is a default constructor that is used when Lambda invokes
   your function. This constructor creates the S3 and Rekognition service clients, and gets the AWS
   credentials for these clients from the |IAM| role you assign to the function when you deploy it. The
   AWS Region for the clients is set to the region your Lambda function is running in. In this blueprint,
   you only want to add tags to the S3 object if the Rekognition service has a minimum level of confidence
   about the label. This constructor checks the environment variable :code:`MinConfidence` to determine the
   acceptable confidence level. You can set this environment variable when you deploy the Lambda function.

   .. code-block:: C#

        public Function()
        {
            this.S3Client = new AmazonS3Client();
            this.RekognitionClient = new AmazonRekognitionClient();

            var environmentMinConfidence = System.Environment.GetEnvironmentVariable(MIN_CONFIDENCE_ENVIRONMENT_VARIABLE_NAME);
            if(!string.IsNullOrWhiteSpace(environmentMinConfidence))
            {
                float value;
                if(float.TryParse(environmentMinConfidence, out value))
                {
                    this.MinConfidence = value;
                    Console.WriteLine($"Setting minimum confidence to {this.MinConfidence}");
                }
                else
                {
                    Console.WriteLine($"Failed to parse value {environmentMinConfidence} for minimum confidence. Reverting back to default of {this.MinConfidence}");
                }
            }
            else
            {
                Console.WriteLine($"Using default minimum confidence of {this.MinConfidence}");
            }
        }

   You can use the second constructor for testing. The test project configures its own S3 and Rekognition
   clients and passes them in.

   .. code-block:: C#

        public Function(IAmazonS3 s3Client, IAmazonRekognition rekognitionClient, float minConfidence)
        {
            this.S3Client = s3Client;
            this.RekognitionClient = rekognitionClient;
            this.MinConfidence = minConfidence;
        }

   :code:`FunctionHandler` is the method Lambda calls after it constructs the instance. Notice that
   the input parameter is of type :code:`S3Event` and not a :code:`Stream`. You can do this because of the registered
   Lambda JSON serializer. The :code:`S3Event` contains all the information about the event triggered in |S3|. The function
   loops through all the S3 objects that were part of the event and tells Rekognition to detect labels. After
   the labels are detected, they are added as tags to the S3 object.

   .. code-block:: C#

        public async Task FunctionHandler(S3Event input, ILambdaContext context)
        {
            foreach(var record in input.Records)
            {
                if(!SupportedImageTypes.Contains(Path.GetExtension(record.S3.Object.Key)))
                {
                    Console.WriteLine($"Object {record.S3.Bucket.Name}:{record.S3.Object.Key} is not a supported image type");
                    continue;
                }

                Console.WriteLine($"Looking for labels in image {record.S3.Bucket.Name}:{record.S3.Object.Key}");
                var detectResponses = await this.RekognitionClient.DetectLabelsAsync(new DetectLabelsRequest
                {
                    MinConfidence = MinConfidence,
                    Image = new Image
                    {
                        S3Object = new Amazon.Rekognition.Model.S3Object
                        {
                            Bucket = record.S3.Bucket.Name,
                            Name = record.S3.Object.Key
                        }
                    }
                });

                var tags = new List();
                foreach(var label in detectResponses.Labels)
                {
                    if(tags.Count < 10)
                    {
                        Console.WriteLine($"\tFound Label {label.Name} with confidence {label.Confidence}");
                        tags.Add(new Tag { Key = label.Name, Value = label.Confidence.ToString() });
                    }
                    else
                    {
                        Console.WriteLine($"\tSkipped label {label.Name} with confidence {label.Confidence} because maximum number of tags reached");
                    }
                }

                await this.S3Client.PutObjectTaggingAsync(new PutObjectTaggingRequest
                {
                    BucketName = record.S3.Bucket.Name,
                    Key = record.S3.Object.Key,
                    Tagging = new Tagging
                    {
                        TagSet = tags
                    }
                });
            }
            return;
        }

   Notice that the code contains calls to :code:`Console.WriteLine()`. When the function is running
   in |LAM|, all calls to :code:`Console.WriteLine()` redirect to |CWLlong|.

#. Open the :code:`aws-lambda-tools-defaults.json` file that the blueprint created. This
   file contains default values that the blueprint has set to help prepopulate some of the fields in the
   deployment wizard. It's also helpful in setting command line options with our integration with the
   new .NET Core CLI. To use it, navigate to the function's project directory and type *dotnet lambda
   help*.

   .. code-block:: JavaScript

An important field is the function handler. This indicates to |LAM| the method to call
in the code in response to the function we're invoking. The format of this field is
:code:`<assembly-name>::<full-type-name>::<method-name>`. Be sure to include the namespace with the
type name.

Deploy the Function
===================

#. Right-click the Lambda project, and then choose :guilabel:`Publish to AWS Lambda`.
   This starts the deployment wizard. Notice that many of the fields
   are already set. These values come from the :code:`aws-lambda-tools-defaults.json` file described earlier.

#. Enter a function name. For this example, use :code:`ImageRekognition`, and
   then choose :guilabel:`Next`.

        .. image:: images/lambda-deployment-wizard-page1.png

#. On the :guilabel:`Advanced Function Details` page, select an IAM role that gives permission for
   your code to access S3 and Rekognition. To keep this post short, select the
   :guilabel:`Power User managed policy`. The tools create a role based on this policy.

#. Finally, set the environment variable :code:`MinConfidence` to 60, and then choose :guilabel:`Upload`.

        .. image:: images/lambda-deployment-wizard-page2.png

   This launches the deployment process, which builds and packages the Lambda project and then creates
   the Lambda function. Once publishing is complete, the :guilabel:`Function` view in the
   :guilabel:`AWS Explorer` window is displayed. From here, you can invoke a test function, view |CWL|
   for the function, and configure event sources.

        .. image:: images/lambda-function-view.png

#. With your function deployed, you need to configure |S3| to send its events to your new function. On
   the :guilabel:`Event Sources` tab, choose :guilabel:`Add`. Then choose Amazon S3
   and the bucket you want to connect to your Lambda function. The bucket must be in the
   same region as the region where the Lambda function is deployed.

Test the Function
=================

Now that the function is deployed and an S3 bucket is configured as an event source for it, open the
S3 bucket browser from the :guilabel:`AWS Explorer` for the bucket you selected. Then upload some images.

When the upload is complete, you can confirm that your function ran by looking at the logs from your
function view. Or, right-click the images in the bucket browser and choose :guilabel:`Properties`.
On the :guilabel:`Tags` tab, you can view the tags that were applied to your object.

        .. image:: images/lambda-object-properties.png
