class Calculadora(object):

    def __init__(self):
        self.numeros = []

    def add_numero(self, numero):
        self.numeros.append(numero)

    def somar(self):
        soma = 0
        for numero in self.numeros:
            soma += numero
        return soma
