.. _readthedocs.org: http://www.readthedocs.org
.. _bower: http://www.bower.io
.. _sphinx: http://www.sphinx-doc.org
.. _compass: http://www.compass-style.org
.. _sass: http://www.sass-lang.com
.. _wyrm: http://www.github.com/snide/wyrm/
.. _grunt: http://www.gruntjs.com
.. _node: http://www.nodejs.com
.. _demo: http://docs.readthedocs.org
.. _hidden: http://sphinx-doc.org/markup/toctree.html

**************************
Read the Docs Sphinx Theme
**************************

This is an old project that I'm fairly confident is no longer used and can be deleted.

.. contents:: 

View a working demo_ over on readthedocs.org_.

This is a mobile-friendly sphinx_ theme I made for readthedocs.org_. It's
currently in development there and includes some rtd variable checks that can be ignored
if you're just trying to use it on your project outside of that site.

**This repo also exists as a submodule within the readthedocs itself**, so please make your edits to
the SASS files here, rather than the .css files on RTD.

.. image:: screen_mobile.png
    :width: 100%

Installation
============

Via package
-----------

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install sphinx_rtd_theme

In your ``conf.py`` file:

.. code:: python

    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"

    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

Via git or download
-------------------

Symlink or subtree the ``sphinx_rtd_theme/sphinx_rtd_theme`` repository into your documentation at
``docs/_themes/sphinx_rtd_theme`` then add the following two settings to your Sphinx
conf.py file:

.. code:: python

    html_theme = "sphinx_rtd_theme"
    html_theme_path = ["_themes", ]

Changelog
=========

v0.1.9
------

* Intermittent scrollbar visibility bug fixed. This change introduces a
  backwards incompatible change to the theme's layout HTML. This should only be
  a problem for derivative themes that have overridden styling of nav elements
  using direct decendant selectors. See `#215`_ for more information.
* Safari overscroll bug fixed
* Version added to the nav header
* Revision id was added to the documentation footer if you are using RTD
* An extra block, ``extrafooter`` was added to allow extra content in the
  document footer block
* Fixed modernizr URL
* Small display style changes on code blocks, figure captions, and nav elements

.. _#215: https://github.com/snide/sphinx_rtd_theme/pull/215

v0.1.8
------

* Start keeping changelog :)
* Support for third and fourth level headers in the sidebar
* Add support for Sphinx 1.3
* Add sidebar headers for :caption: in Sphinx toctree
* Clean up sidebar scrolling behavior so it never scrolls out of view

How the Table of Contents builds
================================

Currently the left menu will build based upon any ``toctree(s)`` defined in your index.rst file.
It outputs 2 levels of depth, which should give your visitors a high level of access to your
docs. If no toctrees are set the theme reverts to sphinx's usual local toctree.

It's important to note that if you don't follow the same styling for your rST headers across
your documents, the toctree will misbuild, and the resulting menu might not show the correct
depth when it renders.

Also note that the table of contents is set with ``includehidden=true``. This allows you
to set a hidden toc in your index file with the hidden_ property that will allow you
to build a toc without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll. However if your toc
is vertically too large, it will revert to static positioning. To disable the sticky nav
altogether change the setting in ``conf.py``.

Contributing or modifying the theme
===================================

The sphinx_rtd_theme is primarily a sass_ project that requires a few other sass libraries. I'm
using bower_ to manage these dependencies and sass_ to build the css. The good news is
I have a very nice set of grunt_ operations that will not only load these dependencies, but watch
for changes, rebuild the sphinx demo docs and build a distributable version of the theme.
The bad news is this means you'll need to set up your environment similar to that
of a front-end developer (vs. that of a python developer). That means installing node and ruby.

Set up your environment
-----------------------

1. Install sphinx_ into a virtual environment.

.. code::

    pip install sphinx

2. Install sass

.. code::

    gem install sass

2. Install node, bower and grunt.

.. code::

    // Install node
    brew install node

    // Install bower and grunt
    npm install -g bower grunt-cli

    // Now that everything is installed, let's install the theme dependecies.
    npm install

Now that our environment is set up, make sure you're in your virtual environment, go to
this repository in your terminal and run grunt:

.. code::

    grunt

This default task will do the following **very cool things that make it worth the trouble**.

1. It'll install and update any bower dependencies.
2. It'll run sphinx and build new docs.
3. It'll watch for changes to the sass files and build css from the changes.
4. It'll rebuild the sphinx docs anytime it notices a change to .rst, .html, .js
   or .css files.


Before you create an issue
--------------------------

I don't have a lot of time to maintain this project due to other responsibilities.
I know there are a lot of Python engineers out there that can't code sass / css and
are unable to submit pull requests. That said, submitting random style bugs without
at least providing sample documentation that replicates your problem is a good
way for me to ignore your request. RST unfortunately can spit out a lot of things
in a lot of ways. I don't have time to research your problem for you, but I do
have time to fix the actual styling issue if you can replicate the problem for me.


Before you send a Pull Request
------------------------------

When you're done with your edits, you can run ``grunt build`` to clean out the old
files and rebuild a new distribution, compressing the css and cleaning out
extraneous files. Please do this before you send in a PR.

Using this theme locally, then building on Read the Docs?
==========================================================

Currently if you import sphinx_rtd_theme in your local sphinx build, then pass
that same config to Read the Docs, it will fail, since RTD gets confused. If
you want to run this theme locally and then also have it build on RTD, then
you can add something like this to your config. Thanks to Daniel Oaks for this.

.. code:: python

    # on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if not on_rtd:  # only import and set the theme if we're building docs locally
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    # otherwise, readthedocs.org uses their theme by default, so no need to specify it

TODO
====
* Separate some sass variables at the theme level so you can overwrite some basic colors.
