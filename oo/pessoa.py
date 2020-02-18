class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    marcus = Pessoa(nome='Marcus')
    luciano = Pessoa(marcus, nome='Luciano', idade=55)

    print(Pessoa.cumprimentar(luciano))
    print(luciano.cumprimentar())
    print(id(luciano))
    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(marcus.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(marcus.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(marcus.olhos), id(luciano.olhos))

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
