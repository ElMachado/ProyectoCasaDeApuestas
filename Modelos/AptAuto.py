import numpy as np
import numpy.random as rnd


class AptAuto:
    saldoInicial = 0
    saldoActual = saldoInicial
    valorApostado = 0
    valorGanado = 0
    probabilidadDeGanar = 0.00
    cuotaDeApuesta = 0.00

    @staticmethod
    def estrategiaConservadora():
        AptAuto.probabilidadDeGanar = round(rnd.uniform(0.70, 0.99), 2)
        return AptAuto.probabilidadDeGanar

    @staticmethod
    def estrategiaArriesgada():
        AptAuto.probabilidadDeGanar = round(rnd.uniform(0.01, 0.40), 2)
        return AptAuto.probabilidadDeGanar

    @staticmethod
    def estrategiaDerrochadora():
        AptAuto.valorApostado = rnd.randint(5000, 50000)
        return AptAuto.valorApostado

    @staticmethod
    def estrategiaEconomizadora():
        AptAuto.valorApostado = rnd.randint(2000, 5000)
        return AptAuto.valorApostado

    @staticmethod
    def setCuotaDeApuesta(estraProbGan):
        if estraProbGan == 1:
            estrategia = AptAuto.estrategiaArriesgada()
        else:
            estrategia = AptAuto.estrategiaConservadora()

        AptAuto.cuotaDeApuesta = round(1 / estrategia, 2)
        return AptAuto.cuotaDeApuesta

    @staticmethod
    def setValorGanado():
        AptAuto.valorGanado = AptAuto.valorApostado * AptAuto.cuotaDeApuesta
        return AptAuto.valorGanado

    @staticmethod
    def setSaldoActualGan():
        AptAuto.saldoActual = AptAuto.saldoInicial - AptAuto.valorApostado + AptAuto.valorGanado
        return int(AptAuto.saldoActual)

    @staticmethod
    def setSaldoActualPer():
        AptAuto.saldoActual = AptAuto.saldoInicial - AptAuto.valorApostado
        return AptAuto.saldoActual

    @staticmethod
    def setSaldoInicial():
        AptAuto.saldoInicial = rnd.randint(20000, 100000)

    @staticmethod
    def apuesta(estraProbGan, estraValApos):
        if estraValApos == 1:
            AptAuto.estrategiaDerrochadora()
        else:
            AptAuto.estrategiaEconomizadora()

        u = rnd.rand() * AptAuto.setCuotaDeApuesta(estraProbGan)
        if u <= AptAuto.cuotaDeApuesta:
            AptAuto.setValorGanado()
            AptAuto.setSaldoActualGan()
            print("gano")

        else:
            AptAuto.setSaldoActualPer()
            print("perdio")


# historicoSaldo = np.array([])
# index = np.array([])
# AptAuto.setSaldoInicial()
# for i in range(100):
#     AptAuto.estrategiaArriesgada()
#     AptAuto.estrategiaDerrochadora()
#     AptAuto.apuesta()
#     data = AptAuto.saldoActual
#     index = np.append(index, i)
#     historicoSaldo = np.append(historicoSaldo, data)
#     print("el saldo actual es:", AptAuto.saldoActual)
