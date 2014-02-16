import os
from setuptools import setup
from distutils.command.sdist import sdist
from distutils.command.bdist import bdist

from pip.req import parse_requirements

cwd = os.path.abspath(os.path.dirname(__file__))

requirements_txt = parse_requirements(os.path.join(cwd, 'requirements.txt'))
requirements = [str(r.req) for r in requirements_txt]
readme = open(os.path.join(cwd, 'README.md')).read()

setup(name='pypi-cdn-log-archiver',
      version='0.1.4',
      description='log archiver for pypi cdn logs',
      long_description=readme,
      author='Benjamin W. Smith',
      author_email='benjaminwarfield@gmail.com',
      packages=[],
      url='http://github.com/benjaminws/pypi-cdn-log-archiver',
      install_requires=requirements,
      scripts=['src/bin/pypi-cdn-log-archiver'],
      platforms = 'Posix; MacOS X; Windows',
) 

