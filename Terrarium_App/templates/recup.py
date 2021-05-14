from math import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
import os
savepath = os.path.join("/Users/quentin/PycharmProjects/TerrariumV6/static/Terrarium_App/images", "graphique.png")
os.remove(savepath)

with open("test.txt") as f:
    contents = f.read()

valeur = str(contents)
print(valeur)
sp = valeur.split(";")
del sp[-1]
print(sp)

int_list = list(map(float, sp))
print(int_list)


### Création d'une suite pour simboliser le temps en X

def u(n):
    return floor((n/24)) + float((n/24 - floor(n/24))*0.24)

k = len(int_list)
l = k*6

time = []
for n in range(l):
    if n % 6 == 0:
        time.append(u(n))


print(time)
width = 0.005
plt.bar(time, int_list, width, color='b' )
pylab.xticks(time, int_list, rotation=40)
plt.scatter([i+width/2.0 for i in time], int_list, color='k', s=40)
plt.xlabel("Temps (jour, heure)", size = 16,)
plt.ylabel("Température", size = 16)
plt.title("Graphique de l'évolution de la température",
          fontdict={'family': 'serif',
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})

savepath = os.path.join("/Users/quentin/PycharmProjects/TerrariumV6/static/Terrarium_App/images", "graphique.png")
plt.savefig(savepath)
plt.show()

