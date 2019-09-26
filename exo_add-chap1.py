# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:40:53 2019

@author: tinou
"""

#%%

a = ["a", "a" , "b"]

def rm_doublons(in_list):
    out_list = []
    for e in in_list:
        if e not in out_list:
            out_list.append(e)
    return out_list

"""
def rm2(in_list: list):
    for e in in_list:
        while in_list.count(e) > 1:
            in_list.pop(in_list.index(e))
    return in_list
"""

#%%

def minimum(liste):
    n = len(liste)
    mini = liste[0]
    for i in range (n):
        if liste[i] < mini :
            mini = liste[i]
    return mini + 1

#%%
    
def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d


#%%
    
def inverse(liste):
    liste2 = []
    while len(liste) > 0 :
        liste2.append(liste[-1])
        liste.pop(-1)
    return liste2

#print(a[::-1]) autre méthode





