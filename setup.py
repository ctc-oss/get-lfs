import os
from setuptools import setup
from version import get_version

requires = []
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().splitlines()

setup(name='get-lfs',
      version=get_version(),
      packages=['lfs'],
      install_requires=requires,
      include_package_data=True,
      extras_require={
          'native': ['GitPython']
      }
      )
