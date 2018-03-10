[![safety](https://raw.githubusercontent.com/pyupio/safety-db/master/safety-db.jpg)](https://pyup.io/safety/)

## What is Safety DB?

Safety DB is a database of known security vulnerabilities in Python packages. The data is made available by [pyup.io](https://pyup.io/) and synced with this repository once per month. Most of the entries are found by filtering CVEs and changelogs for certain keywords and then manually reviewing them.

## Tools

- [Safety CI](https://pyup.io/safety/ci/) is a deep GitHub integration that's available on pyup.io. It checks your commits and Pull Requests.
- [Safety](https://pyup.io/safety/) is a command line tool that checks virtualenvironments and requirement files either locally or on a CI server. 
- [Safety Django](https://pyup.io/safety/django/) is a package for Django that warns you in the admin area if your installed Django release is insecure.
- [Safety Bar](https://github.com/pyupio/safety-bar) (alpha) is a macOS menubar application.
- A [pre-commit hook](https://github.com/Lucas-C/pre-commit-hooks-safety) by Lucas Cimon.
- [`pipenv check`](https://pipenv.readthedocs.io/en/latest/advanced/#detection-of-security-vulnerabilities) relies on `safety` and Safety-DB to check for known vulnerabilities in locked components
- *your tool?*

## Installation

```sh

pip install safety-db
```

## Usage

```python

from safety_db import INSECURE, INSECURE_FULL
```

## What is this not?

This is not a hall of shame, or a list of packages to avoid. The package maintainers show a great responsibility by documenting and fixing security issues in such a way that they can be listed here. That's extremely valuable when considering using a package in production.

## Using this data

For humans:

- There's a small website available that lets you browse the data: https://pyupio.github.io/safety-db/

For robots:

Check out the `data` directory:

- [insecure.json](https://github.com/pyupio/safety-db/blob/master/data/insecure.json) contains just the package name and all insecure releases as a plain list.
- [insecure_full.json](https://github.com/pyupio/safety-db/blob/master/data/insecure_full.json) additionally contains the CVE description and URLs, or the relevant part of the changelog.

The database is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This allows you to use the data in any non commercial project as long as you link back to this repo. If you need a license for a commercial project, please contact support@pyup.io.
