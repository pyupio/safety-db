import os

from setuptools import setup

from safety_db import __version__ as version

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
except:
    readme = ''

tests_require = [
    'packaging',
]

setup(
    name='safety-db',
    version=version,
    description="A curated database of insecure Python packages",
    long_description=readme,
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
    py_modules=['safety_db'],
    license='Attribution-NonCommercial-ShareAlike 4.0 International',
    install_requires=[],
    tests_require=tests_require,
    include_package_data=True,
)
