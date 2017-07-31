.. image:: https://img.shields.io/pypi/v/pygments-style-apprentice.svg
    :target: https://pypi.python.org/pypi/pygments-style-apprentice


Pygments style for Apprentice
=============================

This is a pygments_ plugin for the apprentice_ colorscheme. It was mainly developed to be
used as an IPython highlighting style.

Install
-------

.. code-block:: sh

    $ pip install pygments-style-apprentice


IPython usage
-------------

Generate a new configuration if you haven't done that already

.. code-block:: sh

    $ ipython profile create

Adapt the IPython configuration to use the Apprentice style

.. code-block:: python

    c.TerminalInteractiveShell.highlighting_style = "apprentice"


Caveats
-------

The IPython prompt is currently not correctly colored.


.. _pygments: http://pygments.org/
.. _apprentice: http://romainl.github.io/Apprentice/
