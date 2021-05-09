
class linked_queue_node:

    class descritor:
        def __init__(self, inicio, fim, tamanho):
            self.inicio = inicio
            self.fim = fim
            self.tamanho = tamanho

    def __init__(self, airplane, predecessor, sucessor):
        self.airplane = airplane
        self.predecessor = predecessor
        self.sucessor = sucessor
