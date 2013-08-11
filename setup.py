#!/usr/bin/env python

from distutils.core import setup
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()


setup(name='Combinatorics',
      version='1.4.1',
      description='Basic Combinatorics Functions',
      long_description=README + '\n\n' + NEWS,
      author='Phillip M. Feldman',
      author_email='Phillip.M.Feldman@gmail.com',
      url='http://pypi.python.org/pypi/Combinatorics',
      py_modules=['combinatorics']
     )
