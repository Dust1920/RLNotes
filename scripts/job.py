"""
    Computing v_1 and w_1^* 
"""

import numpy as np
from scipy.special import gamma
from scipy.special import beta

def factorial(x: int):
    """
        Define Factorial Function
    """
    y = gamma(x + 1)
    return y


def comb_function(n,x):
    """
        Combinatory Function
    """
    y = factorial(n) / (factorial(x) * factorial(n - x))
    return y


def beta_binomial(n: int, x, palpha, pbeta):
    """
        Beta Binomial Distribution
    """
    y = comb_function(n, x) * beta(x + palpha, n - x + pbeta) / beta(palpha, pbeta)
    return y


class JobModel:
    """
        Best Job model
    """
    def __init__(self, r, c, w, n, vpar):
        """
            Principal Job Parameters
        """
        self.discount = r
        self.alt_cost = c
        self.dom_var = w
        self.var_grid = n
        self.rv = None
        self.random_pars = vpar
        self.var = np.linspace(w[0], w[1], self.var_grid)


    def simulate_rv(self):
        """
            Simulate Random Variables
        """
        try:
            rv_name = self.random_pars['BetaBinomial']
            self.rv = [beta_binomial(rv_name['n'],
                                     k,
                                     rv_name['a'],
                                     rv_name['b']) for k in range(self.var_grid)]
            print("A", self.rv)
            return None
        except ValueError:
            return "Variable Aleatoria NO Disponible"


    def h_1(self, w):
        """
            Computes lifetime value at t=1 given current 
            wage w_l = w.      
        """
        smax = [max(self.alt_cost, s) for s in self.var]
        expected_w = np.sum(np.array(smax) * self.rv)
        h1 = self.alt_cost + self.discount * expected_w
        s = w + self.discount * w
        g = max(s, h1)
        return g


BETA = 0.95
ALT_COST = 10
JOB_DOM = (10.0,60.0)
N = 51
RANDOM_PARS = {'BetaBinomial':{"n": N,
                               "a":200,
                               "b":100}}


BEST_JOB = JobModel(BETA, ALT_COST, JOB_DOM, N, RANDOM_PARS)
BEST_JOB.simulate_rv()

print(BEST_JOB.h_1(1.0))
