#!/usr/bin/env python3
""" youtube-archive
    youtube-dl wrapper
"""
import setuptools

setuptools.setup(
    name='youtube-archive',
    version='0.1.0dev1',
    description=__doc__,
    url='https://github.com/thorsummoner/youtube-archive',
    author='Dylan Scott Grafmyre',
    author_email='dylan.grafmyre@gmail.com',

    pacakges=['youtube_archive'],

    install_requires=[
        'youtube-dl',
        # aria2c (not python)
    ],

    entry_points={
        'console_scripts': [
            'yta=youtube_archive.__main__:main',
        ],
    },
)
