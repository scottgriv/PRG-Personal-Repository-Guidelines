import os
import requests
import base64
import sys
import traceback
import re
from datetime import datetime

# GitHub token for API requests
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '') # Uncomment this line when done testing for GitHub Actions (environment variable)
# GITHUB_TOKEN = '' # Uncomment this line when testing locally and add your API token to it (hardcoded)

if GITHUB_TOKEN is None:
    print("GitHub token is not set. Set the GITHUB_TOKEN environment variable.")
    sys.exit(1)

# Username for your GitHub account
USERNAME = os.environ.get('GITHUB_ACTOR', 'default_username') # Uncomment this line when done testing for GitHub Actions (environment variable)
# USERNAME = 'scottgriv' # Uncomment this line when testing locally and add your username to it (hardcoded)
print(f"GitHub Username: {USERNAME}")

# File Paths
# Add an extra . to the beginning of the path to make it relative to the root of the repository when testing locally (i.e. ../docs)
MD_FILE_PATH = './categories/project_tier_table.md' # Path to the the main project tier table markdown file
MD_FILE_PATH_PRIVATE = './categories/project_tier_table_private.md' # Path to the private project tier table markdown file
MD_BADGE_REF_PATH = './categories/badge_references.md' # Path to the badge reference markdown file
PLACEHOLDER_ICON = './docs/images/icon-placeholder-rounded.png' # Placeholder for missing icons
TIER_TABLE_URL = f'https://{USERNAME}.github.io/PRG-Personal-Repository-Guidelines/' # URL to the project tier table

# Configuration Flags
INCLUDE_NO_PRG_FILE_PROJECTS = False  # Set to False if you don't want to include projects that don't have a PRG file
INCLUDE_PRIVATE_FILE_PROJECTS = True  # Set to False if you don't want to include projects that are in the private markdown file
INCLUDE_FORKS = True  # Set to False if you don't want to include forked repos
INCLUDE_ORG_REPOS = True  # Set to False if you don't want to include org repos
INCLUDE_FORKS_ORG = True  # Set to False if you don't want to include forked org repos

# Badges URLs
BADGES = {
    'Gold': 'https://img.shields.io/badge/PRG-Gold Project-FFD700?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkQ3MDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Silver': 'https://img.shields.io/badge/PRG-Silver Project-C0C0C0?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDMEMwQzAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Bronze': 'https://img.shields.io/badge/PRG-Bronze Project-CD7F32?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNDRDdGMzIiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Purple': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiM2MjM2RkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Black': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiMwMDAwMDAiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'White': 'https://img.shields.io/badge/PRG-Personal Repository Guidelines-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo=',
    'Optimized': 'https://img.shields.io/badge/PRG-Optimized-6236FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMjYuMDAwMDAwcHQiIGhlaWdodD0iMzQuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCAyNi4wMDAwMDAgMzQuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+Cgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwzNC4wMDAwMDApIHNjYWxlKDAuMTAwMDAwLC0wLjEwMDAwMCkiCmZpbGw9IiNGRkZGRkYiIHN0cm9rZT0ibm9uZSI+CjxwYXRoIGQ9Ik0xMiAzMjggYy04IC04IC0xMiAtNTEgLTEyIC0xMzUgMCAtMTA5IDIgLTEyNSAxOSAtMTQwIDQyIC0zOCA0OAotNDIgNTkgLTMxIDcgNyAxNyA2IDMxIC0xIDEzIC03IDIxIC04IDIxIC0yIDAgNiAyOCAxMSA2MyAxMyBsNjIgMyAwIDE1MCAwCjE1MCAtMTE1IDMgYy04MSAyIC0xMTkgLTEgLTEyOCAtMTB6IG0xMDIgLTc0IGMtNiAtMzMgLTUgLTM2IDE3IC0zMiAxOCAyIDIzCjggMjEgMjUgLTMgMjQgMTUgNDAgMzAgMjUgMTQgLTE0IC0xNyAtNTkgLTQ4IC02NiAtMjAgLTUgLTIzIC0xMSAtMTggLTMyIDYKLTIxIDMgLTI1IC0xMSAtMjIgLTE2IDIgLTE4IDEzIC0xOCA2NiAxIDc3IDAgNzIgMTggNzIgMTMgMCAxNSAtNyA5IC0zNnoKbTExNiAtMTY5IGMwIC0yMyAtMyAtMjUgLTQ5IC0yNSAtNDAgMCAtNTAgMyAtNTQgMjAgLTMgMTQgLTE0IDIwIC0zMiAyMCAtMTgKMCAtMjkgLTYgLTMyIC0yMCAtNyAtMjUgLTIzIC0yNiAtMjMgLTIgMCAyOSA4IDMyIDEwMiAzMiA4NyAwIDg4IDAgODggLTI1eiIvPgo8L2c+Cjwvc3ZnPgo='
}

# Function to create markdown with user-specific links
def create_repo_badges(username):

    repo_badge_template = f"""## Tier Badges

Use this file as a template to gather and add badges to your project's `README.md` files.
- Be sure to run the workflow to automatically update the badges with your username
- Optionally, you can change the `href` attributes below to point to your project's repository by changing the username to your GitHub username.

### Gold Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Gold']}" alt="Gold" />
</a>

### Silver Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Silver']}" alt="Silver" />
</a>

### Bronze Project Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Bronze']}" alt="Bronze" />
</a>

### Purple Brand Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Purple']}" alt="Optimized" />
</a>

### Black Brand Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Black']}" alt="Optimized" />
</a>

### White Brand Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['White']}" alt="Optimized" />
</a>

## Profile README Badges

Add one of the two badges below to your Profile `README` to show that you follow **PRG**, the hpyerlink will take your profile visitors to your catagorized project tier table. You may need to adjust the `src` attribute of the image tag to point to the correct path of the image and also include the "prg_optimized.png" file in your repository.

### PRG Optimized Badge

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="{BADGES['Optimized']}" alt="Optimized" />
</a>

### PRG Optimized Logo

<a href="{TIER_TABLE_URL}" target="_blank">
    <img src="../docs/images/prg_optimized.png" alt="Optimized" width="138" height="51" />
</a>
"""

    # Write markdown to a file
    with open(MD_BADGE_REF_PATH, 'w') as file:
        file.write(repo_badge_template)

def get_all_org_repos(username):
    org_repos = []
    response = requests.get('https://api.github.com/user/orgs',
                            headers={'Authorization': f'token {GITHUB_TOKEN}'})
    if response.status_code != 200:
        print(f"Failed to fetch organizations: {response.status_code}")
        print(response.json())
        return org_repos

    orgs = response.json()
    for org in orgs:
        org_name = org['login']
        page = 1
        while True:
            response = requests.get(f'https://api.github.com/orgs/{org_name}/repos?page={page}&per_page=100',
                                    headers={'Authorization': f'token {GITHUB_TOKEN}'})
            if response.status_code != 200:
                print(f"Failed to fetch repositories for organization {org_name}: {response.status_code}")
                print(response.json())
                break

            new_repos = response.json()
            if not new_repos:
                break

            for repo in new_repos:

                if not repo['private'] and (INCLUDE_ORG_REPOS or not repo['fork']):
                    if repo['name'] == '.github':
                        repo['name'] = org_name
                        repo['html_url'] = f'https://github.com/{org_name}/.github/blob/main/profile/README.md'
                    org_repos.append(repo)

            page += 1

    print(f"Fetched {len(org_repos)} public organization repositories.")
    return org_repos

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

                # Extracting the URL and name directly using regex
                name_match = re.search(r'<a href="([^"]+)" target="_blank">([^<]+)</a>', columns[2].strip())
                if name_match:
                    url = name_match.group(1)
                    name = name_match.group(2)

                    created_at = columns[3].strip()
                    description = columns[4].strip()
                    category = columns[5].strip()
                    technology = columns[6].strip()
                    tier = columns[7].strip()

                    print(f"Found {name_html} in the private markdown file.")

                    order = float('inf')  # Default to infinity
                    if len(columns) > 8 and columns[8].strip().isdigit():
                        order = int(columns[8].strip())

                    data = {
                        'name_html': name_html,
                        'name': name,
                        'url': url,
                        'created_at': created_at,
                        'description': description,
                        'category': category,
                        'technology': technology,
                        'tier': tier,
                        'order': order,
                        'icon_html': icon_html
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
        response = requests.get(f'https://api.github.com/users/{username}/repos?page={page}&per_page=100',
                                headers={'Authorization': f'token {GITHUB_TOKEN}'})
        if response.status_code != 200:
            print(f"Failed to fetch repositories: {response.status_code}")
            print(response.json())
            exit()

        new_repos = response.json()
        if not new_repos:
            break

        for repo in new_repos:
            if INCLUDE_FORKS or not repo['fork']:
                repos.append(repo)

        page += 1

    return repos

# Function to sort the repositories
def sort_repos(repos_data):
    tier_order = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Optimized': 4}
    
    return sorted(repos_data, key=lambda x: (tier_order.get(x['tier'], 4), x['order'], datetime.strptime(x['created_at'], '%Y-%m-%d')))

try:

    print(f"Sending API Request. Please wait...")

    repos = get_all_repos(USERNAME)

    if INCLUDE_ORG_REPOS:
        org_repos = get_all_org_repos(USERNAME)
        repos.extend(org_repos)  # This
    
    repos_data = []

    for repo in repos:
        data = {}
        name = repo['name']
        data['name'] = name
        data['url'] = repo['html_url']
        data['created_at'] = repo['created_at'].split('T')[0]  # Formatting date
        data['description'] = repo['description'] if repo['description'] else 'No description provided'
        data['size'] = repo['size']
        data['homepage'] = repo['homepage']

        # Fetching the content of PRG.md to determine the tier
            # Adjust the URL to point to the correct path of the PRG.md file (if it is not in the root directory)
                # If you change the path, you will have to change it in every repository or adjust it to dynamically fetch the file (which will slow down the process)
        prg_md_response = requests.get(f'https://api.github.com/repos/{USERNAME}/{name}/contents/PRG.md',
                                        headers={'Authorization': f'token {GITHUB_TOKEN}'})

        # Default values
        data['tier'] = 'Optimized'  
        data['technology'] = ''
        data['category'] = ''
        data['order'] = float('inf')  # Default to infinity for those without an order

        if prg_md_response.status_code == 200 or INCLUDE_NO_PRG_FILE_PROJECTS:
            if prg_md_response.status_code == 200:
                prg_md_content = prg_md_response.json()
                content = base64.b64decode(prg_md_content['content']).decode('utf-8').strip()
                lines = [re.sub('<[^<]+?>', '', line) for line in content.split('\n')]  # Clean HTML tags
                
                # Get Lines 7-10 (index 6-9) to extract the tier, technology, and category (if available)
                if lines:
                    # Tier info
                    tier_info = lines[6].split(':')  # Adjusted the index
                    if len(tier_info) > 1 and tier_info[1].strip():
                        data['tier'] = tier_info[1].strip()
                    else:
                        data['tier'] = 'Optimized'
                    
                    # Technology info
                    data['technology'] = ''  # Default value
                    if len(lines) > 7:  # Adjusted the index
                        tech_info = lines[7].split(':')  # Adjusted the index
                        if len(tech_info) > 1 and tech_info[1].strip():
                            data['technology'] = tech_info[1].strip()

                    # Category info
                    data['category'] = ''  # Default value
                    if len(lines) > 8:  # Adjusted the index
                        cat_info = lines[8].split(':')  # Adjusted the index
                        if len(cat_info) > 1 and cat_info[1].strip():
                            data['category'] = cat_info[1].strip()

                    # Extracting order
                    if len(lines) > 9:  # Adjusted the index
                        order_info = lines[9].split(':')  # Adjusted the index
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

        # Writing title
        md_file.write('## Project Tier Table\n\n')

        md_file.write('| Icon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Name | Created&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description | Category | Technology | Tier&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |\n')
        md_file.write('| :---: | :---: | :---: | :--- | :--- | :--- | :---: |\n')

        for repo_data in sorted_repos:

            print(f"Building Repo {counter} - {repo_data['name']} (Category: {repo_data['category']}, Technology: {repo_data['technology']}, Tier: {repo_data['tier']}, Order: {repo_data['order']})")

            # Fetching the tier information and constructing the badge URL
            tier_key = repo_data['tier']
            badge_url = BADGES.get(tier_key)  # If the tier_key is not found, it returns None by default, so no need to specify None
            tier = f'<a href="{TIER_TABLE_URL}" target="_blank"><img src="{badge_url}" alt="{tier_key}" /></a>' if badge_url else "Tier Not Available"

            # First check if the 'icon_html' is in the repo_data (it means it's coming from the private markdown file),
            # otherwise, try to fetch the icon from the public URL
            if 'icon_html' in repo_data:
                icon = repo_data['icon_html']
                name = repo_data['name_html']
            else:
                icon_url = f'https://github.com/{USERNAME}/{repo_data["name"]}/raw/main/docs/images/icon-rounded.png'
                icon_response = requests.get(icon_url)
                if icon_response.status_code != 200 or repo_data['size'] == 0:
                    print(f"No icon found for {repo_data['name']} or the repository is empty, using a placeholder.")
                    icon_url = PLACEHOLDER_ICON
                    
                if repo_data['homepage']:
                    icon = f'<a href="{repo_data["homepage"]}" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                else:
                    icon = f'<a href="{repo_data["url"]}" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                    
                # icon = f'<a href="{repo_data["url"]}" target="_blank"><img src="{icon_url}" width="100" height="100" alt="Icon"></a>'
                name = f'<a href="{repo_data["url"]}" target="_blank">{repo_data["name"]}</a>'

            # Writing the data to the markdown file
            md_file.write(f'| {icon} | {name} | {repo_data["created_at"]} | {repo_data["description"]} | {repo_data["category"]} | {repo_data["technology"]} | {tier} |\n')

            # Increment the counter at the end of the loop
            counter += 1 
                    
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Adjust the format as needed

        # Create the footer under the table
        md_file.write(f'\n<div align="center"><i>Built with GitHub Actions</i>'
                    f'<br><b>Last Updated: {current_time}</b></div>\n')          
        
        print(f"Markdown file '{MD_FILE_PATH}' has been updated.")

        create_repo_badges(USERNAME)

        print(f"Markdown file '{MD_BADGE_REF_PATH}' has been created.")
        

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc(file=sys.stdout)