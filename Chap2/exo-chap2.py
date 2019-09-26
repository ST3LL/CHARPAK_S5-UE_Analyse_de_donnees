# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:43:34 2019

@author: tinou
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(100,200, size=10000)
print('shape x : ', x.shape)
print('10 first elements of x : \n', x[:10])


print("true mean is", x.mean())



def sample_index(x, size):
    """sample random elements and return array index with length defined by size
    
        Args:
            x (numpy.array) : vector to sample from
        Returns:
            numpy.array with length defined by size
    """
    return np.random.normal(size=len(x)) 