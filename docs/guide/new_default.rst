
The default File
---------------------

A regime is a preset of settings. 
It can be loaded from or saved into a file.
If you want your example to start up with a loaded regime, or maybe multiple, 
you need a file called::

    default.sreg

Since most editing programs do not know this format, it might be easier to copy
and work with the default file from here::

    pymoskito/pymoskito/examples/ballbeam/default.sreg

This file will be loaded by the code in lines 29-33 of the :doc:`main file <new_main>`.

To create a file with multiple regimes, just add the following code at the 
bottom of your existing default file again:

.. literalinclude:: ../../pymoskito/examples/ballbeam/default.sreg
    :linenos: