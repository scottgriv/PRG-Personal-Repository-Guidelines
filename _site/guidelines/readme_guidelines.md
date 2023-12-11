<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="../docs/images/icon-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">README Guidelines</h1>

General instructions for crafting a `README` file are provided here, tailored for **PRG** projects but applicable to any type of project.

---------------

## Table of Contents

- [README File](#readme-file)
    - [Templates](#templates)
    - [Markdown](#markdown)
    - [GitHub Markdown Alerts](#github-markdown-alerts)
    - [Disclaimer](#disclaimer)
- [Header](#header)
    - [Header Icon](#header-icon)
    - [Badges](#badges)
    - [Divider](#divider)
- [Title](#title)
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Background Story](#background-story)
- [Definitions](#definitions)
- [Getting Started](#getting-started)
    - [Dependencies](#dependencies)
    - [Configuration](#configuration)
    - [Installation](#installation)
    - [Deployment](#deployment)
- [What's Inside?](#whats-inside)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Closing](#closing)
- [Limitations](#limitations)
- [Disclaimer](#disclaimer-1)
- [What's Next?](#whats-next)
- [Project](#project)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)
- [Footer](#footer)
    - [Credits](#credits)
    - [Footer Icon](#footer-icon)
- [Resources](#resources-1)

## README File

> [!WARNING]
> A `README` file is **REQUIRED** for **ALL** tiers.

- Use the templates in the next section as a starting point for your profile `README` (especially if you're using **PRG**).

### Templates

For templates and examples of `READMEs`, see the [templates](../templates) directory.
Templates are broken down by the four categorized tiers of projects: **Platinum**, **Gold**, **Silver**, and **Bronze**.

- See the [Template Guide](../templates/template_guide.md) for templates used for each tier.

### Markdown

- The `README` file should be written in [Markdown](https://guides.github.com/features/mastering-markdown/).
- GitHub has its own [flavor of Markdown](https://github.github.com/gfm/#backslash-escapes), which is what you should use.

### GitHub Markdown Alerts

GitHub has a special syntax for alerts in Markdown files:

> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

Read more about [GitHub Markdown Alerts](https://github.com/orgs/community/discussions/16925).

### Disclaimer

> [!IMPORTANT]  
> I only mentioned the important parts of a `README` file, there are many other things you can add to your `README` file that I didn't mention here. Feel free to add whatever you want to your `README` file including new sections, images, GIFs, etc.
> Below is a description of each section of a **PRG** `README` and what it should contain.
> Depending on the tier of your project, some sections are **REQUIRED** while others are **OPTIONAL**.

> [!NOTE]
> Your Profile `README` does not need to adhere to the **PRG** guidelines defined in this document, but it is encouraged to include the [PRG Profile Badge](./brand_guidelines#prg-profile-badge) to link to your **PRG Collection**.


---------------

Below is a description of each section of a **PRG** `README` and what it should contain:

## Header

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- The header consists of two parts: the Header Icon and the Badges.
- This should be the **first** section of your `README`.

### Header Icon

- The header icon is a either a logo/icon or a custom banner.
- A banner should always be used for **Platinum/Gold** projects, while a logo/icon should be used for **Silver/Bronze** projects.
- A banner is a custom design created to represent your project.
    - I use [Sketch](https://www.sketch.com/) to create my banners and designs, but you can use any design software you want.
    - See [Brand Guidelines](brand_guidelines.md) for more information on creating banners and other graphics for your project.
- For **Silver/Bronze** projects, you can use a custom icon or a logo of the technology you used to develop your project instead of a banner. 

    > [!TIP]  
    > There are plenty of free logos out there for most technologies, just make sure you give credit to the creator of the logo if it's required (follow the license for the image).

- e.g. My logo for my Silver Project, [UWP Audio Recorder](https://github.com/scottgriv/uwp-audio_recorder):

<div align="center">
    <a href="https://github.com/scottgriv/uwp-audio_recorder" target="_blank">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="../docs/images/demo/icon-dark.png">
            <source media="(prefers-color-scheme: light)" srcset="../docs/images/demo/icon-light.png">
            <img alt="Icon" src="../docs/images/demo/icon-dark.png" width="207" height="207">
        </picture>
    </a>
</div>

> [!TIP]  
> Append `#gh-dark-mode-only` or `#gh-light-mode-only` to the end of the image URL to only show the image in dark or light mode respectively. Be sure to have both a dark and light version of the image when necessary. More on this (shameless plug) [here](https://github.com/scottgriv/markdown-demo#images).

- e.g. A logo for a Bronze project that showcases JavaScript code:
    
<div align="center">
    <img src="../docs/images/demo/javascript.png" alt="JavaScript" style="width: 15%; vertical-align: left;" />
</div>
<br>

- The header icon or banner should always be clickable and take you to your project's website/product/demo.
    - If you do not have a website/product/demo, you should link it to your projects repository main branch.

### Badges

- Badges are a great way to showcase the technologies, frameworks, and languages used in your project. 
- Badges are generated using [Shields.io](https://shields.io/).
- You should include all major technologies, frameworks, and languages used in your project (one badge per technology). This badge should contain the technology name and version you used to develop your project.
    - e.g. [![Python Badge](https://img.shields.io/badge/Python-3.8.5-244C6F?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-385/)
    - e.g. [![Node.js Badge](https://img.shields.io/badge/Node.js-16.13.2-036E02?style=for-the-badge&logo=node.js)](https://nodejs.org/en/)
- The badge color should match the color of the technology's logo. Use a browser extension like [ColorZilla](https://www.colorzilla.com/) to get the exact color code of a logo from a website.
- The badge should hyperlink to the technology's website or version release page (whatever you think is more appropriate).
- Optionally you can add badges for your email, website, and GitHub profile so people can contact you or follow you. You can also add a link to your [BuyMeACoffee](https://www.buymeacoffee.com/) page if you have one to support your work.
    - e.g. [![Email Badge](https://img.shields.io/badge/gmail-contact_me-DC4233?style=for-the-badge&logo=gmail)](mailto:scott.grivner@gmail.com)
    - e.g. [![GitHub Badge](https://img.shields.io/badge/github-follow-9031AC?style=for-the-badge&logo=github&color=9031AC)](https://github.com/scottgriv)
    - e.g. [![BuyMeACoffee Badge](https://img.shields.io/badge/buy_me_a_coffee-support_me-FEDE1F?style=for-the-badge&logo=buymeacoffee&color=FEDE1F)](https://www.buymeacoffee.com/scottgriv)


> [!NOTE] 
> To demonstrate your project adheres to **PRG**, please include the appropriate badge at the top of your repository `README`. See the top of this `README` for an example.

**Resources:**
> [Shields.io](https://shields.io/) - A website for generating badges. <br>
> [GitHub Workflow Status Badge](https://shields.io/badges/git-hub-workflow-status-with-event)

### Divider

A horizontal divider is a great way to separate the top of your `README` from the rest of the content.
Use a divider to separate your `README` into two sections: the _header_ (after the badges and another before the _table of contents_) and the footer section (after the _credits_ but before the _footer_ image).

- e.g. `---------------`

## Title

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.
> The header of "Title" should not be included in your `README`, just the title of your actual project.

- The title should be the name of your project (without underscores or dashes).

## Description

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.
> You do not need to include a header called "Description" for this section, just the description under the title.

- The description should be a short paragraph describing what your project is and what it does after the title.
- This should be the first section after the badges.
    - e.g. "A Python, Django, Plotly, and Pandas web application that visualizes river data pulled using an API from the United States Geological Survey (USGS)."
- Add **screenshots** of your project below the description and throughout the rest of the `README` as needed.
    - This is optional, but highly recommended especially for **Platinum** and **Gold** projects.
    - Animations in the form of GIFs are also a great way to showcase your project.
        - I use [GiFox](https://gifox.io/) to create GIFs of my projects, but you can use any GIF creation software you want.
        - [Snagit](https://www.techsmith.com/screen-capture.html) is another great tool for creating GIFs and screenshots.
        - Both of these tools are paid, but there are plenty of free alternatives out there as well.

## Table of Contents

> [!WARNING] 
> **REQUIRED** section for **Platinum**, **Gold**, and **Silver** tiers.
> **Bronze** tier projects do not require this section, but feel free to add it if you want.

- The table of contents should be a list of links to each section of your `README`.
- This should be the second section after the description.

## Features

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- This section should contain a list of features for your project.
- Explain what each feature does and how it works.
- You can also add screenshots of each feature if you want.

## Background Story

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- The background story should be a short paragraph describing why you created the project and what inspired you to create it.

## Definitions

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of definitions for any terms or acronyms used in your project.

## Getting Started

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- You can break this section down into further subsections if you want (such as below: Dependencies, Configuration, Running Locally, Deployment, etc.).
- Otherwise, you can just include a list of steps to get your project up and running under Getting Started.

### Dependencies

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of dependencies for your project.
- There is no need to list every single dependency, just the major ones.
- There's also no need to list the version or website for each dependency (this will be done in the *Resouces* area, more on that soon), just the name is fine.
    - e.g. This project makes use of several libraries and frameworks: <br>
            - **Python:** For the application logic. <br>
            - **Django:** For web application functionality. <br>
            - **Plotly:** For creating interactive visualizations. <br>
            - **Pandas:** For data manipulation and analysis. <br>
            - **Requests:** For making `API` calls. <br>
            - **Python-Decouple:** For storing sensitive information in a `.env` file. <br>
- You can use a tool like [Dependabot](https://dependabot.com/) to automatically generate a list of dependencies for your project.

**Resources:**
> [Dependabot](https://dependabot.com/) 

### Configuration

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any configuration information for your project here.

### Installation

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of steps to get your project up and running.
- Utilize code blocks to show the commands needed to run your project.
- e.g.
    1. Clone this repository.
    2. Create a virtual environment: `python -m venv venv`.
    3. Install the dependencies.
    4. Run the application: 
        ```bash
        python manage.py runserver
        ```
        
### Deployment

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any deployment information for your project here.

## What's Inside?

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- This section should contain a list of files and folders in your project and what each one does.
- Generally, you should only list the main files and folders in your project, not every single file.
- Use a **tree diagram** to show the relationship between files and folders:
    - e.g.
    ```bash
    ├── README.md # This file.
    ├── config.py # A file that contains sensitive information (excluded from this repository).
    ├── manage.py # A command-line utility that lets you interact with this Django project in various ways.
    ├── requirements.txt # A list of Python packages required to run this project.
    ├── static # A directory for static files that are used in this Django project.
    │   ├── css # A directory for CSS files.
    │   │   └── styles.css # A CSS file that contains the styles for the application.
    │   ├── data # A directory for data files.
    │   │   └── river_charts.csv # A CSV file that contains the float dates for the application.
    │   └── images # A directory for image files.
    ├── templates # A directory for HTML templates.
    │   └── river_charts # A directory for HTML templates specific to the river_charts app.
    │       ├── error.html # An HTML template that displays an error message.
    │       └── index.html # An HTML template that displays the application.
    ├── views.py # A file that contains the application logic.
    ├── VERSION # A file that contains the current version of the application.
    ├── LICENSE # A file that contains the license for this project.
    └── CREDITS # A file that contains the credits for this project.
    ```

- You can use a the following resources below to generate a tree diagram for your project.

**Resources:**
> [An online tree-like utility for generating ASCII folder structure diagrams](https://tree.nathanfriend.io/)
> [Project Tree Generator](https://woochanleee.github.io/project-tree-generator/)
> [ASCII Tree Generator](https://ascii-tree-generator.com/)
> [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=tobiaswadseth.file-tree-generator)

## Closing

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- Add any closing notes or remarks here.

## Limitations

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of limitations for your project.

## Disclaimer

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any disclaimers for your project here.
- e.g. "This project is not affiliated with the United States Geological Survey (USGS)."

## What's Next?

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.

- Include any future plans for your project here.

## Project

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.

- Include a link to your project plan here on GitHub if you do create one.

## Contributing

> [!WARNING] 
> **REQUIRED** section for **Platinum** and **Gold** tiers only.

- GitHub is about collaboration and contribution, so this is why its essential to include a section on how to contribute to your best projects.
- Include any information on how to contribute to your project here.
- Include a `CONTRIBUTING` file in your repository for more detailed information on how to contribute to your project.

## Resources

> [!WARNING] 
> **REQUIRED** section for **Platinum**, **Gold**, and **Silver** tiers.
> **Bronze** tier projects do not require this section, but feel free to add it if you want.

- This section should contain a list of resources used to create your project.
- Include the name of the resource, a link to the resource, and a short description of what the resource is.
    - e.g. [Plotly](https://plotly.com/python/) - A Python graphing library that makes interactive, publication-quality graphs online.
    - e.g. [Django](https://www.djangoproject.com/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
    - e.g. [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

## License

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- Describe the license for your project here.
- I found it helpful to break down what license I choose based on the **PRG** tier of the project:
    - **Platinum** - GNU GPLv3 or No License (if you want to keep your code private)
    - **Gold** - GNU GPLv3
    - **Silver** - MIT
    - **Bronze** - The Unlicense
- I chose [GNU GPLv3](../templates/license_examples/GNU/LICENSE) for my **Platinum** and **Gold** projects.
    - Why? I spent a lot of time on my **Platinum** and **Gold** projects and I want to protect my work as much as possible.
    - I do not want people to use my code to profit off of it without my permission which is why I chose this more restrictive license.
- I chose [MIT](../templates/license_examples/MIT/LICENSE) for my **Silver** projects.
    - Why? I put more work into my **Silver** projects than my **Bronze** projects, so I want to protect my work a little more but still allow people to use my code in their own projects by giving me credit for it.
- I chose [The Unlicense](../templates/license_examples/Unlicense/LICENSE) for my **Bronze** projects.
    - Why? Because I want to encourage people to use my code in their own projects, even if they don't give me credit for it.
- Include a `LICENSE` file in your repository for more detailed information on the license for your project.
- The above licenses are the licenses I chose for my projects, but you can choose whatever license you want for your projects.
- A list of licenses can be found [here](https://choosealicense.com/licenses/).

## Footer

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- The footer consists of two parts: the Credits and the Footer Icon.
- This should be the **last** section of your `README`.

### Credits

- Include a credit block for each person who contributed to your project.
- If you worked on the project by yourself, you can just include your name and other details such as:
    - Author: - Your name + a link to your GitHub profile.
    - Email: - Your email + a link to your email.
    - Website: - Your website + a link to your website.
    - Reference: - Main Branch + a link to the main branch of your repository.
- Include a `CREDITS` file in your repository for more detailed information on the credits for your project.

### Footer Icon

- The footer icon  should contain a image of your application's icon (never a banner) for all tier projects.
- The footer icon should also be a centered clickable image link to your personal website, GitHub profile, or main repo branch for said project.
- Above the footer icon, you should include a [divider](#divider) to separate the footer icon from the rest of the `README`. 
    - e.g. `---------------`
- See the [bottom of this project README](../README.md#credits) for an example.

---------------

## Resources

**General Resources:**
- [About READMEs](https://help.github.com/articles/about-readmes/) - GitHub Docs on READMEs.
- [Creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository#creating-a-template-repository) - GitHub Docs on creating a template repository.
- [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) - GitHub Docs on creating a repository from a template.
- [Managing project templates in your organization](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization) - GitHub Docs on managing project templates in your organization.
- [Managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme) - GitHub Docs on managing your profile README.
- [Organization README](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Getting started with writing and formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) - GitHub documentation on writing and formatting.
- [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github) - Learn advanced formatting features by creating a README for your GitHub profile.
- [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) - Create sophisticated formatting for your prose and code on GitHub with simple syntax.
- [Building a Useful, User-Friendly Project](https://github.com/zalando/zalando-howto-open-source/blob/master/producttemplate.md) - Great project advice.

**General README Information:**
- [Art of README](https://github.com/hackergrrl/art-of-readme) - A collection of advice for creating READMEs.
- [Make a README](https://www.makeareadme.com/) - A guide to writing READMEs.
- [Awesome README](https://github.com/matiassingers/awesome-readme) - A curated list of awesome READMEs.
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme) - A curated list of awesome GitHub Profile READMEs.
- [README Inspiration](https://github.com/LappleApple/feedmereadmes/blob/master/Inspiration.md) - A list of articles and resources to inspire your README.
- [README Best Practices](https://github.com/jehna/readme-best-practices) - A list of best practices for README files.

**README Generators:**
- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/) - A tool that generates GitHub profile READMEs.
- [Online README Editor](https://readme.so/) - A WYSIWYG editor for creating READMEs.
- [user-statistician](https://github.com/cicirello/user-statistician) - Generate a GitHub stats SVG for your GitHub Profile README in GitHub Actions

**Open Source README Templates:**
- [An awesome README template to jumpstart your projects!](https://github.com/othneildrew/Best-README-Template)
- [A Beginners Guide to writing a README](https://gist.github.com/akashnimare/7b065c12d9750578de8e705fb4771d2f)
- [A template to make good README.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
- [A simple README.md template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
- [README.md template for your open-source project](https://github.com/dbader/readme-template)
- [Suggested README file structure for software projects](https://github.com/mhucka/readmine)
- [A standard style for README files](https://github.com/RichardLitt/standard-readme)
- [A README template to encourage open-source contributions](https://github.com/davidbgk/open-source-template/)
- [Open Source guidance from Zalando, Europe's largest online fashion platform](https://github.com/zalando/zalando-howto-open-source/tree/master)

**Markdown:**
- [Basic Syntax | Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [GitHub Flavor Markdown](https://github.github.com/gfm)
- [StackEdit | In-Browser Markdown Editor](https://stackedit.io/)
- [Comments in Markdown](https://stackoverflow.com/questions/4823468/comments-in-markdown)
- [GitHub Markdown Alerts](https://github.com/orgs/community/discussions/16925)
- [Spelling Checker for Visual Studio Code](https://gist.github.com/d2s/927d539268ee219c7ad04da6f5bc813b)
