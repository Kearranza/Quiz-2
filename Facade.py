class Calculadora:

    def __init__(self, Subsistema):

        self._subsistema = Subsistema 

    def operation(self):
        results = []
        results.append("Calculadora inicia los subsistemas:")
        results.append(self._subsistema.sumatoria1())
        results.append("Calculadora manda a realizar las operaciones:")
        results.append(self._subsistema.sumatoria2())
        return "\n".join(results)


class Subsistema:

    def sumatoria1(self):
        return "Subsistema: Calculadora preparando la sumatoria"

    def sumatoria2(self):
        return "Subsistema: Sumatiora realizada"


def client_code(Calculadora):
    print(Calculadora.operation())


subsistema1 = Subsistema()
facade = Calculadora(subsistema1)
client_code(facade)

#Basado en el ejemplo dado por Refactoring guru.