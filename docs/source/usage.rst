Usage
=====

.. _installation:

Installation
------------

To use playmanity, first install it using pip:

.. code-block:: console

   $ pip install playmanity

Connecting bot
----------------

To create our bot instance we use ``playmanity.Bot()`` class:

.. autofunction:: playmanity.Bot()

This class will be used as our account.

.. autoexception:: playmanity.InvalidKindError

Running bot
----------------

To run and get our bot ``token`` we should use ``run()`` method with our bot instance

For example:

.. code-block:: code

   import playmanity

   clientinit = playmanity.accounts.Bot("Login","Password")
   callback = clientinit.run()
   client = callback

