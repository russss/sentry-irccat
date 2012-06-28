#!/usr/bin/env python
"""
sentry-irccat
==============

An extension for Sentry which integrates with irccat (or compatible servers).

:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
    'nose>=1.1.2',
]

install_requires = [
    'sentry>=4.6.0',
]

setup(
    name='sentry-irccat',
    version='0.1.0',
    author='Russ Garrett',
    author_email='russ@garrett.co.uk',
    url='http://www.github.com/russss',
    description='A Sentry extension which integrates with irccat',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    entry_points={
       'sentry.plugins': [
            'irccat = sentry_irccat.plugin:IRCCatMessage'
        ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
