from scipy.integrate import *
from split import *
import numpy as np
from planck import *
import time

#En este script se compara el algoritmo implementado para calcular la funcion
#de planck con la funcion de scipy integrate.quad



#Integracion numerica de la funcion de Planck
#No podemos partir el calculo de la integral desde cero
#ya que la funcion se indefine en este valor
ini = 0.000001
fin = np.pi/2
start_1 = time.time()
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
time_1 = time.time() - start_1

start_2 = time.time()
I, err = quad(planck, 0, np.pi/2)
time_2 = time.time() - start_2


print "Metodo Implementado =", S, "Tiempo =", time_1 
print "integrate.quad =", I, "Tiempo =", time_2 
print "diferencia =", I-S
