import os

from setuptools import setup, find_packages
from glob import glob

setup(name='AjaxTerm2',
      version='1.1.0',
      py_modules=['ajaxterm2'],
      install_requires=['webob','paste','pastedeploy'],
      data_files=[('', glob('*.ini')),
                  ('www', glob('www/*.html')),
                  ('www/js', glob('www/js/*.js')),
                  ('www/css', glob('www/css/*.css')),
                   ],
      )
