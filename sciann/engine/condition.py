""" Condition class to constrain the training.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from ..utils import *


class Condition(object):
    """ Configures the condition to impose constraint.

    # Arguments
        var: The layer name to impose the constraint.
        cond: A callable handle to function that imposes the condition.
        ids: A 1D numpy arrays consists of node-ids to impose the condition.
        sol: The true (expected) value for the `var` layer.
        name: A `str` to be associated to the constraint.

    # Returns

    # Raises
        ValueError if `model` is not of class `SciModel`.
    """
    def __init__(self,
                 var=None,
                 cond=None,
                 ids=None,
                 sol=None,
                 name=None):
        # check the inputs.
        assert isinstance(var, (str, type(None))), \
            "Expected a Layer Name of type str. "
        assert (cond is None or callable(cond) or K.is_tensor(cond)), \
            "Expected a function or a Tensor as input. "

        if ids is not None:
            assert all([isinstance(ids, np.ndarray), ids.ndim==1]), \
                "Expected a 1d numpy array for \"ids\". "
        
        if sol is not None: 
            sol = to_list(sol)
            assert all([isinstance(x, np.ndarray) for x in sol]), \
                "Expected a list of numpy array for \"sol\". "
        
        assert isinstance(name, (str, type(None))), \
            "Expected a string input for the name. "
        
        self.var = var
        self.cond = cond
        self.ids = ids
        self.sol = sol
        self.name = name

    def __call__(self):
        return self.cond

    def eval(self, xs):
        return self.cond.eval(xs)
