import numpy as np
import matplotlib.pylot as plt
%matplolib inline


#ouvrir un fichier .txt et ignorer les 33 premieres lignes
data = np.loadtxt("x01.txt", skiprows=33) #genere un array

#nombres de lignes/colonnes
data.shape

#recuperation de la premiere et de la deuxieme colonne
"""
[:10,0] : début jusqu'a 9e ligne, 1ere colonne
[10:,0] : 9e ligne jusqu'a fin, 1ere colonne
[:20:3,0] : debut jusqu'a 19e ligne de 3 en 3, 1ere colonne
"""
x = data[:,1]
y = data[:,2]

plt.scatter(x,y)
plt.hist(x, bins=100)
plt.show()


from sklearn import linear_model
x = x.reshape(-1,1)
y = y.reshape(-1,1)

regr = linear_model.LinearRegression()
regr.fit(x, y)

#recuperer les coefficients
regr.coef_, regr.intercept_

#coefficient R²
regr.score(x,y)



from sklearn.metrics import r2_score
#coefficient R²
r2_score(x,y)

plt.scatter(x,y)
plt.plot(x, regr.predict(x))
plt.show()

#calculer residus et representer la distribution (gaussienne ou non ?)
residus = y - regr.predict(x)

"""
si pas distribution gaussienne : 
- on retire les extremes
- on change les donner en apportant une transformation
- ?
"""
logx = np.log(x)
logy = np.log(y)

regr = linear_model.LinearRegression()
regr.fit(logx, logy)
regr.coef_, regr.intercept_
regr.score(logx, logy)

r2_score(logx, logy)

plt.scatter(logx, logy)
plt.plot(logx, regr.predict(logx))
plt.show()

residus = logy - regr.predict(logx)
plt.hist(residus, bins=100)