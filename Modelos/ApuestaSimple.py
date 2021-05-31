from math import factorial
import random

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
        self.saldoActual = saldoInicial

    def getSaldoInicial(self):
        return self.saldoActual

    def getSaldoActual(self):
        return self.saldoActual

    def getvalorApostado(self):
        return self.saldoActual

    def getvalorGanado(self):
        return self.saldoActual

    def getprobabilidadDeGanar(self):
        return self.saldoActual

    def getcuotaDeApuesta(self):
        return self.saldoActual

    def setCuotaDeApuesta(self):
        self.cuotaDeApuesta = 1 / self.probabilidadDeGanar
        return round(self.cuotaDeApuesta, 2)

    def setValorGanado(self):
        self.valorGanado = self.valorApostado * self.cuotaDeApuesta
        return self.valorGanado.__int__()

    def setSaldoActualGan(self):
        self.saldoActual = self.saldoInicial - self.valorApostado + self.valorGanado
        return self.saldoActual.__int__()

    def setSaldoActualPer(self):
        self.saldoActual = self.saldoInicial - self.valorApostado + 0
        return self.saldoActual.__int__()

    def apuesta(self):
        u = rnd.rand()
        if u <= self.probabilidadDeGanar:
            self.setCuotaDeApuesta()
            self.setValorGanado()
            self.setSaldoActualGan()
            return 0
        else:
            self.setSaldoActualPer()
            return 1