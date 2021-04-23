# Using CodeArtifact in Visual Studio<a name="using-aws-codeartifact"></a>

AWS CodeArtifact is a fully managed artifact repository service that makes it easy for organizations to securely store and share software packages used for application development\. You can use CodeArtifact with popular build tools and package managers such as the NuGet and \.NET Core CLIs and Visual Studio\. You can also configure CodeArtifact to pull packages from an external, public repository such as [NuGet\.org](https://www.nuget.org/)\.

In CodeArtifact, your packages are stored in repositories which are then stored within a domain\. The AWS Toolkit for Visual Studio simplifies the configuration of Visual Studio with your CodeArtifact repositories, making it easy to consume packages in Visual Studio from both CodeArtifact directly and NuGet\.org\.

## Add your CodeArtifact repository as a NuGet package source<a name="add-repo-as-nuget-package-source"></a>

To consume packages from your CodeArtifact, you will need to add your repository as a packabe source in the **NuGet Package Manager** in Visual Studio

 **To add your repository as a package source** 

1. In AWS Explorer, navigate to your repository in the **AWS CodeArtifact** node\.

1. Open the context \(right\-click\) menu for the repository you want to add, and then choose **Copy NuGet Source Endpoint**\.

1. Navigate to **Package Sources** underneath the **NuGet Package Manager** node in the **Tools > Options** menu\.

1. In **Package Sources**, select the plus sign \(**\+**\), edit the name, and paste the NuGet source endpoint URL that you copied earlier in the **Source** field\.

1. Select the checkbox next to your newly added package source to enable it\.
**Note**  
We recommend adding an external connection to **NuGet\.org** to your CodeArtifact and disabling the **nuget\.org** package source in Visual Studio\. When using an external connection, all of the dependencies pulled from **NuGet\.org** are stored in CodeArtifact\. If **NuGet\.org** goes down for any reason, the packages you need will still be available\. For more information about external connections, see [Add an external connection](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html) in the *AWS CodeArtifact User Guide*\.

1. Choose **OK** to close the menu\.

For more information about using CodeArtifact with Visual Studio, see [Use CodeArtifact with Visual Studio](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-visual-studio.html) in the *AWS CodeArtifact User Guide*\.