class Airplane:
    def __init__(self, prefixo, nome, companhia):
        self.prefixo = prefixo
        self.nome = nome
        self.companhia = companhia


def print_airplane(airplane):
    print(f"{airplane.prefixo} - {airplane.nome} - {airplane.companhia}"
          if isinstance(airplane, Airplane) else "not an airplane")


def create_airplane():
    print("Digite o prefixo")
    prefixo = input()

    print("Digite o nome")
    nome = input()

    print("Digite a companhia")
    companhia = input()

    return Airplane(prefixo, nome, companhia)
