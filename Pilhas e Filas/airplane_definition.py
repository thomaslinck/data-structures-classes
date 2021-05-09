class Airplane:
    def __init__(self, prefixo, nome, companhia):
        self.prefixo = prefixo
        self.nome = nome
        self.companhia = companhia


def print_airplane(airplane):
    if (isinstance(airplane, Airplane)):
        print(airplane.prefixo)
        print(airplane.nome)
        print(airplane.companhia)
    else:
        print("not an airplane")
