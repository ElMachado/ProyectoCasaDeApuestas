import numpy.random as rnd


class AptAuto:
    saldoInicial = 0
    saldoActual = saldoInicial
    saldoAnterior = 0
    valorApostado = 0
    valorGanado = 0
    probabilidadDeGanar = 0.00
    cuotaDeApuesta = 0.00
    terminarApuesta = 0

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
        if AptAuto.saldoActual > 30000:
            AptAuto.valorApostado = rnd.randint(30000, 100000)
            return AptAuto.valorApostado
        else:
            AptAuto.terminarApuesta = 1

    @staticmethod
    def estrategiaEconomizadora():
        if AptAuto.saldoActual > 2000:
            AptAuto.valorApostado = rnd.randint(2000, 30000)
            return AptAuto.valorApostado
        else:
            AptAuto.terminarApuesta = 1

    @staticmethod
    def setCuotaDeApuesta(estraProbGan):
        if estraProbGan == 2:
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
        AptAuto.saldoActual = AptAuto.saldoAnterior - AptAuto.valorApostado + AptAuto.valorGanado
        AptAuto.saldoAnterior = AptAuto.saldoActual
        return int(AptAuto.saldoActual)

    @staticmethod
    def setSaldoActualPer():
        AptAuto.saldoActual = AptAuto.saldoAnterior - AptAuto.valorApostado
        AptAuto.saldoAnterior = AptAuto.saldoActual
        return int(AptAuto.saldoActual)

    @staticmethod
    def setSaldoInicial():
        AptAuto.saldoInicial = rnd.randint(30000, 100000)
        return AptAuto.saldoInicial

    @staticmethod
    def apuesta(estraProbGan, estraValApos):
        if estraValApos == 4:
            AptAuto.estrategiaDerrochadora()
        else:
            AptAuto.estrategiaEconomizadora()
        AptAuto.setCuotaDeApuesta(estraProbGan)
        u = rnd.rand()
        if u <= AptAuto.probabilidadDeGanar:
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
