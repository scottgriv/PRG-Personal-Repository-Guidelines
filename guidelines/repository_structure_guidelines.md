<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="../docs/images/icon-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">Repository Structure Guidelines</h1>

This guideline details necessary files and overall structure for your repository.

> [!IMPORTANT] 
> This guidelines also details the GitHub specific files and folders that can be included in your repository.
> Examples for key files are located in the root of this repository and within the `.github/` folder.
> Utilize these files as templates to craft your GitHub special/specific files.

---------------

## Table of Contents
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
- [.gitkeep File](#gitkeep-file)
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
- [Images, Gifs, Videos, Diagrams, and Documents](#images-gifs-videos-diagrams-and-documents)
- [Resources](#resources)


## README File

> [!NOTE] 
> **REQUIRED** file for **ALL** tiers.

- A `README` file describes your project and provides information on how to use it.
- The `README` file should be named `README.md`.
- The `README` file should be located in the root of your repository.   
- Use the templates in the [Template Guide](../templates/template_guide.md) as a starting point for your profile `README` (especially if you're using **PRG**).

> [!TIP]
> Consult the [README Guidelines](readme_guidelines.md) for more resources and information on how to write a `README` file.

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
- Compare this file to `AUTHORS`, `CONTRIBUTORS`, and `ACKNOWLEDGMENTS` files.

**Resources:**
- [CREDITS Generator](https://scottgriv.github.io/CREDITS-Generator) - Personal Project - used to generate PRG's CREDITS file.
- [CREDITS Example 1](https://github.com/scottgriv/PRG-Personal-Repository-Guidelines/blob/main/.github/CREDITS.md) - PRG's CREDITS file.
- [CREDITS Example 2](https://github.com/10up/Open-Source-Best-Practices/blob/gh-pages/CREDITS.md) - Unaffiliated project example
- [AUTHORS Explained - Recording Contributors for GNU License](https://www.gnu.org/prep/maintain/html_node/Recording-Contributors.html)

## .github/CHANGELOG.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains a list of changes for each version of your project.
- Use the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format for your changelog.
- Follow [Semantic Versioning](https://semver.org/) guidelines.
    - Given a version number **X.Y.Z** (**MAJOR.MINOR.PATCH**) (e.g. 1.0.0), increment the:
        - **MAJOR** version when you make incompatible API changes.
        - **MINOR** version when you add functionality in a backward compatible manner.
        - **PATCH** version when you make backward compatible bug fixes.
        - A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes.
        - Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

    - For pre-release and build metadata, use the labels **alpha**, **beta**, **rc**, and **build** using the format **MAJOR.MINOR.PATCH-label.build**.
    - Examples:
        - 1.0.0-alpha
        - 1.0.0-beta
        - 1.0.0-rc
            - **rc** stands for release candidate, which is a beta version with potential to be a final product, which is ready to release unless significant bugs emerge.
            - **alpha** and **beta** are used for pre-release versions.
            - **build** is used to identify a build.
            - This scheme is not strictly enforced, but it is recommended by the Semantic Versioning (SemVer) specification, highlighted in their 2.0.0 release [here](https://semver.org/spec/v2.0.0.html#spec-item-9).

**Resources:**
> [Semantic Versioning](https://semver.org/)
> [Semantic Versioning HOWTO](https://github.com/dbrock/semver-howto)
> [Software Versioning](https://en.wikipedia.org/wiki/Software_versioning)
> [What do the numbers in a version typically represent](https://stackoverflow.com/questions/65718/what-do-the-numbers-in-a-version-typically-represent-i-e-v1-9-0-1)
> [How do version numbers work?](https://www.akeeba.com/how-do-version-numbers-work.html#:~:text=Reading%20version%20numbers&text=The%20leftmost%20number%20(1)%20is,%22%20or%20%22subminor%20version%22.)
> [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) 

## .github/CONTRIBUTING.md File

> [!NOTE] 
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to contribute to your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a contributing file for your project.
    - Reference the GitHub Repository [here](https://github.com/bttger/contributing-gen) and the UI Frontend repository for it [here](https://github.com/bttger/contributing-gen-web).

**Resources:**
> [Setting Guidelines for Repository Contributors](https://help.github.com/articles/setting-guidelines-for-repository-contributors/)
> [Awesome Contributing List](https://github.com/mntnr/awesome-contributing)
> [Hall-Of-Fame README Widget](https://github.com/sourcerer-io/hall-of-fame#readme)
> [Contributing-Gen Template](https://generator.contributing.md/#)
> [How to Build a CONTRIBUTING.md - Best Practices](https://contributing.md/how-to-build-contributing-md/)
> [Good-CONTRIBUTING.md-template.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426)

## .github/CODE_OF_CONDUCT.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains a code of conduct for your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a code of conduct for your project.
    - Reference the GitHub Repository [here](https://github.com/bttger/contributing-gen) and the UI Frontend repository for it [here](https://github.com/bttger/contributing-gen-web).


**Resources:**
> [Adding a Code of Conduct to your project](https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/)
> [Awesome Code of Conduct List](https://i-sight.com/resources/18-of-the-best-code-of-conduct-examples/)
> [Debian Code of Conduct](https://www.debian.org/code_of_conduct)    
> [Contributing-Gen Template](https://generator.contributing.md/#)  
> [CODE_OF_CONDUCT Example](https://github.com/remarkjs/.github/blob/main/code-of-conduct.md)
> [Contributor Covenant](https://www.contributor-covenant.org/version/1/4/code-of-conduct/)

## .github/SECURITY.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on the security policy for your project.

**Resources:**
> [Adding a security policy to your repository](https://help.github.com/en/articles/adding-a-security-policy-to-your-repository)

## .github/SUPPORT.md File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to get support for your project.

**Resources:**
> [Adding a support file to your repository](https://help.github.com/en/articles/adding-support-resources-to-your-project)
> [SUPPORT Example](https://github.com/remarkjs/.github/blob/main/support.md)

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
    - e.g. `ISSUE_TEMPLATE/bug_report.md`, `ISSUE_TEMPLATE/feature_request.md`, `ISSUE_TEMPLATE/custom.md`

**Resources:**
> [Creating a issue template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
> [About issue and pull request templates](https://docs.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates)
> [Multiple issue and pull request templates (Blog Post)](https://blog.github.com/2018-01-25-multiple-issue-and-pull-request-templates/)
> [Awesome Template Lists](https://github.com/devspace/awesome-github-templates)
> [Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
> [Manually creating a single issue template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/manually-creating-a-single-issue-template-for-your-repository)

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
> [Manually creating a single issue template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/manually-creating-a-single-issue-template-for-your-repository)

## FUNDING.yml File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to fund your project.


### These are supported funding model platforms
```shell
github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']
```

**Resources:**
> [Displaying a sponsor button in your repository](https://help.github.com/en/articles/displaying-a-sponsor-button-in-your-repository)

## CITATION.cff File

> [!NOTE]
> **OPTIONAL** file for **ALL** tiers.

- This file contains information on how to cite your project.

**Resources:**
> [What is a CITATION.cff file?](https://citation-file-format.github.io/)
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

**Resources:**
> [GitHub Special Files and Paths](https://github.com/joelparkerhenderson/github-special-files-and-paths)
> [Common special files found in the root directory of a repository](https://github.com/kmindi/special-files-in-repository-root/tree/master)

## .gitignore File

> [!NOTE] 
> **REQUIRED** file for **ALL** tiers.

- This file should contain a list of files and folders that should be ignored by Git.
- Its recommended to ignore your vscode workspace files, virtual environment files, build folders, and any sensitive information files.
    - e.g. `.vscode/`, `venv/`, `.env`
- This will dramatically reduce the size of your repository, making it easier to download.

> [!TIP]
> Use the [.gitignore](../.gitignore) file in the root of this repository as a good example and starting point for a .gitignore template for your projects.

> [!NOTE]
> It's good practice to research what the best files are to add to your .gitignore file based on the technology you're using to develop.

## .gitkeep File

> [!NOTE] 
> **OPTIONAL** file for **ALL** tiers.

- Sometimes you may want to include an empty directory as a resource in your project (say, a place to dump image files from an upload process).
- Well, by default, git will ignore empty folders from being uploaded to your repository.
    - This is because git can't track empty directories. It can only track files.
    - Thus, no files/changes, no tracking.
- Adding this file (with no content inside of it), will ensure that git will not ignore the file since a change has taken place.

**Resources:**
> [What is .gitkeep? How to Track and Push Empty Folders in Git](https://www.freecodecamp.org/news/what-is-gitkeep/)


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
- Include any postman collections in this folder.

## Misc. Folders

> [!NOTE]
> **OPTIONAL** folders for **ALL** tiers.

- Add any other folders as needed.
- A lot of projects, especially web frameworks, have a `src/` folder and other related folders.

> [!IMPORTANT]
> It's important to follow your frameworks conventions and [programming style guides](https://github.com/standard/standard).

## Images, GIFs, Videos, Diagrams, and Documents

> [!NOTE] 
> **OPTIONAL** files for **ALL** tiers.

- Include repo images and GIFs in a `docs/images` folder.
- Include repo videos in a `docs/videos` folder.
- Include diagrams (such as UML diagrams) in a `docs/diagrams` folder.
- Add important documents to the `docs` folder.
- Add more folders as needed.

**Resources:**
> [GiFox](https://gifox.io/) - Paid GIF recording tool for macOS.
> [Snagit](https://www.techsmith.com/screen-capture.html) - Paid screen capture tool for macOS and Windows.

## Resources

- [GitHub Repository Structure Best Practices](https://medium.com/code-factory-berlin/github-repository-structure-best-practices-248e6effc405) - A list of GitHub repository structure best practices.
- [Best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories) - Learn how to use repositories most effectively.
- [Best Practices for GitHub Repositories](https://www.codecademy.com/learn/fscp-22-git-and-github-part-ii/modules/wdcp-22-best-practices-for-github-repositories/cheatsheet) - A list of best practices for GitHub repositories.
- [Linguist](https://github.com/github-linguist/linguist/tree/master) - This library is used on GitHub.com to detect blob languages, ignore binary or vendored files, suppress generated files in diffs, and generate language breakdown graphs.
- [Creating discussion category forms](https://docs.github.com/en/discussions/managing-discussions-for-your-community/creating-discussion-category-forms) - You can customize the templates that are available for community members to use when they open new discussions in your repository.
- [Viewing traffic to a repository](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository) - Anyone with push access to a repository can view its traffic, including full clones (not fetches), visitors from the past 14 days, referring sites, and popular content in the traffic graph.
- [JavaScript Standard Style](https://github.com/standard/standard)) - JavaScript Style Guide, with linter & automatic code fixer.
- [Common README for node modules](https://github.com/hackergrrl/common-readme#readme) - A common README style for node modules.
- [Project Guidelines](https://github.com/elsewhencode/project-guidelines) - A set of best practices for JavaScript projects.
- [What are all available Git special files that can be committed to a repository?](https://stackoverflow.com/questions/12605576/what-are-all-available-git-special-files-that-can-be-committed-to-a-repository) - Stack Overflow question on GitHub special files.
- [Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) - You can create default community health files, such as CONTRIBUTING and CODE_OF_CONDUCT. Default files will be used for any repository owned by the account that does not contain its own file of that type.
