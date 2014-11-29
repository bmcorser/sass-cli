sass-cli
########

    I don't want to install Ruby, but I want to compile ``*.scss`` from the
    command line.

Same here.

If you use the Ruby CLI, you will find some things missing. This command
accepts two arguments, which may either be a pair of filenames or a pair of
directory names.

Examples
--------

Two files:

.. code-block:: bash

    $ sass assets/scss/file.scss build/output.css


Two dirs:

.. code-block:: bash

    $ sass assets/scss build/css
