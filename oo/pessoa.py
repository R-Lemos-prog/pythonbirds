class Pessoa:
    def __init__(self, nome=None, idade=16):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, {id(self)}!'


if __name__ == '__main__':
    p = Pessoa('Catarina')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Raiene'
    print(p.nome)
    print(p.idade)
    p.idade = 23
    print(p.idade)
    print(f'{p.nome} tem {p.idade} anos de idade.')
