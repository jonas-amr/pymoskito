
Implementing a Model (too much for tutorial)
--------------------------------------------

In case your model contains discontinuities, the solver needs
to be reseted. The method root_function() must return true 
and the state to continue with if a switching point is reached.
In this example, their are no discontinuities. If you are interested
in this method, please take a look at the 'Ball in Tube' example.

.. literalinclude:: ../../pymoskito/examples/ballbeam/model.py
    :lines: 69-75
    :lineno-match:

Every model needs boundary conditions. 
In case they are violated, the following method must throw
an exception and the simulation will be stopped:

.. literalinclude:: ../../pymoskito/examples/ballbeam/model.py
    :lines: 77-85
    :lineno-match:

