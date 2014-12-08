# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import ode
from sim_core import SimulationModule

#---------------------------------------------------------------------
# solver base class 
#---------------------------------------------------------------------
class Solver(SimulationModule):

    def __init__(self, mode):
        SimulationModule.__init__(self)
        self.mode = mode
        return

    def getOutputDimension(self):
        return self.output_dim

    def initialize(self):
        self.solver.set_integrator(self.mode,\
                method=self.settings['Method'],\
                rtol=self.settings['rTol'],\
                atol=self.settings['aTol'],\
                ) 
        self.solver.set_initial_value(self.settings['initial state'])

    def integrate(self, t):
        return self.calcOutput(t)

    def getTime(self):
        return self.solver.t

#---------------------------------------------------------------------
# VODE Solver
#---------------------------------------------------------------------
class VODESolver(Solver):
    '''
    VODE Solver
    '''

    #solver specific
    settings = {'Method': 'adams',\
            'step size': 0.01,\
            'rTol': 1e-6,\
            'aTol': 1e-9,\
            'end time': 10,\
            'initial state': [0, 0, 0, 0],\
            }
    
    def __init__(self, output_dim, stateFunction):
        Solver.__init__(self, 'vode')
        self.output_dim = output_dim 
        self.solver = ode(stateFunction)
        
    def calcOutput(self, t):
        q = self.solver.integrate(t + self.settings['step size'])
        return q

