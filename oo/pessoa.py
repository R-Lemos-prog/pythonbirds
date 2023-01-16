class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=5):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, objeto de id "{id(self)}"!'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    catarina = Pessoa(nome='Catarina')
    raiene = Pessoa(catarina, nome='Raiene', idade= 23)
    print(Pessoa.cumprimentar(catarina))
    print(f'{catarina.nome} tem {catarina.idade} anos de idade.')
    print(f'{raiene.nome} tem {raiene.idade} anos de idade.')
    for filho in raiene.filhos:
        print(f'{filho.nome} com {filho.idade} anos de idade.')
    catarina.sobrenome = 'Archetti'
    print(f'{catarina.nome} {catarina.sobrenome}')
    raiene.olhos = 1
    print(raiene.__dict__)
    print(catarina.__dict__)
    raiene.altura = 1.75
    print(raiene.__dict__)
    del raiene.altura
    del raiene.filhos
    print(raiene.__dict__)
    #print(Pessoa.nome)
    print(Pessoa.olhos)
    print(catarina.olhos)
    print(id(Pessoa.olhos), id(catarina.olhos))
    Pessoa.olhos = 3
    print(catarina.olhos)
    print(raiene.olhos)
    del raiene.olhos
    print(raiene.olhos)
    print(Pessoa.metodo_estatico(), raiene.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), raiene.nome_e_atributos_de_classe())
