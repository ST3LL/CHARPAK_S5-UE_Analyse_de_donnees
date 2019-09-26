# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:42:53 2019

@author: tinou
"""

#%%
#10 nombres random entre 0 et 1
from random import random 

x = []
for i in range (10):
    x.append(random())
print (x) #entre 0 et 1
    
    
#%%
#1à nombres random entre 0 et 10
from random import random 

x = []
for i in range (10):
    x.append(10*random()) #entre 0 et 1
print(x)
    

#%%
#transformer le premier code en comprehension de liste 
from random import random

[random() for i in range(10)]


#%%
#transformer le premier code  à partir de numpy
import numpy as np
from random import random

np.random.random(10)


#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
plt.hist(x)
plt.show() #après manipulation, permet de visualiser (sans le show, on ne peut pas voir le graph)


#%%
#représenter une droite
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
y = 5*x + 1
plt.plot(x,y) #droite sans point
#plt.squatter(x,y) nuage de points 


#%%
#loi normale 
from random import normalvariate

y_normal = [normalvariate(0,1) for i in range(10000)]
plt.hist(y_normal, bins=50, normed=True)
plt.show()


#%%

import numpy as np
from random import random
import matplotlib.pyplot as plt

#np.random.normal(loc=0.0, scale=1.0, size=None)


#display the histogram of the samples, along with the probability density function
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()




