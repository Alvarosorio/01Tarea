from scipy.integrate import *
from split import *
import numpy as np

#En este script se compara el algoritmo implementado para calcular el Espectro
#del sol con la funcion de scipy integrate.trapz

#Cargamos los datos
T = np.loadtxt("sun_AM0.dat")

#La funcion split ordena los datos en una matriz
#Es un poco estupido pero es por una cosa de comodidad
D = split(T)

#El tamano de esta matriz
n = D.shape

#integracion ordinaria, mas ordinaria que el vino en bolsa

I = 0
for j in range(0, n[1]-1):
    gap = D[0, j+1] - D[0, j]
    trap = ((D[1, j] + D[1, j+1]) * gap/2)
    I += trap

T = trapz(D[1, :], x=D[0, :])

print "Metodo Implementado =", I
print "integrate.trapz =", T
