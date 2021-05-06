# Exercísio de polimorfismo
class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(f'{nome}')

pessoa = Pessoa()
pessoa.apresentar('Amanda', 21, 'Programadora')
pessoa.apresentar('Amanda', 21)
pessoa.apresentar('Amanda')