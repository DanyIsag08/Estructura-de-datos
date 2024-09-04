from Nodo import Nodo
from Smartphone import Smartphone
class ListaLigada:
    def __init__(self):
        self.head = None
        self.tamanio = 0

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
        else:
            aux = self.head
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
        self.tamanio += 1

    def transversal(self):
        aux = self.head
        while aux != None:
            print(aux.dato, end=" --> ")
            aux = aux.siguiente
        print("")

    def esta_vacia(self):
        if self.head is None:
            print("Está vacía")
            return True
        else:
            print("No está vacía")
            return False

    def insertar_al_inicio(self, dato):
        self.head = Nodo(dato, self.head)
        self.tamanio += 1

    def get_tamanio(self):
        return self.tamanio

    def agregar_despues_de(self, valoref, dato):
        aux=self.head
        while aux != None:
            if aux.dato == valoref:
                nuevo = Nodo(dato)
                aux.siguiente = nuevo
                self.tamanio += 1
                return
            aux=aux.siguiente

    def eliminar(self, posicion):
        aux=self.head
        for _ in range(posicion - 1):
            aux = aux.siguiente
        aux.siguiente = aux.siguiente.siguiente
        self.tamanio -=1

    def eliminar_primero(self):
        self.head = self.head.siguiente
        self.tamanio -=1

    def eliminar_final(self):
        aux = self.head
        while aux.siguiente.siguiente != None:
            aux = aux.siguiente
        aux.siguiente=None
        self.tamanio -=1

    def buscar(self, dato):
        contador = 0
        aux = self.head
        while aux.dato != None:
            if aux.dato == dato:
                return contador
            aux=aux.siguiente
            contador +=1

    def actualizar(self, a_buscar, dato):
        aux = self.head
        while aux.dato != None:
            if aux.dato == a_buscar:
                aux.dato = dato
                return
            aux=aux.siguiente

        
        







