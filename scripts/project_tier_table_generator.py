import os
import requests
import base64
import sys
import traceback
import re
from datetime import datetime
import pytz

# Local Testing Flag:
LOCAL_TESTING = False # Set to True if you want to test locally, False if you want to deploy using GitHub Actions

print(f"Local Testing?: {LOCAL_TESTING}")

# Local (Test/Development)
if LOCAL_TESTING:
    path_start = '..' # Path Start
    GITHUB_TOKEN = '' # Add your API token here (WARNING: MAKE SURE YOU REMOVE YOUR ACCESS TOKEN PRIOR TO COMMITTING TO GITHUB)
    USERNAME = '' # Add your username here
# GitHub Actions (Production)
else:
    path_start = '.' # Path Start
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '') # Access Token used for GitHub Actions (Repository secret variable)
    USERNAME = os.environ.get('GITHUB_ACTOR', 'default_username') # Used for GitHub Actions (Repository secret variable)

print(f"GitHub Username: {USERNAME}")

# GitHub token for API requests
if GITHUB_TOKEN is None:
    print("GitHub token is not set. Set the GITHUB_TOKEN environment variable.")
    sys.exit(1)

# Required Configurations - PRG Portfolio URL, and Timezone:
PRG_REPO_URL = f'https://github.com/scottgriv/PRG-Personal-Repository-Guidelines' # URL to the PRG repo (you can use your own fork if you want or the main repo)
TIER_TABLE_URL = f'https://prgportfolio.com' # URL to the project tier table using GitHub Pages (update this if you're using a custom domain)
MY_TIME_ZONE = 'America/New_York' # Your timezone (used for the last updated timestamp) for local testing, otherwise it will use an environment variable for GitHub Actions.
# For a list of timezones: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

# Optional Configurations - File Paths:
MD_FILE_PATH = f'{path_start}/categories/project_tier_table.md' # Path to the the main project tier table markdown file
MD_FILE_PATH_PRIVATE = f'{path_start}/categories/project_tier_table_private.md' # Path to the private project tier table markdown file
MD_BADGE_REF_PATH = f'{path_start}/categories/badge_reference_guide.md' # Path to the badge reference guide markdown file
PLACEHOLDER_ICON = f'{path_start}/docs/images/prg-placeholder.png' # Placeholder for missing icons
PRIVATE_REPO_ICON_DIR = f'{path_start}/docs/images/private_repos' # Path to the private repo icons from your root directory of your repository (don't adjust for local testing)
PROJECT_ICON_PATH = 'docs/images/PRG.png' # Path to the project icon from the root directory of your repositories (don't adjust for local testing) 

# Tip: 
# Private repo icons cannot be reached by users that are not logged in to GitHub and have access to the private repo.
# Therefore, the best way to show private repos with icons is to add them to your private markdown file, an image in the docs/images/private_repos dirextory, + don't add a PRG.md file to the repo.
# In the future, I may add a feature to allow you to add a custom icon for private repo in the private_repos folder and pick up the image from there to solve this problem instead of adding it to the private markdown file which can be used for other things (Future Enhancement).

# Configuration Flags:
# General PRG Configurations:
INCLUDE_PRG_FILE_PROJECTS = True  # Set to False if you want to include projects that don't have a PRG file
INCLUDE_PRIVATE_FILE_PROJECTS = False  # Set to False if you want to exclude projects that are in the private project tier table markdown file
MD_ONLY_TIER_TABLE = False  # Set to True if you only want to display the tier table in the markdown file and you don't plan on hosting it on GitHub Pages

# Personal Repo Configurations:
INCLUDE_PRIVATE_REPOS = True  # Set to False if you don't want to include private repos
INCLUDE_FORKS = True  # Set to False if you don't want to include forked repos

## Organizational Repo Configurations:
INCLUDE_ORG_REPOS = True  # Set to False if you don't want to include org repos
INCLUDE_ORG_PRIVATE_REPOS = True  # Set to False if you don't want to include private org repos (requires INCLUDE_ORG_REPOS to be True)
INCLUDE_ORG_FORKS = True  # Set to False if you don't want to include forked org repos (requires INCLUDE_ORG_REPOS to be True)

# Misc Configurations:
# EXCLUDE_REPOS_LIST = []  # List of repos to be exclude from the project tier table output (Future Enhancement). Example: ['repo1', 'repo2']

# Tip: 
# If, for some reason, you want to exclude public projects and only include private projects:
# set the INCLUDE_PRIVATE_FILE_PROJECTS flag to True 
# and set the INCLUDE_PRG_FILE_PROJECTS to False (and don't add PRG.md files to your public projects)

# Badges URLs:
BADGES = {
    'Platinum': 'https://img.shields.io/badge/PRG-Platinum Project-E5E4E2?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNFNUU0RTIiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Gold': 'https://img.shields.io/badge/PRG-Gold Project-FFD700?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkQ3MDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Silver': 'https://img.shields.io/badge/PRG-Silver Project-C0C0C0?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDMEMwQzAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Bronze': 'https://img.shields.io/badge/PRG-Bronze Project-CD7F32?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDRDdGMzIiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Optimized': 'https://img.shields.io/badge/PRG-Optimized-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Purple': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiM2MjM2RkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Black': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiMwMDAwMDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'White': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Purple_Collection': 'https://img.shields.io/badge/PRG-Collection-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiM2MjM2RkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Black_Collection': 'https://img.shields.io/badge/PRG-Collection-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiMwMDAwMDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'White_Collection': 'https://img.shields.io/badge/PRG-Collection-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
}

# Function to create markdown with user-specific links
def create_repo_badges(username):

    repo_badge_template = f"""

<div align="center">
    <a href="{PRG_REPO_URL}" target="_blank">
        <img src="../docs/images/icon_2-rounded.png" width="200" height="200"/>
    </a>
</div>

<h1 align="center">Badge Reference Guide</h1>

Utilize this file as a template for collecting and incorporating badges into your project `README` files.
- Execute the GitHub action workflow to automatically modify badge links, directing them to your **PRG Portfolios's** website/domain.
- Before initiating the workflow, ensure you update the `TIER_TABLE_URL` parameter in the `project_tier_table_generator.py` script.

---------------

## Table of Contents
- [Tier Badges](#tier-badges)
    - [Platinum Tier Project Badge](#platinum-tier-project-badge)
    - [Gold Tier Project Badge](#gold-tier-project-badge)
    - [Silver Tier Project Badge](#silver-tier-project-badge)
    - [Bronze Tier Project Badge](#bronze-tier-project-badge)
    - [Optimized Tier Project Badge](#optimized-tier-project-badge)
- [Profile Badges](#profile-badges)
    - [PRG Collection Badge (Optimized) (Default)](#prg-collection-badge)
    - [PRG Collection Badge (Collection)](#prg-collection-badge-collection)
    - [PRG Collection Badge (Portfolio)](#prg-collection-badge-collection)
- [Alternative Profile Badges](#alternative-profile-badges)
    - [PRG Collection Badge (Purple Book)](#prg-collection-badge-purple)
    - [PRG Collection Badge (Black Book)](#prg-collection-badge-black)
    - [PRG Collection Badge (White Book)](#prg-collection-badge-white)

## Tier Badges

<a id="platinum-tier-project-badge"></a>

### ![#E5E4E2](https://via.placeholder.com/13/E5E4E2/000000?text=+) Platinum Tier Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Platinum']}" alt="Platinum" />
</a>

<a id="gold-tier-project-badge"></a>

### ![#FFD700](https://via.placeholder.com/13/FFD700/000000?text=+) Gold Tier Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Gold']}" alt="Gold" />
</a>

<a id="silver-tier-project-badge"></a>

### ![#C0C0C0](https://via.placeholder.com/13/C0C0C0/000000?text=+) Silver Tier Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Silver']}" alt="Silver" />
</a>

<a id="bronze-tier-project-badge"></a>

### ![#CD7F32](https://via.placeholder.com/13/CD7F32/000000?text=+) Bronze Tier Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Bronze']}" alt="Bronze" />
</a>

<a id="optimized-tier-project-badge"></a>

### ![#6236FF](https://via.placeholder.com/13/6236FF/000000?text=+) Optimized Tier Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Optimized']}" alt="Optimized" />
</a>

<br>
<br>

> [!TIP]
> Consult the [Category Guidelines](../guidelines/category_guidelines.md) for more information on the **PRG** project tier system and how to determine the appropriate tier badge for your project.

## Profile Badges

Add the following badge to your profile `README` to showcase your **PRG Collection** for your **GitHub portfolio**.
- The hyperlink will take your profile visitors to your categorized project tier table. 
- This will complete the **PRG** experience for your profile visitors.

<a id="prg-collection-badge"></a>

### ![#680F7F](https://via.placeholder.com/13/680F7F/000000?text=+) PRG Collection Badge (Optimized) (_Default_)

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{PRG_REPO_URL}/raw/main/docs/images/prg_optimized.png" alt="Collection" width="138" height="51" />
</a>

<a id="prg-collection-badge-collection"></a>

### ![#680F7F](https://via.placeholder.com/13/680F7F/000000?text=+) PRG Collection Badge (Collection) 

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{PRG_REPO_URL}/raw/main/docs/images/prg_collection.png" alt="Collection" width="138" height="51" />
</a>

<a id="prg-collection-badge-portfolio"></a>

### ![#680F7F](https://via.placeholder.com/13/680F7F/000000?text=+) PRG Collection Badge (Portfolio) 

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{PRG_REPO_URL}/raw/main/docs/images/prg_portfolio.png" alt="Collection" width="138" height="51" />
</a>

## Alternative Profile Badges

<a id="prg-collection-badge-purple"></a>

### ![#6236FF](https://via.placeholder.com/13/6236FF/000000?text=+) PRG Collection Badge (Purple Book)

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Purple_Collection']}" alt="Collection" />
</a>
<br>
<br>
<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Purple']}" alt="Optimized" />
</a>

<a id="prg-collection-badge-black"></a>

### ![#000000](https://via.placeholder.com/13/000000/000000?text=+) PRG Collection Badge (Black Book)

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Black_Collection']}" alt="Collection" />
</a>
<br>
<br>
<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Black']}" alt="Optimized" />
</a>

<a id="prg-collection-badge-white"></a>

### ![#FFFFFF](https://via.placeholder.com/13/FFFFFF/000000?text=+) PRG Collection Badge (White Book)

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['White_Collection']}" alt="Collection" />
</a>
<br>
<br>
<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['White']}" alt="Optimized" />
</a>

<br>
<br>

> [!NOTE]
> This file is automatically generated by the `project_tier_table_generator.py` script and the `weekly-project-tier-table-generator` GitHub Action workflow.

"""

    # Write markdown to a file
    with open(MD_BADGE_REF_PATH, 'w') as file:
        file.write(repo_badge_template)

def parse_private_md_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines = lines[4:]

        extra_repos_data = []
        for line in lines:
            columns = line.split('|')
            if len(columns) >= 8:
                icon_html = columns[1].strip()
                name_html = columns[2].strip()
                owner_html = columns[4].strip()

                # Extracting the URL and name directly using regex
                name_match = re.search(r'<a href="([^"]+)" target="_blank">([^<]+)</a>', columns[2].strip())
                if name_match:
                    url = name_match.group(1)
                    name = name_match.group(2)

                    created_at = columns[3].strip()
                    description = columns[5].strip()
                    technology = columns[6].strip()
                    category = columns[7].strip()
                    tier = columns[8].strip()

                    print(f"Found {name_html} in the private markdown file.")

                    order = float('inf')  # Default to infinity
                    if len(columns) > 9 and columns[9].strip().isdigit():
                        order = int(columns[9].strip())

                    data = {
                        'name_html': name_html,
                        'name': name,
                        'url': url,
                        'created_at': created_at,
                        'description': description,
                        'technology': technology,
                        'category': category,
                        'tier': tier,
                        'order': order,
                        'icon_html': icon_html,
                        'owner_html': owner_html
                    }
                    extra_repos_data.append(data)

        return extra_repos_data

    except Exception as e:
        print("An error occurred while parsing the file:")
        print(e)
        traceback.print_exc()
        return []

# Function to get all the repositories
def get_all_repos(username):
    repos = []
    page = 1
    while True:
        # response = requests.get(f'https://api.github.com/users/{username}/repos?page={page}&per_page=100',
        response = requests.get(f'https://api.github.com/user/repos?page={page}&per_page=999',
                                headers={'Authorization': f'token {GITHUB_TOKEN}'})
        if response.status_code != 200:
            print(f"Failed to fetch repositories: {response.status_code}")
            print(response.json())
            exit()

        new_repos = response.json()
        if not new_repos:
            break

        for repo in new_repos:

            # Org repos
            if repo['owner']['login'].lower() != username.lower() and INCLUDE_ORG_REPOS:
                # Apply the INCLUDE_FORKS filter
                if not INCLUDE_ORG_FORKS and repo['fork']:
                    continue
                
                # Apply the INCLUDE_PRIVATE_REPOS filter
                if not INCLUDE_ORG_PRIVATE_REPOS and repo['private']:
                    continue

               

            # User repos
            if repo['owner']['login'].lower() == username.lower():
                # Apply the INCLUDE_FORKS filter
                if not INCLUDE_FORKS and repo['fork']:
                    continue
                
                # Apply the INCLUDE_PRIVATE_REPOS filter
                if not INCLUDE_PRIVATE_REPOS and repo['private']:
                    continue

            repos.append(repo)

        page += 1

    return repos

# Function to sort the repositories
def sort_repos(repos_data):
    tier_order = {'Platinum': 1, 'Gold': 2, 'Silver': 3, 'Bronze': 4, 'Optimized': 5}
    
    return sorted(repos_data, key=lambda x: (tier_order.get(x['tier'], 4), x['order'], datetime.strptime(x['created_at'], '%Y-%m-%d')))

try:

    print(f"Sending API Request. Please wait...")

    repos = get_all_repos(USERNAME)
    
    repos_data = []

    for repo in repos:
        data = {}
        name = repo['name']
        owner = repo['owner']['login']
        data['name'] = name
        data['url'] = repo['html_url']
        data['created_at'] = repo['created_at'].split('T')[0]  # Formatting date
        data['description'] = repo['description'] if repo['description'] else 'No Description Provided.'
        data['size'] = repo['size']
        data['homepage'] = repo['homepage']
        data['owner'] = owner
        data['private'] = repo['private']

        # Fetching the content of PRG.md to determine the tier
            # Adjust the URL to point to the correct path of the PRG.md file (if it is not in the root directory)
                # If you change the path, you will have to change it in every repository or adjust it to dynamically fetch the file (which will slow down the process)
        prg_md_response = requests.get(f'https://api.github.com/repos/{owner}/{name}/contents/PRG.md',
                                        headers={'Authorization': f'token {GITHUB_TOKEN}'})

        # Default values
        data['tier'] = 'Optimized'  
        data['technology'] = ''
        data['category'] = ''
        data['order'] = float('inf')  # Default to infinity for those without an order, so they are sorted at the end
                                      # If you don't want to sort by an order, I suggest using a large number like 9999

        if prg_md_response.status_code == 200 or not INCLUDE_PRG_FILE_PROJECTS:
            if prg_md_response.status_code == 200:
                prg_md_content = prg_md_response.json()
                content = base64.b64decode(prg_md_content['content']).decode('utf-8').strip()
                lines = [re.sub('<[^<]+?>', '', line) for line in content.split('\n')]  # Clean HTML tags
                
                # Get Lines 15-18 (index 14-17) to extract the tier, technology, and category (if available)
                if lines:
                    # Tier info
                    tier_info = lines[14].split(':**')  # Adjusted the index
                    if len(tier_info) > 1 and tier_info[1].strip():
                        data['tier'] = tier_info[1].strip()
                    else:
                        data['tier'] = 'Optimized'
                    
                    # Technology info
                    data['technology'] = ''  # Default value
                    if len(lines) > 15:  # Adjusted the index
                        tech_info = lines[15].split(':**')  # Adjusted the index
                        if len(tech_info) > 1 and tech_info[1].strip():
                            data['technology'] = tech_info[1].strip()

                    # Category info
                    data['category'] = ''  # Default value
                    if len(lines) > 16:  # Adjusted the index
                        cat_info = lines[16].split(':**')  # Adjusted the index
                        if len(cat_info) > 1 and cat_info[1].strip():
                            data['category'] = cat_info[1].strip()

                    # Extracting order
                    if len(lines) > 17:  # Adjusted the index
                        order_info = lines[17].split(':**')  # Adjusted the index
                        if len(order_info) > 1 and order_info[1].strip().isdigit():
                            data['order'] = int(order_info[1].strip())

            repos_data.append(data)
        else:
            print(f"Skipping {name} as it does not contain a PRG.md file.")

    # Parse the private markdown file if the flag is set to True
    if INCLUDE_PRIVATE_FILE_PROJECTS:
        print(f"Parsing Private Repositories. Please wait...")

        existing_repos_data = parse_private_md_file(MD_FILE_PATH_PRIVATE)
        print(f"Number of repos fetched from private MD file: {len(existing_repos_data)}")

        # Append the existing repos to the repos_data table
        repos_data.extend(existing_repos_data)

        print(f"Total number of repos after extending: {len(repos_data)}")
    else:
        print("Skipping Private Repositories as per the configuration.")

    # Sort repos by tier and creation date
    sorted_repos = sort_repos(repos_data)

    # Creating or updating markdown file
    with open(MD_FILE_PATH, 'w') as md_file:

        # Initialize the counter before starting the loop
        counter = 1 

        # Send a GET request to the GitHub API to fetch user details
        response = requests.get(f"https://api.github.com/users/{USERNAME}", headers={"Authorization": f"token {GITHUB_TOKEN}"})

        # Check if the request was successful
        if response.status_code == 200:
            user_data = response.json()
            profile_url = user_data["html_url"]
            avatar_url = user_data["avatar_url"]

            # Write title and description
            md_file.write('<p align="center"><em><strong>PRG</strong> is utilized by the following personal and organizational accounts in this portfolio:</em></p>\n\n')

            # Start a div with display:flex to align items horizontally
            md_file.write('<div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 20px;">\n')

            # User profile and image
            md_file.write(f'<div style="text-align: center;">\n')  # Wrapper div for the user
            md_file.write(f'<a href="{profile_url}" target="_blank" class="icon-container"><img src="{avatar_url}" alt="{USERNAME}" style="border-radius: 50%; width: 150px; height: 150px;"></a>\n')
            md_file.write(f'<br>\n')
            md_file.write(f'<a href="{profile_url}" target="_blank">@{USERNAME}</a>\n')
            md_file.write(f'</div>\n')

            # Organizations
            orgs_response = requests.get(f"https://api.github.com/user/orgs", headers={"Authorization": f"token {GITHUB_TOKEN}"})

            if orgs_response.status_code == 200:
                orgs_data = orgs_response.json()

                # Loop through each organization and get details
                for org in orgs_data:
                    org_response = requests.get(org["url"], headers={"Authorization": f"token {GITHUB_TOKEN}"})
                    if org_response.status_code == 200:
                        org_details = org_response.json()
                        org_profile_url = org_details["html_url"]
                        org_avatar_url = org_details["avatar_url"]

                        # Write the organization's details in a flex item
                        md_file.write(f'<div style="text-align: center;">\n')  # Wrapper div for each org
                        md_file.write(f'<a href="{org_profile_url}" target="_blank" class="icon-container"><img src="{org_avatar_url}" alt="{org["login"]}" style="border-radius: 50%; width: 150px; height: 150px;"></a>\n')
                        md_file.write(f'<br>\n')
                        md_file.write(f'<a href="{org_profile_url}" target="_blank">@{org["login"]}</a>\n')
                        md_file.write(f'</div>\n')

            else:
                print(f"Failed to fetch org data for {USERNAME}: {orgs_response.content}")
                # Handle error or add fallback content

            # Close the flex container div
            md_file.write('</div><br>\n\n')

        else:
            print(f"Failed to fetch user data for {USERNAME}: {response.content}")
            # Handle error or add fallback content

        md_file.write('## Project Tier Table \n\n')
        md_file.write('<p align="center"><em><strong>PRG</strong> is optimized for the following projects and repositories:</em></p>\n\n')

        if MD_ONLY_TIER_TABLE:
            md_file.write('| Icon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Name | Created&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Owner | Description | Technology | Category | Tier&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |\n')
        else:
            md_file.write('| Icon | Name | Created&nbsp;&nbsp;&nbsp;&nbsp; | Owner | Description | Technology | Category | Tier |\n')
        md_file.write('| :---: | :---: | :---: | :---: | :--- | :--- | :--- | :---: |\n')

        for repo_data in sorted_repos:

            print(f"Building Repo {counter} - {repo_data['name']} (Technology: {repo_data['technology']}, Category: {repo_data['category']}, Tier: {repo_data['tier']}, Order: {repo_data['order']})")

            # Fetching the tier information and constructing the badge URL
            tier_key = repo_data['tier']
            badge_url = BADGES.get(tier_key)  # If the tier_key is not found, it returns None by default, so no need to specify None
            tier = f'<a href="{TIER_TABLE_URL}" target="_blank" class="icon-container"><img src="{badge_url}" alt="{tier_key}" /></a>' if badge_url else "Tier Not Available"

            # First check if the 'icon_html' is in the repo_data (it means it's coming from the private markdown file),
            # otherwise, try to fetch the icon from the public URL
            if 'icon_html' in repo_data:
                icon = repo_data['icon_html']
                name = repo_data['name_html']
                owner = repo_data['owner_html']
            else: 
                owner = repo_data['owner']
                icon_url = f'https://github.com/{owner}/{repo_data["name"]}/raw/main/{PROJECT_ICON_PATH}'
                icon_response = requests.get(icon_url)
                if icon_response.status_code != 200 or repo_data['size'] == 0:

                    icon_url = f'https://github.com/{owner}/{repo_data["name"]}/raw/master/{PROJECT_ICON_PATH}'
                    icon_response = requests.get(icon_url)
                    if icon_response.status_code != 200 or repo_data['size'] == 0:

                        # Check if the repo is private to use the private repo icon (Issue #3)
                        if repo_data['private']:
                            # Construct the expected icon file path
                            expected_icon_path = os.path.join(PRIVATE_REPO_ICON_DIR, f"{repo_data['name']}.png")
                            print(f"{repo_data['name']} is a private repo, checking if the icon exists at {expected_icon_path}...")
                            
                            # Check if the icon file exists
                            if os.path.isfile(expected_icon_path):
                                # Use the relative path from your project root to the icon
                                if MD_ONLY_TIER_TABLE:
                                    path_start = '..'
                                icon_url = f"{PRIVATE_REPO_ICON_DIR}/{repo_data['name']}.png"
                                print(f"Using private repo icon for {repo_data['name']}.")
                            else:
                                # Use placeholder if the icon file does not exist
                                if MD_ONLY_TIER_TABLE:
                                    path_start = '..'
                                icon_url = PLACEHOLDER_ICON
                                print(f"Icon not found for private repo {repo_data['name']}, using placeholder.")

                        else:
                            print(f"No icon found for {repo_data['name']} or the repository is empty, using a placeholder.")
                            if MD_ONLY_TIER_TABLE:
                                path_start = '..'
                            icon_url = PLACEHOLDER_ICON
                else:
                    print(f"Icon found for {repo_data['name']}!")

                # Check if the repo has a homepage URL, if so, use it as the icon link, otherwise, use the repo URL
                # If the repo is private, use the homepage, otherwise, use the PRG repo default URL
                if repo_data['homepage']:
                    icon = f'<a href="{repo_data["homepage"]}" class="icon-container" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                else:
                    if repo_data['private']:
                        icon = f'<a href="{PRG_REPO_URL}" class="icon-container" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                    else:
                        icon = f'<a href="{repo_data["url"]}" class="icon-container" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                
                # Handle organization special repo case for .github repo name
                if repo_data['name'] == '.github':
                        repo_data['name'] = owner
                        repo_data['url'] = f'https://github.com/{owner}/.github/blob/main/profile/README.md'
                
                # Get the repo name with a link to the repo
                # If the repo is private, use the homepage if it exists, otherwise, the PRG repo default URL
                if repo_data['private']:
                    if repo_data['homepage']:
                        name = f'<a href="{repo_data["homepage"]}" target="_blank">{repo_data["name"]}</a>'
                    else:
                        name = f'<a href="https://github.com/{owner}" target="_blank">{repo_data["name"]}</a>'
                else:
                    name = f'<a href="{repo_data["url"]}" target="_blank">{repo_data["name"]}</a>'

            # Get owner profile URL
            owner_url = f'<a href="https://github.com/{owner}" target="_blank">@{owner}</a>'

            # Writing the data to the markdown file
            md_file.write(f'| {icon} | {name} | {repo_data["created_at"]} | {owner_url} | {repo_data["description"]} | {repo_data["technology"]} | {repo_data["category"]} | {tier} |\n')

            # Increment the counter at the end of the loop
            counter += 1 

        # Set the timezone to Eastern Time  
        if LOCAL_TESTING:
            # Set the timezone to Eastern Time
            timezone = pytz.timezone(MY_TIME_ZONE)

            # Get the current time in Eastern Time with timezone name
            current_time = datetime.now(timezone).strftime("%Y-%m-%d %I:%M:%S %p %Z")

        else: 
            # Get timezone from environment variable or default to 'UTC' if not set
            timezone = os.getenv('TZ', 'UTC')
            tz = pytz.timezone(timezone)

            # Get the current time in the specified timezone
            current_time = datetime.now(tz).strftime("%Y-%m-%d %I:%M:%S %p %Z")

        # Create the footer under the table
        md_file.write(f'\n<div align="center"><b>Last Updated:</b><br><b>{current_time}</b></div>\n')       
        
        print(f"Markdown file '{MD_FILE_PATH}' has been updated.")

        create_repo_badges(USERNAME)

        print(f"Markdown file '{MD_BADGE_REF_PATH}' has been created.")
        

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc(file=sys.stdout)