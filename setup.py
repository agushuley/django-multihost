#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages
from gushuley.multihost import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = app_name,
    version = version,
    packages = find_packages(),
    include_package_data = True,
    author = "Andriy Gushuley",
    author_email = "agushuley@me.com",
    description = "A Django application/framework which allow to serve different hostnames "
                  "and urlconfs in one django application instance",
    long_description = \
"""
[https://github.com/agushuley/gu-multihost]
""",
    license = "MIT License",
    keywords = "django multihost framework",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/agushuley/gu-multihost",
)