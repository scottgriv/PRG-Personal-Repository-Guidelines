# Project Structure
This section describes requirements for the project file structure of your repository.

> [!IMPORTANT] 
> Templates for the following files can be found in the root of this repository and the `.github` folder.

Here are some general guidelines to follow:

## Images, Gifs, Videos, and Documents
> [!WARNING] 
> **OPTIONAL** files for **ALL** tiers.

- Include repo images and gifs in a `docs/images` folder.
- Include repo videos in a `docs/videos` folder.
- Add important documents to the `docs` folder.
- Add more folders as needed.

## .gitignore File
> [!WARNING] 
> **REQUIRED** file for **ALL** tiers.

- This file should contain a list of files and folders that should be ignored by Git.
- Its recommended to ignore your vscode workspace files, virtual environment files, and any sensitive information files.
    - i.e. `.vscode/`, `venv/`, `.env`

## .gitattributes File
> [!WARNING] 
> **OPTIONAL** file for **ALL** tiers.

- One reason I use this file, is to adjust the linguist language statistics on GitHub.
- See [Linguist](https://github.com/github-linguist/linguist/tree/master) for more information.

## VERSION File
> [!WARNING] 
> **REQUIRED** file for **Gold** tier only.
> **Silver** and **Bronze** tier projects do not require this file, but feel free to add it if you want

- This file should contain the version of your project.
- The version should follow the [Semantic Versioning](https://semver.org/) guidelines.
    - i.e. `1.0.0`

## LICENSE File
> [!WARNING] 
> **REQUIRED** file for **ALL** tiers.

- This file should contain the license for your project.

## CREDITS File
> [!WARNING] 
> **REQUIRED** file for **Gold** tier only.

- This file should contain a list of people who have contributed to your project.

### CHANGELOG File
> [!WARNING]
> **OPTIONAL** file for **ALL** tiers.

- This file should contain a list of changes for each version of your project.
- Follow [Semantic Versioning](https://semver.org/) guidelines mentioned above.
- Use the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format for your changelog.

## CONTRIBUTING File
> [!WARNING] 
> **OPTIONAL** file for **ALL** tiers.

- This file should contain information on how to contribute to your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a contributing file for your project.
    - GitHub Repository: [Here](https://github.com/bttger/contributing-gen-web)

## CODE_OF_CONDUCT File
> [!WARNING]
> **OPTIONAL** file for **ALL** tiers.

- This file should contain a code of conduct for your project.
- See the [Contributing-Gen Template](https://generator.contributing.md/#) to generate a code of conduct for your project.

## Other GitHub Files
> [!WARNING] 
> **OPTIONAL** files for **ALL** tiers.

Below are some other files you can include in your repository if you want to provide more information about your project:
- Include a `SECURITY` file in your repository for more detailed information on the security policy for your project.
    - See [Security Policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository) for more information.
- Include a `SUPPORT` file in your repository for more detailed information on how to get support for your project.
- Include a `ROADMAP` file in your repository for more detailed information on the roadmap for your project.
- Include a `CONTRIBUTORS` file in your repository for more detailed information on the contributors for your project.
- Include a `CODEOWNERS` file in your repository for more detailed information on the code owners for your project.
- Include a `FUNDING` file in your repository for more detailed information on how to fund your project.
- Include a `CONTRIBUTORS` file in your repository for more detailed information on the contributors for your project.
- Include a `PULL_REQUEST_TEMPLATE` file in your repository for more detailed information on the pull request template for your project.
