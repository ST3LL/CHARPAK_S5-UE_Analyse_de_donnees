# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:43:34 2019

@author: tinou
"""

#%%
import numpy as np

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
    if size > len(x) : 
        size = len(x)
    index = np.arange(x.size)
    np.random.shuffle(index)
    return index[:size] #récupère les 10 premiers éléments

"""
---> Explication :
    - Génère l'index de x
    - Mélange la liste et prend les 10 premiers éléments de x correspondant à 10 éléments random dans la liste
"""

for i in range(10):
    print(x[sample_index(x, 10)].mean()) #récupérer un bout de x
    
    
#%%
import numpy as np
import matplotlib.pyplot as plt
    
N_iterations = 10000


plt.hist(sampled, bins=100, density=True)
    
    
    
    
    
    
    