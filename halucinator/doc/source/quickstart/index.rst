================
Quickstart Guide
================

Welcome to the quickstart guide for HALucinator. Here you will find
everything you need to set up quickly.


Setting up your environment
---------------------------

First, you will need a recent linux distribution with Python 3.9 or 
later installed. Older Linux distributions may work, but we do not 
support them.

We recommend you package your projects with `poetry`, but this is not 
obligatory. To install this, use:

.. code-block:: sh

  pip install --user poetry

Installing HALucinator
----------------------

HALucinator can be installed using the pip tool as follows:

.. code-block:: sh

  poetry install
  poetry build
  pip install ./dist/halucinator-0.1.0-py3-none-any.whl
