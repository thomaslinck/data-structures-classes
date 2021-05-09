from abstract_queue_manager import abstract_queue_manager
from sequential_queue_manager import sequential_queue_manager
from linked_queue_manager import linked_queue_manager


class queue_manager_factory:
    def make(self, tipo) -> abstract_queue_manager:
        implementacoes = {
            "sequential": sequential_queue_manager,
            "linked": linked_queue_manager
        }

        concrete_queue_manager = implementacoes.get(tipo)
        if concrete_queue_manager is not None:
            return concrete_queue_manager()
        else:
            raise Exception()
