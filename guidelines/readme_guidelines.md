<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="../docs/images/icon_2-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">README Guidelines</h1>

General guidelines for creating a `README` file for your project (specifically for **PRG** projects) but this can be applied to any project.

## README File

> [!WARNING]
> A `README` file is **REQUIRED** for **ALL** tiers.

> [!NOTE]
> Your Profile `README` does not need to adhere to the **PRG** guidelines defined in this document, but it is encouraged to include the [Profile Badge](../README.md#6236ff-profile-badge) to link to your **PRG** project collection.

- A Profile `README` is always required. Read more about it [here](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).
    - View [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/) for a quick and easy way to generate a profile `README` for your GitHub profile.
    - Use the templates in the next section as a starting point for your profile `README` (espcially if you're using **PRG**).

*Below is a descrption of each section of the `README` and what it should contain.*

> [!NOTE]  
> I only mentioned the important parts of a `README` file, there are many other things you can add to your `README` file that I didn't mention here. Feel free to add whatever you want to your `README` file including new sections, images, GIFs, etc.

### Templates

For templates and examples of `README files`, see the [templates](../templates) directory.
Templates are broken down by the three categorized tiers of projects: **Gold**, **Silver**, and **Bronze**.

See the following links for `README` templates for each tier:
- [Gold Tier README Template](../templates/README_gold.md)
- [Silver Tier README Template](../templates/README_silver.md)
- [Bronze Tier README Template](../templates/README_bronze.md)

## Banner

> [!WARNING] 
> **REQUIRED** section for **Gold** tier only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want (or a logo of the technology you used to develop your project).

- The banner should be a custom design created to represent your project.
- I use [Sketch](https://www.sketch.com/) to create my banners and designs, but you can use any design software you want.
- See [PRG Brand Guidelines](brand_guidelines.md) for more information on creating banners and other graphics for your project.
- **Silver** projects don't require a banner, but feel free to add a logo of the technology you used to develop your project.
    - i.e. Svelte + Firebase Logos <br>
    <img src="./docs/images/demo/svelte_logo.png" alt="Svelte" style="width: 5%; vertical-align: left;" />
    <img src="./docs/images/demo/plus-dark.png#gh-dark-mode-only" alt="+" style="width: 5%;vertical-align: left;"/>
    <img src="./docs/images/demo/plus-light.png#gh-light-mode-only" alt="+" style="width: 5%; vertical-align: left;" />
    <img src="./docs/images/demo/firebase_logo.png" alt="Firebase" style="width: 5%; vertical-align: left;" />

> [!NOTE]  
> Append `#gh-dark-mode-only` or `#gh-light-mode-only` to the end of the image URL to only show the image in dark or light mode respectively. Be sure to have both a dark and light version of the image when necessary. More on this (shameless plug) [here](https://github.com/scottgriv/markdown-demo#images).

## Badges

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- Badges are a great way to showcase the technologies, frameworks, and languages used in your project. 
- Badges are generated using [Shields.io](https://shields.io/).
- You should include all major technologies, frameworks, and languages used in your project (one badge per technology). This badge should contain the technology name and version you used to develop your project.
    - i.e. [![Python Badge](https://img.shields.io/badge/Python-3.8.5-244C6F?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-385/)
    - i.e. [![Node.js Badge](https://img.shields.io/badge/Node.js-16.13.2-036E02?style=for-the-badge&logo=node.js)](https://nodejs.org/en/)
- The badge color should match the color of the technology's logo. Use a browser extension like [ColorZilla](https://www.colorzilla.com/) to get the exact color code of a logo from a website.
- The badge should hyperlink to the technology's website or version release page (whatever you think is more appropriate).
- Optionally you can add badges for your email, website, and GitHub profile so people can contact you or follow you. You can also add a link to your [BuyMeACoffee](https://www.buymeacoffee.com/) page if you have one to support your work.
    - i.e. [![Email Badge](https://img.shields.io/badge/gmail-contact_me-DC4233?style=for-the-badge&logo=gmail)](mailto:scott.grivner@gmail.com)
    - i.e. [![GitHub Badge](https://img.shields.io/badge/github-follow-9031AC?style=for-the-badge&logo=github&color=9031AC)](https://github.com/scottgriv)
    - i.e. [![BuyMeACoffee Badge](https://img.shields.io/badge/buy_me_a_coffee-support_me-FEDE1F?style=for-the-badge&logo=buymeacoffee&color=FEDE1F)](https://www.buymeacoffee.com/scottgriv)
- Next, add a horizontal rule to separate the badges from the rest of the `README`.
    - i.e. `---`

> [!NOTE] 
> To demonstrate your project adheres to **PRG**, please include the appropriate badge at the top of your repository `README`. See the top of this `README` for an example.

## Title

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- The title should be the name of your project (without underscores or dashes).

## Description

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- The description should be a short paragraph describing what your project is and what it does.
- This should be the first section after the badges.
    - i.e. "A Python, Django, Plotly, and Pandas web application that visualizes river data pulled using an API from the United States Geological Survey (USGS)."
- Add **screenshots** of your project below the description and throughout the rest of the `README` as needed.
    - This is optional, but highly recommended especially for **Gold** projects.
    - Animations in the form of GIFs are also a great way to showcase your project.
        - I use [GiFox](https://gifox.io/) to create GIFs of my projects, but you can use any GIF creation software you want.
        - [Snagit](https://www.techsmith.com/screen-capture.html) is another great tool for creating GIFs and screenshots.
        - Both of these tools are paid, but there are plenty of free alternatives out there as well.

## Table of Contents

> [!WARNING] 
> **REQUIRED** section for **Gold** and **Silver** tiers.
> **Bronze** tier projects do not require this section, but feel free to add it if you want.

- The table of contents should be a list of links to each section of your `README`.
- This should be the second section after the description.

## Background Story

> [!WARNING] 
> **REQUIRED** section for **Gold** tier only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- The background story should be a short paragraph describing why you created the project and what inspired you to create it.

## Definitions

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of definitions for any terms or acronyms used in your project.

## Limitations

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of limitations for your project.

## Features

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of features for your project.
- Explain what each feature does and how it works.
- You can also add screenshots of each feature if you want.

## What's Inside?

> [!WARNING] 
> **REQUIRED** section for **Gold** tier only.
> **Silver** and **Bronze** tier projects do not require this section, but feel free to add it if you want.

- This section should contain a list of files and folders in your project and what each one does.
- Generally, you should only list the main files and folders in your project, not every single file.
- Use a **tree diagram** to show the relationship between files and folders:
    -i.e. 
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
    - You can use a the following tools to generate a tree diagram for your project:
        - [tree.nathanfriend.io](https://tree.nathanfriend.io/)
        - [woochanleee.github.io](https://woochanleee.github.io/project-tree-generator/)
        - [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=tobiaswadseth.file-tree-generator)

## Dependencies

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- This section should contain a list of dependencies for your project.
- There is no need to list every single dependency, just the major ones.
- There's also no need to list the version or website for each dependency (this will be done in the *Resouces* area, more on that soon), just the name is fine.
    - i.e. This project makes use of several libraries and frameworks: <br>
            - **Python:** For the application logic. <br>
            - **Django:** For web application functionality. <br>
            - **Plotly:** For creating interactive visualizations. <br>
            - **Pandas:** For data manipulation and analysis. <br>
            - **Requests:** For making `API` calls. <br>
            - **Python-Decouple:** For storing sensitive information in a `.env` file. <br>
- You can use a tool like [Dependabot](https://dependabot.com/) to automatically generate a list of dependencies for your project.

## Getting Started

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- This section should contain a list of steps to get your project up and running.
- Utilize code blocks to show the commands needed to run your project.
- i.e.
    1. Clone this repository.
    2. Create a virtual environment: `python -m venv venv`.
    3. Install the dependencies.
    4. Run the application: 
        ```bash
        python manage.py runserver
        ```
## Configuration

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any configuration information for your project here.

## Deployment

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any deployment information for your project here.

## Closing

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Add any closing notes or remarks here.

## Disclaimer

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any disclaimers for your project here.
- i.e. "This project is not affiliated with the United States Geological Survey (USGS)."

## Resources

> [!WARNING] 
> **REQUIRED** section for **Gold** and **Silver** tiers.
> **Bronze** tier projects do not require this section, but feel free to add it if you want.

- This section should contain a list of resources used to create your project.
- Include the name of the resource, a link to the resource, and a short description of what the resource is.
    - i.e. [Plotly](https://plotly.com/python/) - A Python graphing library that makes interactive, publication-quality graphs online.
    - i.e. [Django](https://www.djangoproject.com/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
    - i.e. [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

## What's Next?

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any future plans for your project here.

## Project

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include a link to your project plan here on GitHub if you do create one.

## Contributing

> [!WARNING] 
> **OPTIONAL** section for **ALL** tiers.

- Include any information on how to contribute to your project here.
- Include a `CONTRIBUTING` file in your repository for more detailed information on how to contribute to your project.

## License

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- Describe the license for your project here.
- I found it helpful to break down what license I choose based on the **PRG** tier of the project:
    - **Gold** - GNU GPLv3
    - **Silver** - MIT
    - **Bronze** - The Unlicense
- I chose [GNU GPLv3](../templates/license_examples/GNU/LICENSE) for my **Gold** projects.
    - Why? I spent a lot of time on my **Gold** projects and I want to protect my work as much as possible.
    - I do not want people to use my code to profit off of it without my permission which is why I chose this more restrictive license.
- I chose [MIT](../templates/license_examples/MIT/LICENSE) for my **Silver** projects.
    - Why? I put more work into my **Silver** projects than my **Bronze** projects, so I want to protect my work a little more but still allow people to use my code in their own projects by giving me credit for it.
- I chose [The Unlicense](../templates/license_examples/Unlicense/LICENSE) for my **Bronze** projects.
    - Why? Because I want to encourage people to use my code in their own projects, even if they don't give me credit for it.
- Include a `LICENSE` file in your repository for more detailed information on the license for your project.
- The above licenses are the licenses I chose for my projects, but you can choose whatever license you want for your projects.
- A list of licenses can be found [here](https://choosealicense.com/licenses/).

## Credits

> [!WARNING] 
> **REQUIRED** section for **ALL** tiers.

- Include a credit block for each person who contributed to your project.
- If you worked on the project by yourself, you can just include your name and other details such as:
    - Author: - your name.
    - Email: - A link to your email.
    - Website: - A link to your website.
    - Reference: - A link to the main branch of your repository.
- Include a `CREDITS` file in your repository for more detailed information on the credits for your project.

## Footer

> [!WARNING] 
> **REQUIRED** section for **Gold** tier only.
> If you have a personal brand logo, you can add it here for **Silver** and **Bronze** tier projects.

- The footer should contain a image of your application's icon.
- See the [bottom of this project README](../README.md#credits) for an example.