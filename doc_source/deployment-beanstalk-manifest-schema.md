# Elastic Beanstalk Windows Deployment Manifest Schema<a name="deployment-beanstalk-manifest-schema"></a>

This topic provides the Elastic Beanstalk Windows Deployment Manifest Schema for reference\.

The schema is also available for download [here](aws-vs-toolkit.s3.amazonaws.com/JSONSchemas/aws-windows-deployment-manifest-schema.json)\.

```
{
  "$schema": "http://json-schema.org/draft-04/schema",
  "title": "JSON schema for AWS ElasticBeanstalk windows deployment manifest",

  "type": "object",
  "additionalProperties": true,

  "definitions": {

    "iisConfig": {
      "description": "Configuration to apply to IIS before deploying applications",
      "type": "object",
      "properties": {
        "appPools": { "$ref": "#/definitions/appPools" }
      }
    },

    "appPools": {
      "description": "This list of IIS App Pools to configure.",
      "type": "array",
      "items": { "$ref": "#/definitions/appPool" }
    },

    "appPool": {
      "description": "An App Pool to configure in IIS before deploying applications",
      "type": "object",
      "required": [ "name" ],
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the app pool"
        },
        "enable32Bit": {
          "type": "boolean",
          "description": "Enables a 32-bit application to run on a computer that runs a 64-bit version of Windows"
        },
        "managedPipelineMode": {
          "type": "string",
          "description": "Request-processing mode that an application pool uses",
          "enum": [ "Integrated", "Classic" ]
        },
        "managedRuntimeVersion": {
          "type": "string",
          "description": "Specifies the .NET Runtime version to be used by the application pool",
          "enum": [ "No Managed Code", "v2.0", "v4.0" ]
        },
        "queueLength": {
          "type": "integer",
          "description": "Indicates to HTTP.sys how many requests to queue for an application pool before rejecting future requests"
        },

        "cpu": {
          "type": "object",
          "description": "Properties for configuring the app pool's cpu usage",
          "properties": {
            "limitPercentage": {
              "type": "number",
              "description": "Configures the maximum percentage of CPU time that the worker processess in an application pool are allowed to consume"
            },
            "limitAction": {
              "type": "string",
              "description": "The action to take when the CPU limit is reached",
              "enum": [ "NoAction", "KillW3wp", "Throttle", "ThrottleUnderLoad" ]
            },
            "limitMonitoringInterval": {
              "type": "number",
              "description": "Specifies the reset period (in minutes) for CPU monitoring and throttling limits on the application pool"
            }
          }
        },

        "recycling": {
          "type": "object",
          "description": "Properties for configuring the app pool's policy for recycling the process",
          "properties": {
            "regularTimeInterval": {
              "type": "integer",
              "description": "Period of time (in minutes) after which an application pool will recycle"
            },
            "requestLimit": {
              "type": "integer",
              "description": "Maximum number of requests an application pool can process before it is recycled"
            },
            "memory": {
              "type": "integer",
              "description": "Specifies the amount of virtual memory (in kilobytes) that a worker process can use before the worker process is recycled"
            },
            "privateMemory": {
              "type": "integer",
              "description": "Specifies the amount of private memory (in kilobytes) that a worker process can use before the worker process recycles"
            }
          }
        }

      }
    },

    "deployments": {
      "description": "This list of applications to deploy.",
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "description": {
          "type": "string"
        },
        "msDeploy": { "$ref": "#/definitions/msDeploy" },
        "aspNetCoreWeb": { "$ref": "#/definitions/aspNetCoreWeb" },
        "custom": { "$ref": "#/definitions/custom" }
      }
    },

    "msDeploy": {
      "description": "Applications that are deployed using MSDeploy.exe.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "description": "The name of the application. This value must be unique for all applications deployed in the manifest.",
            "type": "string"
          },
          "special": {
            "description": "The name of the application. This value must be unique for all applications deployed in the manifest.",
            "type": "string"
          },		  
          "description": {
            "type": "string"
          },
          "parameters": {
            "description": "Parameters used deploy the application.",
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "appBundle": {
                "description": "The path to the application appBundle relative to the manifest file.",
                "type": "string"
              },
              "iisWebSite": {
                "description": "The IIS Web Site to deploy the application to.",
                "type": "string",
                "default": "Default Web Site"
              },
              "iisPath": {
                "description": "The virtual directory path configured in IIS for the application.",
                "type": "string",
                "default": "/"
              },
              "appPool": {
                "description": "The app pool that will run this application. If the app pool does not exist then a new app pool will be created with IIS default values.",
                "type": "string"
              }
            },
            "required": [ "appBundle" ]
          },
          "scripts": { "$ref": "#/definitions/eventScripts" }
        },
        "required": [ "name", "parameters" ]
      }
    },

    "aspNetCoreWeb": {
      "description": "The list of ASP.NET Core applications to be deployed with IIS support.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "description": "The name of the application. This value must be unique for all applications deployed in the manifest.",
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "parameters": {
            "description": "Parameters used deploy the application.",
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "appBundle": {
                "description": "The path to the application appBundle relative to the manifest file. This can be either a path to a zip archive or a directory relative to the manifest file.",
                "type": "string"
              },
              "iisWebSite": {
                "description": "The IIS Web Site to deploy the application to.",
                "type": "string",
                "default": "Default Web Site"
              },
              "iisPath": {
                "description": "The virtual directory path configured in IIS for the application.",
                "type": "string",
                "default": "/"
              },
              "appPool": {
                "description": "The app pool that will run this application. If the app pool does not exist then a new app pool will be created with IIS default values.",
                "type": "string"
              }
            },
            "required": [ "appBundle" ]
          },
          "scripts": { "$ref": "#/definitions/eventScripts" }
        },
        "required": [ "name", "parameters" ]
      }
    },

    "custom": {
      "description": "The list of custom deployments.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "description": "The name of the application. This value must be unique for all applications deployed in the manifest.",
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "scripts": { "$ref": "#/definitions/deployScripts" }
        },
        "required": [ "name" ]
      }
    },


    "eventScripts": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "preInstall": { "$ref": "#/definitions/scriptElement" },
        "postInstall": { "$ref": "#/definitions/scriptElement" },
        "preRestart": { "$ref": "#/definitions/scriptElement" },
        "postRestart": { "$ref": "#/definitions/scriptElement" },
        "preUninstall": { "$ref": "#/definitions/scriptElement" },
        "postUninstall": { "$ref": "#/definitions/scriptElement" }
      }
    },

    "deployScripts": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "preInstall": { "$ref": "#/definitions/scriptElement" },
        "postInstall": { "$ref": "#/definitions/scriptElement" },
        "preRestart": { "$ref": "#/definitions/scriptElement" },
        "postRestart": { "$ref": "#/definitions/scriptElement" },
        "preUninstall": { "$ref": "#/definitions/scriptElement" },
        "postUninstall": { "$ref": "#/definitions/scriptElement" },

        "install": { "$ref": "#/definitions/scriptElement" },
        "restart": { "$ref": "#/definitions/scriptElement" },
        "uninstall": { "$ref": "#/definitions/scriptElement" }
      }
    },

    "scriptElement": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "file": {
          "type": "string"
        },
        "ignoreErrors": {
          "type": "boolean",
          "default": false
        }
      },
      "required": [ "file" ]
    }
  },
  "properties": {
    "manifestVersion": {
      "description": "The version of the manifest this file is compatible with.",
      "type": "number",
      "default": 1,
      "enum": [ 1 ]
    },
	"iisConfig" :{ "$ref": "#/definitions/iisConfig" },
    "deployments": { "$ref": "#/definitions/deployments" }
  },
  "required": [ "manifestVersion", "deployments" ]
}
```
