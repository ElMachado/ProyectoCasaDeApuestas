import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt
class Apuesta():
    saldoInicial = 0
    saldoActual = 0
    valorApostado = 0
    valorGanado = 0
    probabilidadDeGanar = 0.00
    cuotaDeApuesta = 0.00

    def __init__(self, saldoInicial, valorApostado, probabilidadDeGanar):
        self.saldoInicial = saldoInicial
        self.valorApostado = valorApostado
        self.probabilidadDeGanar = probabilidadDeGanar

    def setCuotaDeApuesta(self):
        self.cuotaDeApuesta = 1 / self.probabilidadDeGanar
        return round(self.cuotaDeApuesta,2)


    def setValorGanado(self):
        self.valorGanado = self.valorApostado * self.cuotaDeApuesta
        return self.valorGanado.__int__()

    def setSaldoActual(self):
        self.saldoActual = self.saldoInicial - self.valorApostado + self.valorGanado
        return self.saldoActual.__int__()

    def apostar(self):


        b = self.setCuotaDeApuesta()
        c = self.setValorGanado()
        a = self.setSaldoActual()
        print(f"la apuesta dio como resultado {b} {c} {a}")

apuesta = Apuesta(8000, 4000, 0.75)
apuesta.apostar()
AG=np.array([])
for i in range(10000):
    u = rnd.rand()*apuesta.probabilidadDeGanar
    if(u>=1):
      G="Gano"
    else:
      G="perdio"
    AG=np.append(AG,G)
plt.hist(AG,bins=2,range=[0,1],rwidth=0.8,align="left")