"""Setup for pip package."""



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import unittest
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['mock']

setup(name='gttraffic',
      version='0.1',
      description='gttraffic is a package for implementing GeekTrust Solution ',
      url='https://github.com/ashavish/gttraffic',
      author='Asha Vishwanathan',
      author_email='asha dot vish at gmail dot com',
      license='MIT',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
