# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:55:57 2019

@author: tinou

"""
#Calculer une moyenne
v = range(10)
for i, x in enumerate(v) : 
    print(i, x)
 
    
def moyenne(v):
    pass #votre code à la place de cette ligne
    s = 0
    for x in v:
        s+=x
    return 1/len(v)*s

moyenne(v)

#%%

#Calculer la médiane
def calculate_median(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        return ( l[int((l_len-1)/2)] + l[int((l_len+1)/2)]) / 2 
    else:
        return l[int((l_len-1)/2)]


v = [1, 2, 3,4]

print(calculate_median(v))

#%%

#Calculer le produit scalaire
def produit_scalaire(u,v):
    s = 0
    if len(u) == len(v):
        for i in range (len(u)):
            s += u[i]*v[i]
        return s
    else :
        return "Erreur"
    

def autre_methode(u,v):
    s = 0
    for i, j in zip(u,v):
        s += i*j 
    return s


#compréhension de liste
def comprehension_de_liste(u,v):
    return sum([i*j for i,j in zip(u,v)])




#%%



