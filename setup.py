import re
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))


# Get current version
with open(path.join(here, 'data', '__init__.py')) as fp:
    main_package = fp.read()
version_re = r"^__version__\s*=\s*['\"]([^'\"]*)['\"]"
version_match = re.search(version_re, main_package, re.M)
if not version_match:
    raise RuntimeError("Unable to find version string.")
version = version_match.group(1)


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


tests_require = [
    'packaging',
    'parameterized',
]

setup(
    name='safety-db',
    version=version,
    description="A curated database of insecure Python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords="security",
    author='Jannis Gebauer',
    author_email='support@pyup.io',
    url='https://github.com/pyupio/safety-db/',
    package_dir={
        'safety_db': 'data',
    },
    packages=['safety_db'],
    license='Attribution-NonCommercial-ShareAlike 4.0 International',
    install_requires=[],
    tests_require=tests_require,
    include_package_data=True,
)
