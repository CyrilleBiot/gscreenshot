#!/usr/bin/env python

from setuptools import setup
import sys
import os

install_requires = [
    'pillow',
    'pygtk',
    'pygobject'
    ]

test_requires = [
    'nose',
    'mock'
    ]

data_files=[
    ('bin/', ['dist/bin/gscreenshot'])
    ]


setup(name='gscreenshot',
    version='2.0.1',
    description='Lightweight GTK frontend to scrot',
    author='Nate Levesque',
    author_email='public@thenaterhood.com',
    url='https://github.com/thenaterhood/gscreenshot/archive/master.zip',
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='nose.collector',
    package_dir={'':'src'},
    packages=[
        'gscreenshot',
        'gscreenshot.resources',
        'gscreenshot.resources.gui',
        'gscreenshot.resources.gui.glade'
        ],
    data_files=data_files,
    package_data={
        '': ['*.glade']
        }
    )

