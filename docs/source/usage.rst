Usage
=====

.. _installation:

Installation
------------

To use playmanity, first install it using pip:

.. code-block:: console

   $ pip install playmanity

Linking account
----------------

To link our account we use ``playmanity.account()`` class:

.. autofunction:: playmanity.account()

This class will be used as our primary account.


Running bot
----------------

To link and run our account we should use ``run()`` method with our ``playmanity.account()`` instance

For example:

.. code-block:: python

   account = playmanity.account("Nickname","Password")
   account.run()

Overall we should get:

.. code-block:: python
   import playmanity

   account = playmanity.account("Nickname","Password")
   account.run()