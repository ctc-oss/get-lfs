import os
from setuptools import setup

requires = []
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().splitlines()

setup(name='get-lfs',
      version='0.0.1',
      packages=['lfs'],
      install_requires=requires,
      include_package_data=True,
      extras_require={
          'native': ['GitPython']
      }
      )
