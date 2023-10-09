## Project Structure
This section describes requirements for the project file structure of your repository.
Here are some general guidelines to follow:

### .gitignore File
- This file is **always** required for all tiers of projects.
- This file should contain a list of files and folders that should be ignored by Git.
- Its recommended to ignore your vscode workspace files, virtual environment files, and any sensitive information files.
    - i.e. `.vscode/`, `venv/`, `.env`

### .gitattributes File
- This file is **optional** for all tiers of projects.
- One reason I use this file, is to adjust the linguist language statistics on GitHub.

### VERSION File
- A `VERSION` file is only required for **Gold** projects but recommended for **Silver** projects as well. 
- **Bronze** projects do not need a `VERSION` file.
- The version should follow the [Semantic Versioning](https://semver.org/) guidelines.
- i.e. `1.0.0`

### LICENSE File
- A `LICENSE` file is **always** required for all tiers of projects.

### CREDITS File
- A `CREDITS` file is **always** required for all tiers of projects.

### CONTRIBUTING File
- A `CONTRIBUTING` file is **optional** for all tiers of projects.

### Other GitHub Files
Below are some other files you can include in your repository if you want to provide more information about your project:
- Include a `CODE_OF_CONDUCT` file in your repository for more detailed information on the code of conduct for your project.
- Include a `SECURITY` file in your repository for more detailed information on the security policy for your project.
- Include a `SUPPORT` file in your repository for more detailed information on how to get support for your project.
- Include a `ROADMAP` file in your repository for more detailed information on the roadmap for your project.
- Include a `CHANGELOG` file in your repository for more detailed information on the changelog for your project.

### Images
- Include repo images in a `docs/images` folder.
- Add important documents to the `docs` folder.
- Add more folders as needed.

### Templates
- See `templates` folder in this repository for templates you can use for your projects.
- Feel free to use these templates as a starting point for your own projects.
    - i.e. [Gold Template](templates/gold_template.md)
    - i.e. [Silver Template](templates/silver_template.md)
    - i.e. [Bronze Template](templates/bronze_template.md)