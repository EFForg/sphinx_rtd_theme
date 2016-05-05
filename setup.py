# -*- coding: utf-8 -*-
"""`sphinx_rtd_theme` lives on `Github`_.

.. _github: https://www.github.com/EFForg/sphinx_rtd_theme

"""
from setuptools import setup
from sphinx_rtd_theme import __version__


setup(
    name='sphinx_rtd_theme',
    version=__version__,
    url='https://github.com/EFForg/sphinx_rtd_theme/',
    license='MIT',
    author='Mark Burdett',
    author_email='mfb@eff.org',
    description='A fork of the ReadTheDocs.org theme for Sphinx, 2013 version, by Dave Snider.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_rtd_theme'],
    package_data={'sphinx_rtd_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
