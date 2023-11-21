<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="../docs/images/icon-pyrg-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">Table Generator Guide</h1>

**PyRG** is a `Python` implementation of the **PRG** system. It is a simple `Python` script that allows you to easily create a project tier table for your **GitHub Portfolio**. Also included is a GitHub Action CI/CD workflow that will automatically generate a table of all your repositories and their **PRG** tiers to deploy to GitHub Pages in order to showcase your projects/portfolio.

---------------

## Table of Contents
- [Initial Setup](#initial-setup)
  - [PRG Connection File](#prg-connection-file)
  - [PRG Project Logo](#prg-project-logo)
  - [Finish Setup](#finish-setup)
- [Python Build Script (PyRG)](#python-build-script-pyrg)
  - [Configuration](#configuration)
  - [Time Zone & Schedule Configuration](#time-zone--schedule-configuration)
  - [Customization](#customization)
- [GitHub Actions Workflow](#github-actions-workflow)
  - [Project Tier Table (Output) and Private Project Tier Table (Input)](#project-tier-table-output-and-private-project-tier-table-input)
  - [Project Tier Badges (Output)](#project-tier-badges-output)
- [GitHub Pages Deployment](#github-pages-deployment)
  - [Local Testing](#local-testing)
  - [GitHub Actions API Secret](#github-actions-api-secret)
- [Running the Workflow](#running-the-workflow)
- [Resources](#resources)

## Initial Setup

In order to get the **PRG** system to work, you must perform the following pre-requisites:

### PRG Connection File

1. In each repository, inside the root project folder, there should be a markdown file called `PRG.md`.
  - See the **PRG Connection File** used in this repo, [here](../PRG.md), for an example and more information on how to use it.
  - Follow the instructions in the file to configure your repository.
  - The file name and path can be changed in the `project_tier_table_generator.py` script (default path is your project root directory).

> [!CAUTION]
> Lines 15-18 are mapped in the `scripts/project_tier_table_generator.py` script to the PRG system. Do not move or change these lines without adjusting the script to account for this change.

   - The GitHub Action Workflow (explained below) uses this file to categorize your repositories.
   - You must have a _Repository Tier_ label for each repository for the categorization to work.
     - Change the repository's `Tier` label to match the tier of the repository (![#FFD700](https://via.placeholder.com/10/FFD700/000000?text=+) **Gold**, ![#C0C0C0](https://via.placeholder.com/10/C0C0C0/000000?text=+) **Silver**, ![#CD7F32](https://via.placeholder.com/10/CD7F32/000000?text=+) **Bronze**, or ![#6236FF](https://via.placeholder.com/10/6236FF/000000?text=+) **Optimized**).
     - The `Tier` label is the only required label for the **PRG** system to work (if configured to look for a **PRG Connection File** file in the root folder).
     - Optionally, if you don't want to categorize your project, but still want to display it in your table, you can use the ![#6236FF](https://via.placeholder.com/10/6236FF/000000?text=+) **Optimized** badge.
     - There are optional labels you can add to your repository as well: `Technology`, `Category`, and `Order`.
     - Place an empty values for `String` labels and `0` for `Integer` labels if you don't want to use them.

### PRG Project Logo

2. Optionally, you can display a logo for your repository in the table. To do so, follow these steps:
   - In the project root folder, there should be a folder called `docs/`.
   - Inside the `docs/` folder, there should be a subfolder called `images/`.
   - Inside the `docs/images/` folder, there should be a file called `PRG.png`.
   - This is the icon that will be used for the project tier table.
     - See the PRG file used in this repo, [here](../docs/images/PRG.png), for an example.
     - By default, if no icon is found, a [placeholder image](../docs/images/icon-placeholder-rounded.png) will be used (defined in the build script).
     <br>
     <img src="../docs/images/icon-placeholder-rounded.png" width="50" height="50"/><br>
     - If a homepage/website is not defined in the repository settings, clicking on the icon will link to the repository.
     - Clicking on the name of the repository will always link to the repository.

### Finish Setup

3. Follow the Configuration steps below to configure the workflow and GitHub pages for deployment.

> [!TIP]
> You can reference your built project tier table in your repository `README` or wherever you see fit.
> This can be helpful showcasing your projects using the **PRG** system.

## Python Build Script (PyRG)

- The `python` script is located in the `scripts` folder called `project_tier_table_generator.py`.
  - There are a number of configurations that are optional and required to run the script. 
  - Overall, you will see that the script is well documented, highly customizable, and easy to follow.
  - Optionally, you can manually add projects that are not on GitHub or are private (and/or excluded in the config flags) by adding them to the `categories/project_tier_table_private.md` file.
    - Add images used in this private table in the `docs/images/private_repos` folder.
    - Projects in this file will be consolidated into the main table when the workflow runs.

> [!WARNING]
> Make sure you add all the required fields to the private tier table in order for the table to be generated properly or this can cause the output to be incorrect.

### Configuration

- The build script that generates the project tier table is located in the `scripts` folder called [project_tier_table_generator.py](../scripts/project_tier_table_generator.py).
  - There are a number of configuration flags on the top of the script that you can set to customize the output of the table to your liking.
- The config file for Jekyll/GitHub Pages is located in the `_config.yml` file in the root of the project.
  - There are a number of titles and descriptions you can set to customize the output of the table to your liking.

### Time Zone & Schedule Configuration

The time zone will be updated on the bottom of the table to reflect the time zone of the repository owner and when the table was last updated.
- For local testing, adjust the `MY_TIME_ZONE` configuration in the `project_tier_table_generator.py` file.
- For deployment with GitHub Pages, adjust the `TZ` environment variable under `env` to your time zone in the `.github/workflows/main.yml` file.
  - The default time zone is set to `America/New_York` for both local testing and deployment.
- The script will run on a weekly basis (Sunday's at 12:00 AM - defined using a cron expression in the workflow file).
- The script can also be run manually by clicking on the `Run workflow` button in the `Actions` tab in your repository.

### Customization

You can customize your build script however you want if you want to categorize your project tier table further.
- You have three options for customizations:

1. Static Table Fields:
  - Feel free to add more labels/fields/columns to your project tier table.
  - Be sure to adjust the `PRG.md` (**PRG Connection File**) and the `project_tier_table_generator.py` script accordingly.
  - You will also have to adjust the `project_tier_table_private.md` file to display the new fields.
2. Dynamic Table Fields using GitHub API:
  - There are also other API fields that can be used such as Total Stars, Forks, etc.
  - If you decide to modify the output, consult the [GitHub API](https://docs.github.com/en/rest/reference/repos#get-a-repository) for more details on what fields are available and be sure to adjust the `project_tier_table_generator.py` script accordingly.
  - You will also have to adjust the `project_tier_table_private.md` file to display the new fields.
3. HTML Layouts, CSS Styles, Images and Fonts:
  - Adjust the `_layouts/default.html` file to change the layout of the table.
  - Adjust `assets/css/style.css` to change the styling of the table.
  - Adjust `assets/images/` to change the images used in the table.
  - Adjust `assets/fonts/` to change the fonts used in the table.

## GitHub Actions Workflow

- The GitHub action is defined in the `.github/workflows` folder called `main.yml`.
  - The name of the workflow is `weekly-project-tier-table-generator`.
  - The workflow will call `scripts/project_tier_table_generator.py` which will build the table and output it to `categories/project_tier_table.md`.
 
### Project Tier Table (Output) and Private Project Tier Table (Input)

- See the [Project Tier Table](../categories/project_tier_table.md) and [Private Project Tier Table](/categories/project_tier_table_private.md) for example inputs and outputs of what the table looks like (placeholder images won't be displayed in the output due to the GitHub Action workflow running on a public repository).
- The script will also update the [Badge Reference Guide](../categories/badge_reference_guide.md) file with the latest badges you can use to add to your repository `READMEs` that use **PRG**.

### Project Tier Badges (Output)

See [Badge Reference Guide](../categories/badge_reference_guide.md) for more details on how to create badges for your repository.
- Run the workflow above to get an update `categories/badge_reference_guide.md` file pointing to your **PRG** system.
- Place the badges in your repository `README` to showcase your **PRG Collection**.
- Use my repos and **PRG Collection** as an example of how to use the badges in your `README` files.

## GitHub Pages Deployment

### Local Testing

1. Build Script Testing:
- You can test the script locally by running the following command in the root of the project:
  - `python scripts/project_tier_table_generator.py`

2. Jekyll Testing for GitHub Pages:
- Install Jekyll on your machine (follow the instructions [here](https://jekyllrb.com/docs/installation/)):
  - `gem install bundler jekyll`
- You can test the Jekyll build locally by running the following command in the root of the project:
  - `bundle exec jekyll serve`
- You can view the Jekyll build locally by going to the following URL in your browser:
  - `http://localhost:4000/`

### GitHub Actions API Secret

- You will need to create a GitHub Actions API Secret in order for the workflow to run:
1. Go to your GitHub profile settings.
2. Click on the `Developer settings` tab.
3. Click on the `Personal access tokens` tab.
4. Click on the `Generate new token` button.
5. Name the token `GITHUB_TOKEN`.
6. Select the `repo` scope.
7. Click on the `Generate token` button.
8. Copy the token and save it somewhere safe.
9. Go to your repository settings.
10. Click on the `Secrets` tab.
11. Click on the `New repository secret` button.
12. Name the secret `MY_GITHUB_TOKEN`.

- Some common errors you may see when running the workflow:
  - `Error: Resource not accessible by integration`
    - If you see this error, make sure you have the correct token and that you have the `repo` scope selected.
  - `Error: fatal: could not read Username for 'https://github.com': terminal prompts disabled`
    - If your secret token is not set correctly, you will see this.
- For local testing, if you accidentally commit your token, you can revoke the token and generate a new one.

## Running the Workflow

1. Fork this repository.
2. Go to your forked repository and click on the `Actions` tab.
3. Click on the `weekly-project-tier-table-generator` workflow.
4. Click on the `Run workflow` button.
5. Go to your repository settings.
6. Click on the `Pages` tab.
7. Under `Source`, select the `main` branch (or whatever branch you want to deploy from).
8. Click on the `Save` button.
9. Run the pages workflow.
10. Click on the `URL` link to view your project tier table.

- The workflow should take about 1-2 minutes to run (depending on how many repositories you have).
- Be sure to add **PRG Connection Files** to your repositories and add the `Tier` label to each repository or else the workflow will be blank.
  - Optionally, you can adjust the config files in the build script to ignore the **PRG Connection File** and pull in all of your repos without categorizing them.
  - If you opt to do this, repositories will have the ![#6236FF](https://via.placeholder.com/15/6236FF/000000?text=+) **Optimized** badge by default.

## Resources

- [Jekyll](https://jekyllrb.com/) - Static Site Generator for GitHub Pages
- [Jekyll Installation](https://jekyllrb.com/docs/installation/) - Jekyll Installation Guide
- [Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#about-custom-domain-configuration) - GitHub Pages Custom Domain Configuration
- [Troubleshooting custom domains and GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages) - GitHub Pages Custom Domain Troubleshooting
- [GitHub Pages: Generate SSL certificate for www subdomain](https://github.com/isaacs/github/issues/1675) - GitHub Pages SSL Certificate Generation Discussion
- [Securing your GitHub Pages site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https) - GitHub Pages HTTPS Configuration
- [Quickstart for GitHub REST API](https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28) - Learn how to get started with the GitHub REST API.

