<!-- Begin README -->

[![Banner Large](./docs/images/banner_large.png)](https://github.com/scottgriv/PRG-Personal-Repository-Guidelines)

<p align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines">
        <img src="https://img.shields.io/badge/PRG-1.0.0-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="PRG Badge" />
    </a>
    <a href="https://github.github.com/gfm/">
        <img src="https://img.shields.io/badge/GFMarkdown-0.29-093FA1?style=for-the-badge&logo=markdown" alt="Markdown Badge" />
    </a>
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines/blob/main/guides/project_tier_table.md">
        <img src="https://img.shields.io/badge/PRG-Gold Project-FFD700?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkQ3MDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="Gold PRG Badge" />
    </a>
    <br>
        <a href="https://github.com/scottgriv">
        <img src="https://img.shields.io/badge/github-follow-9031AC?style=for-the-badge&logo=github&color=9031AC" alt="GitHub Badge" />
    </a>
    <a href="mailto:scott.grivner@gmail.com">
        <img src="https://img.shields.io/badge/gmail-contact me-DC4233?style=for-the-badge&logo=gmail" alt="Email Badge" />
    </a>
    <a href="https://www.buymeacoffee.com/scottgriv">
        <img src="https://img.shields.io/badge/buy me a coffee-support me-FEDE1F?style=for-the-badge&logo=buymeacoffee&color=FEDE1F" alt="BuyMeACoffee Badge" />
    </a>
</p>

---

<h1 align="center">Personal Repository Guidelines (PRG)</h1>

**PRG** is a robust repository categorization, guideline, and template system developed to help you standardize and develop repositories for your projects, `README`'s, and overall repository structure.
- Get your projects up and running quickly and easily so you can focus on what matters most - your project and your code!
- Categorize repositories and projects for your **GitHub Portfolio**.
- Define guidelines and templates for repository `README`'s and files.

---

This `README` highlights the **three** main areas of **PRG**:
1. **Categories**: categorize your repositories into three tiers: ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold**, ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver**, and ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze** then display them in a "project tier table" (built using GitHub Actions).
2. **Guidelines**: defined guidelines for repository `README`, files, and overall structure. Brand guidelines for your ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold** tier projects are also defined.
3. **Templates**: templates for your `README`'s and associated files.
*Each section will have hyperlinks to the appropriate files and folders in this repository for more details.*

## Table of Contents

- [Background Story](#background-story)
    - ["The GitHub Portfolio Problem"](#the-github-portfolio-problem)
- [1. Categories](#1-categories)
    - [Repository Tiers and Naming Conventions](#repository-tiers-and-naming-conventions)
        - [Gold Tier](#gold-tier)
        - [Silver Tier](#silver-tier)
        - [Bronze Tier](#bronze-tier)
    - [Project Tier Table](#project-tier-table)
    - [Project Tier Badges](#project-tier-badges)
- [2. Guidelines](#2-guidelines)
    - [Repository Settings Guidelines)](#repository-settings-guidelines)
    - [README Guidelines](#readme-guidelines)
    - [Repository Structure](#repository-structure-guidelines)
    - [Brand Guidelines](#brand-guidelines)
- [3. Templates](#3-templates)
    - [Tier README Templates](#tier-readme-templates)
- [What's Inside?](#whats-inside)
- [Closing](#closing)
- [Resources](#resources)
- [What's Next?](#whats-next)
- [Project](#project)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Background Story

I needed a system to showcase my GitHub portfolio and keep it organized and standardized. My repository README and folder/file structures were different from each other, which was a pain to maintain or use as a template for a future projects, so I created this repository and document, the <u><b>Personal Repository Guidelines</b></u> or **PRG** for short, to help solve my problem. 
- This document primarily applies to the version control system here on *GitHub* but it can be extended or applied to other version control systems as well. 
- [This](#) repository is treated no different than my other repositories, it also adheres to **PRG** (itself in this case). 

### "The GitHub Portfolio Problem"

Another reason I created this document was to solve the "GitHub Portfolio Problem" (as I like to call it):
> GitHub is being used to showcase my portfolio, but I don't want to showcase every single repository I have created. I want to showcase my best work, but I also want to showcase my other work that I am proud of. How do I do that?

***PRG** was designed to solve this problem.*

## What's Inside?

Below is a list of the files and folders in this repository and what they are used for:
    
    ├── .github
    │   └── workflows
    │       └── project_tier_table.yml
    ├── docs
    │   ├── api
    │   └── images
    ├── guides
    │   ├── brand_guidelines.md
    │   ├── readme_guidelines.md
    │   ├── repository_structure_guidelines.md
    │   └── repository_settings_guidelines.md
    ├── scripts
    │   └── build_project_tier_table.py
    ├── templates
    │   ├── gold_tier_readme_template.md
    │   ├── silver_tier_readme_template.md
    │   ├── bronze_tier_readme_template.md
    │   └── badge_reference_template.md
    ├── .gitignore
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── .gitattributes
    └── PRG.md

## Getting Started

To get started, you can fork this repository and adjust the guidelines to fit your own needs, this was designed to be a template above all else. If you decide to fork it and make changes to it, please provide proper credit by linking back to the main branch of this repository! Thank you!

## 1. Categories

To solve the "GitHub Portfolio Problem" above, **PRG** categorizes repositories into three tiers: ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold**, ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver**, and ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze** to destinguish the quality of the project. It does this by utilizing GitHub Actions to automatically create a project tier table based on a simple markdown file placed in each of your repositories.

### Repository Tiers and Naming Conventions

- There are <u>three</u> tiers to describe repository projects under **PRG** collection.
- The tier is **required** to be added to the top of each repository to conform to **PRG**.
- This is what links your repository to the guidelines and helps categorize it.

#### ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) Gold Tier

<a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines">
    <img src="https://img.shields.io/badge/PRG-Gold Project-FFD700?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkQ3MDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="Gold PRG Badge" />
</a>
<br>

- 10+ hours of work to complete the project.
- These are the best open-sourced projects you have completed in your repository collection.
- These repositories can be used in a business/real-world environment. 
- These are considered actual **products** and more than a demo or example "Hello World" repo.
- These repositories should have their own graphic designs and brands/app icons.
- The naming scheme that will be followed for this project tier is: 
	- `Application-Brand-Name`
	- i.e. [River-Charts](https://github.com/scottgriv/River-Charts)

#### Gold Repo Additional Requirements
- Use **upper** case letters for the first letter of each word in the project name.
- Use dashes `-` to separate words or apply spaces in the project name.
- The name should be "catchy" and easy to remember, but also descriptive of what the project is (which is why coming up with a brand for your project is important).

#### ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) Silver Tier

<a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines">
    <img src="https://img.shields.io/badge/PRG-Silver Project-C0C0C0?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDMEMwQzAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="Silver PRG Badge" />
</a>
<br>

- 2-10 hours of work to complete the project.
- These are fully functional projects, but are not quite as developed to make it an actual product. 
- The naming scheme that will be followed for this project tier is: 
	- `technology/framework/language-project_name`
	- i.e. [java-backsplash_tile_square_footage_calculator](https://github.com/scottgriv/java-backsplash_tile_square_footage_calculator)
    - i.e. [angular-github_user_info](https://github.com/scottgriv/angular-github_user_info)
    
#### ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) Bronze Tier 

<a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines">
    <img src="https://img.shields.io/badge/PRG-Bronze Project-CD7F32?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDRDdGMzIiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="Bronze PRG Badge" />
</a>
<br>

- 0-2 hours of work to complete the project.
- These repositories are projects I made to learn or understand a specific technology better (language, framework, technology, principle, etc.).
- The naming scheme that will be followed for this project tier is the same as `Silver` above, which is:
	- `technology/framework/language-project_name`
    - i.e. [csharp-nunit_test_demo](https://github.com/scottgriv/csharp-nunit_test_demo)
    - i.e. [rust-json_note_manager](https://github.com/scottgriv/rust-json_note_manager) 
    - i.e. [python-convert_html_table_to_csv](https://github.com/scottgriv/python-convert_html_table_to_csv)

#### Silver & Bronze Additional Requirements 
- If you have multiple languages or technologies you want to highlight, you can use the following naming scheme: language-language-language-project_name`
    - i.e. [json-xml-yaml-portfolio_template](https://github.com/scottgriv/json-xml-yaml-portfolio_template)
- Use **lower** case letters for the first letter of each word in the project name.
- Use underscores `_` to separate words in the project name.
- Use dashesa `-` to separate each language/technology.
- The languages/technologies don't necessarily have to be in any particular order, but I would recommend putting the most important one first.
- View the [Badge References](./categories/badge_references.md) file for more details on how to create badges for your repository. 
- By default, (and this goes without saying) forked repositories will not have the `PRG Connection File`, so make sure you add it to your forked repository:
    - If you forked the repository without making any changes, by default the repo will be considered a ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze** tier.
    - If you make significant changes to the repository, you can consider it a ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver** tier.
    - Because you did not originate the work, a forked repo can only be considered a ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze** or ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver** tier, never ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold**.

#### ![#6236FF](https://via.placeholder.com/15/6236FF/000000?text=+) PRG Profile Badge

- I won't say this is *required*, because I don't want to tell you what to do with your personal profile `README`, but I strongly encourage adding one of thw two following badges to your main "About Me" profile `README` to showcase your **PRG** tier collection (this is the essence of fixing the "GitHub Portfolio Problem" I mentioned earlier):

<a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines/blob/main/categories/project_tier_table.md">
    <img src="https://img.shields.io/badge/PRG-Optimized-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=" alt="PRG Badge" />
</a>

**OR**

<a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines/blob/main/categories/project_tier_table.md" target="_blank">
    <img src="docs/images/prg_optimized.png" alt="PRG Optimized Logo" width="138" height="51"/>
</a>

- This will link to your `project_tier_table.md` file in your forked repository to showcase all of your repositories under *PRG*. 
- The tier badges on your repositories will also link to this file.

> [!IMPORTANT] 
> Make sure you run the GitHub action workflow to replace the projects in the table with your own.
> Running the workflow will output badges with your username as a hyperlink in the [Badge References](./categories/badge_references.md) file.
> If you choose to not run the Action, make sure you change the username in the badge to your own to link to your forked repositories Project Tier Table if you choose to not use the Action.

### Project Tier Table

Included in this project is a GitHub Action that will automatically generate a table of all your repositories and their tiers using GitHub Actions.
- The script is located in the `.github/workflows` folder called `project_tier_table.yml`.
- The workflow will call `scripts/build_project_tier_table.py` which will build the table and output it to `docs/project_tier_table.md`.
- The script will run on a weekly basis.
- See the [Project Tier Table](/categories/project_tier_table.md) for an output of what the table looks like.
- The script will also update the [Badge References](./categories/badge_references.md) file with the latest badges for your repository under your GitHub username.

#### Pre-requisites

1. In each repository, inside the root project folder, there should be a markdown file called `PRG.md`. 
    - The GitHub Action Workflow (explained below) uses this file to categorize your repositories.
    - You must have a `Repository Tier` label for each repository for the categorization to work.
        - Change the repository's `Tier` label to match the tier of the repository (![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold**, ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver**, and ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze**).
    - There are optioanl labels you can add to your repository as well: `Technology`, `Category`, and `Order`.
    - See the PRG Tier file used in this repo, [here](PRG.md), for an example and more information on how to use it.
2. Also, each repository should have a `docs/` folder in the root of the project.
    - Inside the `docs/` folder, there should be a subfolder called `images/`.
    - Inside the `images/` folder, there should be a file called `icon-rounded.png`.
    - This is the icon that will be used for the project tier table.
        - See the PRG Tier file used in this repo, [here](/docs/images/icon-rounded.png), for an example.
        - See [Brand Guidelines](/guides/brand_guidelines.md) for more details on how to create your own icon.

> [!NOTE] 
> You can reference your built project tier table in your repository `README` or wherever you see fit.
> This can be helpful showcasing your projects using the PRG system.

#### Setting up the Workflow

1. Fork this repository.
2. Go to your forked repository and click on the `Actions` tab.
3. Click on the `Set up a workflow yourself` button.
4. Add the `PRG Connection File` to your repository.
    - Click on the `Add file` button and select `Create new file`.
    - Name the file `PRG.md`.
    - Copy the contents of the [PRG Tier](PRG.md) file in this repository and paste it into your new `PRG.md` file.
    - Commit the file to your repository.

### Project Tier Badges

See [Badge References](./categories/badge_references.md) for more details on how to create badges for your repository.
- Run the workflow above to get an update `badge_references.md` file pointing to your **PRG** system.

## 2. Guidelines

Below are the guidelines for repository `README`'s, files, and overall structure. This applies to **all** tiers.

### Repository Settings Guidelines

See [Repository Settings](./guides/repository_settings_guidelines.md) for more details on how to configure your repository settings.

### README Guidelines

See [README Guidelies](./guides/readme_guidelines.md) for more details on how to structure your repository `README`.

### Repository Structure Guidelines

See [Project Structures](./guides/repository_structure_guidelines.md) for more details on how to structure your overall repository/files.

### Brand Guidelines

See [Brand Guidelines](./guides/brand_guidelines.md) for more details on how to create your own brand for your project.

## 3. Templates

The following templates are provided for you to use in your repositories. These templates are designed to be used with the **PRG** system.

### Tier README Templates

For templates and examples of `README files`, see the [templates](../templates) directory.
Templates are broken down by the three tiers of projects: ![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+) **Gold**, ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) **Silver**, and ![#CD7F32](https://via.placeholder.com/15/CD7F32/000000?text=+) **Bronze**.

See the following links for `README` templates for each tier:
- [Gold Tier README Template](../templates/README_gold.md)
- [Silver Tier README Template](../templates/README_silver.md)
- [Bronze Tier README Template](../templates/README_bronze.md)

## Closing

Thank you for taking the time to read through this document and I hope you find it useful!
If you have any questions or suggestions, please feel free to reach out to me.

## Resources

Below are some resources I found helpful when creating my repositories and **PRG** in general:
- [GitHub Docs](https://docs.github.com/en)
- [GitHub Docs - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## What's Next?

- [ ] Conform all repositories to **PRG**.

I'm looking forward to seeing how this project evolves over time and how it can help others with their GitHub portfolio.
- Please reference the [CHANGELOG](CHANGELOG.md) file in this repository for more details.

## Project

Please reference the [GitHub Project](https://github.com/users/scottgriv/projects/8) tab inside this Repo to get a good understanding of where I'm currently at with the overall project. 
- Issues and Enhancements will also be tracked there as well.

## Contributing

Feel free to submit a pull request if you find any issues or have any suggestions on how to improve this project. You can also open an issue with the tag "bug" or "enhancement".
- How to contribute:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/PRG-Personal-Repository-Guidelines`)
3. Commit your Changes (`git commit -m 'Add new feature'`)
4. Push to the Branch (`git push origin feature/PRG-Personal-Repository-Guidelines`)
5. Open a Pull Request
- Please reference the [CONTRIBUTING](CONTRIBUTING.md) file in this repository for more details.

## License

This project is released under the terms of the **GNU General Public License, version 3 (GPLv3)**. 
- The GPLv3 is a "copyleft" license, ensuring that derivatives of the software remain open source and under the GPL.
- For more details and to understand all requirements and conditions, see the [LICENSE](LICENSE) file in this repository.

## Credits

**Author:** Scott Grivner <br>
**Email:** scott.grivner@gmail.com <br>
**Website:** [scottgrivner.dev](https://www.scottgrivner.dev) <br>
**Reference:** [Main Branch](https://github.com/scottgriv/PRG-Personal-Repository-Guidelines) <br>
<div align="center">
    <a href="https://github.com/scottgriv/PRG-Personal-Repository-Guidelines" target="_blank">
        <img src="./docs/images/icon-rounded.png" width="100" height="100"/>
    </a>
</div>

<!-- End README -->
