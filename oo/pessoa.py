class Pessoa:

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    marcus = Pessoa(nome='marcus')
    luciano = Pessoa(marcus, nome='luciano', idade=55)

    print(Pessoa.cumprimentar(luciano))
    print(luciano.cumprimentar())
    print(id(luciano))
    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

