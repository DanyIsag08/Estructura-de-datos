from cliente import cliente
from Queque import Queque
class BoundedPriorityQueue:
    def __init__(self, niveles):
        self._data = [Queque() for _ in range(niveles)]
        self._size = 0

    def encolar(self, cliente):
        prioridad = cliente.nivel
        if 1 <= prioridad <= 5: 
            self._data[prioridad - 1].encolar(cliente) 
            self._size += 1

    def desencolar(self):
        for queue in self._data: 
            if not queue.est_vacia():
                self._size -= 1
                return queue.desencolar()  
        print("No hay más elementos")
        return None


    def longitud(self):
        return self._size

    def est_vacia(self):
        return self.longitud() == 0

    def imprimir_cola(self):
        if self.est_vacia():
            print("La cola está vacía.")
        else:
            print("Cola actual:")
            for queue in self._data:
                queue.imprimir_cola()





                