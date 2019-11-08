# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:55:18 2019

@author: tinou
"""
import numpy as np

#%%
def moyenne(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return (s/len(l))

def numpy_moyenne(l):
    return np.mean(l)
   
    

#%%   
def nympy_ecarttype(x):
    return np.std(x)



#%%
def produit_scalaire(u,v):
    return sum([x * y for x, y in zip(u, v)])

def numpy_produit_scalaire(u,v):
    return np.dot(u,v)


#%%
def variance(a):
    m = moyenne(a)
    v = 0
    for i in (len(a)):
        v += (a[i]-m)**2
    return (v/len(a))

def nympy_variance(a):
    return np.var(a)


#%%
def covariance(x):
    return np.cov(x)


#%%
def linear(x, params=(0,1)):
    return params[1]*x + params[0] + np.random.normal(size=len(x))




 