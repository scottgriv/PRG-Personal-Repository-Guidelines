<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="../docs/images/icon_2-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">Repository Structure Guidelines</h1>

This guideline details the necessary project file structure for your repository.

> [!IMPORTANT] 
> Templates for key files are located in the root of this repository and within the `.github/` folder.
> Utilize these templates to craft your GitHub special/specific files.

The following are some overarching guidelines pertinent to both **PRG** and general GitHub practices:

---------------

## Table of Contents
- [Images, Gifs, Videos, and Documents](#images-gifs-videos-and-documents)
- [README File](#readme-file)
- [LICENSE File](#license-file)
- [.github/CREDITS File](#githubcredits-file)
- [.github/CHANGELOG.md File](#githubchangelogmd-file)
- [.github/CONTRIBUTING.md File](#githubcontributingmd-file)
- [.github/CODE_OF_CONDUCT.md File](#githubcode_of_conductmd-file)
- [.github/SECURITY.md File](#githubsecuritymd-file)
- [.github/SUPPORT.md File](#githubsupportmd-file)
- [.github/CODEOWNERS File](#githubcodeowners-file)
- [.github/ISSUE_TEMPLATE.md](#githubissue_templatemd-file)
- [.github/PULL_REQUEST_TEMPLATE.md File](#githubpull_request_templatemd-file)
- [FUNDING.yml File](#fundingyml-file)
- [CITATION.cff File](#citationcff-file)
- [Other GitHub Special Files](#other-github-special-files)
- [.gitignore File](#gitignore-file)
- [.gitattributes File](#gitattributes-file)
- [.editorconfig File](#editorconfig-file)
- [.prettierrc File](#prettierrc-file)
- [.eslintrc File](#eslintrc-file)
- [.stylelintrc File](#stylelintrc-file)
- [.huskyrc File](#huskyrc-file)
- [.github Folder](#github-folder)
- [.github/workflows Folder](#githubworkflows-folder)   
- [.github/dependabot.yml File](#githubdependabotyml-file)
- [api Folder](#api-folder)
- [Misc. Folders](#misc-folders)
- [Resources](#resources)


## Images, Gifs, Videos, and Documents

> [!NOTE] 
> **OPTIONAL** files for **ALL** tiers.

- Include repo images and gifs in a `docs/images` folder.
- Include repo videos in a `docs/videos` folder.
- Add important documents to the `docs` folder.
- Add more folders as needed.

## README File

> [!NOTE] 
> **REQUIRED** file for **ALL** tiers.

- A `README` file describes your project and provides information on how to use it.
- The `README` file should be written in [Markdown](https://guides.github.com/features/mastering-markdown/).

**Resources:**
> [About READMEs](https://help.github.com/articles/about-readmes/)
> [Awesome README List](https://github.com/matiassingers/awesome-readme)
> [Profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
> [Organization README](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)

## LICENSE File

> [!NOTE] 
> **REQUIRED** file for **ALL** tiers.

- This file contains the license for your project.

**Resources:**
> [Adding a License to a Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
> [Choose a License](https://choosealicense.com/)
> [Open Source Licenses](https://opensource.org/licenses)

## .github/CREDITS File

> [!NOTE] 
> **OPTIONAL** file for **ALL** tiers.

- This file should contain a list of people who have contributed to your project.
- Compare this file to `AUTHORS`, `CONTRIBUTORS`, and `ACKNOWLEDGMENTS` files below.

## .github/CHANGELOG.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains a list of changes for each version of your project.
- Follow [Semantic Versioning](https://semver.org/) guidelines.
    - Given a version number **MAJOR.MINOR.PATCH** (e.g. 1.0.0), increment the:
        - **MAJOR** version when you make incompatible API changes
        - **MINOR** version when you add functionality in a backward compatible manner
        - **PATCH** version when you make backward compatible bug fixes
        - Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
- Use the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format for your changelog

## .github/CONTRIBUTING.md File

> [!NOTE] 
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to contribute to your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a contributing file for your project.
    - GitHub Repository: [Here](https://github.com/bttger/contributing-gen-web)

**Resources:**
> [Setting Guidelines for Repository Contributors](https://help.github.com/articles/setting-guidelines-for-repository-contributors/)
> [Awesome Contributing List](https://github.com/mntnr/awesome-contributing)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## .github/CODE_OF_CONDUCT.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains a code of conduct for your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a code of conduct for your project.

**Resources:**
> [Adding a Code of Conduct to your project](https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/)
> [Awesome Code of Conduct List](https://i-sight.com/resources/18-of-the-best-code-of-conduct-examples/)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## .github/SECURITY.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on the security policy for your project.

**Resources:**
> [Adding a security policy to your repository](https://help.github.com/en/articles/adding-a-security-policy-to-your-repository)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## .github/SUPPORT.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to get support for your project.

**Resources:**
> [Adding a support file to your repository](https://help.github.com/en/articles/adding-support-resources-to-your-project)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
> [@wooorm's Support Example](https://github.com/remarkjs/.github/blob/main/support.md)

## .github/CODEOWNERS File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on who owns the code for your project.

**Resources:**
> [About code owners](https://help.github.com/articles/about-codeowners/)

## .github/ISSUE_TEMPLATE.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to create a pull request for your project.
- This can also be a folder/directory called `ISSUE_TEMPLATE` with multiple templates for different types of pull requests.
    - i.e. `ISSUE_TEMPLATE/bug_report.md`, `ISSUE_TEMPLATE/feature_request.md`, `ISSUE_TEMPLATE/custom.md`

**Resources:**
> [Creating a issue template for your repository](https://help.github.com/articles/creating-an-issue-template-for-your-repository/)
> [About issue and pull request templates](https://docs.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates)
> [Multiple issue and pull request templates (Blog Post)](https://blog.github.com/2018-01-25-multiple-issue-and-pull-request-templates/)
> [Awesome Template Lists](https://github.com/devspace/awesome-github-templates)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## .github/PULL_REQUEST_TEMPLATE.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to create a pull request for your project.
- This can also be a folder/directory called `PULL_REQUEST_TEMPLATE` with multiple templates for different types of pull requests.

**Resources:**
> [Creating a pull request template for your repository](https://help.github.com/en/articles/creating-a-pull-request-template-for-your-repository)
> [About issue and pull request templates](https://docs.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates)
> [Awesome Template Lists](https://github.com/devspace/awesome-github-templates)
> [About automation for issues and pull requests with query parameters](https://docs.github.com/en/github/building-a-strong-community/about-automation-for-issues-and-pull-requests-with-query-parameters)

## FUNDING.yml File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to fund your project.

**Resources:**
> [Displaying a sponsor button in your repository](https://help.github.com/en/articles/displaying-a-sponsor-button-in-your-repository)
> [Creating a default community health file for your organization](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## CITATION.cff File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to cite your project.

**Resources:**
> [Citation File Format](https://citation-file-format.github.io/)
> [About Citation Files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

## Other GitHub Special Files

> [!NOTE] 
> **OPTIONAL** files for **ALL** tiers.

Below are some other popular files used in GitHub repositories:
- `AUTHORS` file in your repository for more detailed information on the authors for your project.
- `CONTRIBUTORS` a file in your repository for more detailed information on the contributors for your project.
- `ACKNOWLEDGMENTS` file in your repository for more detailed information on the acknowledgments for your project.
- `ROADMAP` file in your repository for more detailed information on the roadmap for your project.
- `GOVERNANCE` file in your repository for more detailed information on the governance for your project.

## .gitignore File

> [!NOTE] 
> **REQUIRED** file for **ALL** tiers.

- This file should contain a list of files and folders that should be ignored by Git.
- Its recommended to ignore your vscode workspace files, virtual environment files, and any sensitive information files.
    - i.e. `.vscode/`, `venv/`, `.env`

## .gitattributes File

> [!NOTE] 
> **OPTIONAL** file for **ALL** tiers.

- One reason I use this file, is to adjust the linguist language statistics on GitHub.

**Resources:**
> [Linguist](https://github.com/github-linguist/linguist/tree/master) 

## .editorconfig File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your editor.

**Resources:**
> [EditorConfig](https://editorconfig.org/)

## .prettierrc File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your code formatting.

**Resources:**
> [Prettier](https://prettier.io/)

## .eslintrc File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your code linting.

**Resources:**
> [ESLint](https://eslint.org/)

## .stylelintrc File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your style linting.

**Resources:**
> [Stylelint](https://stylelint.io/)

## .huskyrc File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your git hooks.

**Resources:**
> [Husky](https://typicode.github.io/husky/#/)

## .github Folder

> [!NOTE]
> **OPTIONAL** folder for **ALL** tiers.

- This folder contains information on how to configure your GitHub repository.

**Resources:**
> [GitHub Docs](https://docs.github.com/en/github/building-a-strong-community)

## .github/workflows Folder

> [!NOTE]
> **OPTIONAL** folder for **ALL** tiers.

- This folder contains information on how to configure your GitHub Actions.

 **Resources:**
> [GitHub Actions Docs](https://docs.github.com/en/actions)

## .github/dependabot.yml File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to configure your GitHub Dependabot.

**Resources:**
> [Dependabot Docs](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates) 

## api Folder

> [!NOTE]
> **OPTIONAL** folder for **ALL** tiers.

- This folder contains information on how to configure your API.
- Include any API documentation in this folder.
- Iclude any postman collections in this folder.

## Misc. Folders

> [!NOTE]
> **OPTIONAL** folders for **ALL** tiers.

- Add any other folders as needed.
- A lot of projects, especially web frameworks, have a `src/` folder and other related folders.

> [!IMPORTANT]
> It's important to follow your frameworks conventions and programming style guides.

## Resources

Below is a great resource for GitHub special files and paths:
- [GitHub Special Files and Paths](https://github.com/joelparkerhenderson/github-special-files-and-paths).
