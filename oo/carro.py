
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:
    girar_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    girar_a_esquerdaa_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.girar_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.girar_a_esquerdaa_dct[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()


direcao = Direcao()
motor = Motor()
carro = Carro(direcao, motor)
carro.girar_a_direita()
carro.motor.acelerar()
for _ in range(63):
    carro.motor.acelerar()
    carro.girar_a_direita()


print(carro.calcular_direcao(), carro.calcular_velocidade())
