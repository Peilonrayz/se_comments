SE Comments
===========

.. image:: https://travis-ci.com/Peilonrayz/se_comments.svg?branch=master
   :target: https://travis-ci.com/Peilonrayz/se_comments
   :alt: Build Status

About
-----

This is a micro-language to build common comments on the Stack Exchange network.
The comments have a modular design, this means that you can plug them together like lego.

.. code:: bash

    $ python -m se_comments "Welcome[John Doe],VTC[Broken[Quote[this does not work], Asking[to fix this]], Inline], Scope[Title]"
    552 / 600  
    Welcome to Code Review John Doe. Unfortunately your question is currently off-topic. We only review [code that works as intended](//codereview.meta.stackexchange.com/a/3650). Since you've said "this does not work"; and you're asking us to fix this we can see the code is not working correctly. The code to be reviewed must be [inline in the question](//codereview.meta.stackexchange.com/q/1308). Once you have fixed the issues with your post we'll be happy to review your code. [Titles](/help/how-to-ask) should only consist of a description of your code.

Welcome to Code Review John Doe. Unfortunately your question is currently off-topic. We only review `code that works as intended <https://codereview.meta.stackexchange.com/a/3650>`_. Since you've said "this does not work"; and you're asking us to fix this we can see the code is not working correctly. The code to be reviewed must be `inline in the question <https://codereview.meta.stackexchange.com/q/1308>`_. Once you have fixed the issues with your post we'll be happy to review your code. `Titles <https://codereview.stackexchange.com/help/how-to-ask>`_ should only consist of a description of your code.

Installation
------------

.. code:: shell

   $ git clone https://github.com/Peilonrayz/se_comments
   $ cd se_comments
   $ python -m pip install .

Documentation
-------------

Documentation is available `via GitHub <https://peilonrayz.github.io/se_comments/>`_.

Testing
-------

To run all tests run ``nox``. No venv is needed; nox makes all of them for us.

.. code:: shell

   $ python -m pip install --user nox
   $ git clone https://github.com/Peilonrayz/se_comments
   $ cd se_comments
   se_comments $ nox

License
-------

SE Comments is available under the MIT license.
