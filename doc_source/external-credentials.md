# Using external credentials<a name="external-credentials"></a>

If you have a method to generate or look up credentials that isn't directly supported by AWS, you can add to the shared credentials file a profile that contains the `credential_process` setting\. This setting specifies an external command that's run to generate or retrieve authentication credentials to use\. For example, you might include an entry similar to the following in the `config` file:

```
[profile developer]
credential_process = /opt/bin/awscreds-custom --username helen
```

For more information on using external credentials and the associated security risks, see [Sourcing credentials with an external process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html) in the *AWS Command Line Interface User Guide*\.