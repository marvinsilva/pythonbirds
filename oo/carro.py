class Carro:
    def __init__(self, motor, direcao):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0

class Direcao:
    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'

if __name__ == '__main__':

    motor = Motor()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)

    print()

    direcao = Direcao()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    print()

    carro = Carro(motor, direcao)
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.calcular_direcao())

    carro.girar_a_direita()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())