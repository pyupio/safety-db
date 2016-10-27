*Note: This database is currently in its early stages. It's possible that there are false positives and missing packages.*

## What is this?

This is an effort to collect all known security vulnerabilities in Python packages and make them available to consume for humans and automated tools.

The data is collected by filtering CVEs and changelogs for certain keywords and then manually reviewing them. Take a look at [previous pull requests](https://github.com/pyupio/safety-db/pulls) to see how that looks like.

## Using this data

For humans:

- There's a small website available that lets you browse the data: https://pyupio.github.io/safety-db/

For robots:

Check out the `data` directory:

- [insecure.json](https://github.com/pyupio/safety-db/blob/master/data/insecure.json) contains just the package name and all insecure releases as a plain list.
- [insecure_full.json](https://github.com/pyupio/safety-db/blob/master/data/insecure_full.json) additionally contains the CVE description and URLs, or the relevant part of the changelog.

The database is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This allows you to use the data in any non commercial project as long as you link back to this repo. If you need a license for a commercial project, please get in touch.

## Tools

- [safety](https://github.com/pyupio/safety) checks your installed dependencies for known security vulnerabilities. To use it, install it in the virtualenv you want to check with `pip install safety` and then run `safety check`.
- [pyup.io](https://pyup.io) *coming soon*
- *your tool?*

## Support this project

If you find this useful, please consider getting a paid [pyup.io](https://pyup.io) account. This is what makes projects like this possible.
