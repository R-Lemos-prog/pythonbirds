class Pessoa:
    def __init__(self, *filhos, nome=None, idade=5):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, objeto de id "{id(self)}"!'


if __name__ == '__main__':
    catarina = Pessoa(nome='Catarina')
    raiene = Pessoa(catarina, nome='Raiene', idade= 23)
    print(Pessoa.cumprimentar(catarina))
    print(f'{catarina.nome} tem {catarina.idade} anos de idade.')
    print(f'{raiene.nome} tem {raiene.idade} anos de idade.')
    for filho in raiene.filhos:
        print(f'{filho.nome} com {filho.idade} anos de idade.')
