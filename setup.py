from distutils.core import setup
import os

cwd = os.path.abspath(os.path.dirname(__file__))
requirements_txt = filter(None, open(os.path.join(cwd, 'requirements.txt')).read().split('\n'))
readme = open(os.path.join(cwd, 'README.md')).read()

setup(name='pypi-cdn-log-archiver',
      version='0.1.1',
      description='log archiver for pypi cdn logs',
      long_description=readme,
      author='Benjamin W. Smith',
      author_email='benjaminwarfield@gmail.com',
      packages=[],
      url='http://github.com/benjaminws/pypi-cdn-log-archiver',
      install_requires=requirements_txt,
      scripts=['src/bin/pypi-cdn-log-archiver'],
      platforms = 'Posix; MacOS X; Windows',
) 

