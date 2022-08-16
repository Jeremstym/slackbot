#!/usr/bin/env python
import os

import setuptools

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return [s.strip() for s in f.readlines()
                if (s.strip() and not s.startswith('#'))]


_REQUIREMENTS_TXT = _read_reqs('requirements.txt')
_TESTS_REQUIREMENTS_TXT = _read_reqs('tests-requirements.txt')
_DEPENDENCY_LINKS = [word for word in _REQUIREMENTS_TXT if '://' in word]
_INSTALL_REQUIRES = [word for word in _REQUIREMENTS_TXT if '://' not in word]
_TEST_REQUIRE = [word for word in _TESTS_REQUIREMENTS_TXT if '://' not in word]

setuptools.setup(
    name='chatter_bot',
    version='0.1',
    install_requires=_INSTALL_REQUIRES,
    dependency_links=_DEPENDENCY_LINKS,
    tests_require=_TEST_REQUIRE,
    entry_points={
        'console_scripts': [
            # Do not change 'run-app', as that specific name is needed by Jenkins.
            # The part before the colon is the name of the module containg your main.
            # You will need to change it if your main is in a different location.
            'run-app = chatter_bot.chatterbot:main',
        ],
    },
    # This is necessary because jinja is not configured to read files from zips.
    zip_safe=False,
    # This includes data from the 'MANIFEST.in' file.
    include_package_data=True,
    packages=setuptools.find_packages()
)
