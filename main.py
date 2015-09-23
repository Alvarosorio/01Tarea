from split import *
from planck import *
import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy import units as u


#Cargamos los datos
T = np.loadtxt("sun_AM0.dat")

#La funcion split ordena los datos en una matriz
#Es un poco estupido pero es por una cosa de comodidad
D = split(T)

#El tamano de esta matriz
n = D.shape

#integracion numerica de los datos

I = 0
for j in range(0, n[1]-1):
    gap = D[0, j+1] - D[0, j]
    trap = ((D[1, j] + D[1, j+1]) * gap/2)
    I += trap

#integracion numerica de la funcion de Planck
#No podemos partir el calculo de la integral desde cero
#ya que la funcion se indefine en este valor
ini = 0.000001
fin = np.pi/2

#discretizamos el domino a integrar
delta = np.linspace(ini, fin, num=1000)
m = delta.shape

S = 0
#Como los deltas son los mismos lo calculamos solo una vez
paso = (delta[1] - delta[0])/2

for k in range(0, m[0]-2):
#la funcion planck es la integral a resolver luego de aplicar el cambio de variables
    simp = (paso/3.0) * (planck(delta[k]) + 4*(planck(delta[k+1])) + planck(delta[k+2]))
    S += simp

#Tenemos que la temperatura que mas se aproxima a la del sol es 5778 K
temp = 5778 * u.K

#La constante que acompana la integral
P = ((2*np.pi*const.h)/((const.c)**2)) * ((const.k_B*temp)/(const.h))**4
#el valor final de la funcion de Planck
P = P*S
a = const.au

#Tenemos que el radio del sol esta dada por la conservacion del flujo

RS = (np.sqrt(I/P.value))*a

print "Constante solar =", I
print "Integral de la funcion de Planck", P
print "Radio  del Sol", RS

plt.plot(D[0, 0:1500], D[1, 0:1500])
plt.title('Espectro del Sol')
plt.xlabel('Longitud de Onda $[nm]$', fontsize=15)
plt.ylabel('Flujo $[w/m^2 nm^1]$', fontsize=15)

plt.show()
