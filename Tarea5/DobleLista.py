from NodoDoble import NodoDoble
class DobleLista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanio = 0

    def esta_vacia(self):
        res = False
        if self.head == None and self.tail == None:
            res = True
        return res

    def get_tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.esta_vacia():
            self.head = nuevo
            self.tail = nuevo
        else:
            nuevo.siguiente = self.head
            self.head.anterior = nuevo
            self.head = nuevo
        self.tamanio += 1

    def transversal(self, direccion):
        if direccion == 1:
            aux = self.tail
            while aux != None:
                print(aux.data, end = "<--")
                aux = aux.anterior
        else:
            aux = self.head
            while aux != None:
                print(aux.data, end = "-->")
                aux = aux.siguiente
        print("")
        

    def agregar_despues_de(self, referencia, valor):
        aux = self.head
        while aux != None and aux.data != referencia:
            aux = aux.siguiente
        
        if aux == None:
            print("No existe la referencia!!!")
        else:
            nuevo = NodoDoble(valor)
            nuevo.siguiente = aux.siguiente
            nuevo.anterior = aux
            if aux.siguiente is not None:
                aux.siguiente.anterior = nuevo
            else:
                self.tail = nuevo
            aux.siguiente = nuevo
            self.tamanio += 1

    def agregar_al_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.esta_vacia():
            self.head = nuevo
            self.tail = nuevo
        else:
            nuevo.anterior = self.tail
            self.tail.siguiente = nuevo
            self.tail = nuevo
        self.tamanio += 1

    def obtener(self, valor):
        contador = 1
        aux = self.head
        if aux is None:
            print("No existe la referencia!!!")
        else:
            while aux != None:
                if contador == valor:
                    print("Valor solicitado", aux.data)
                contador += 1
                aux = aux.siguiente

    def eliminar_primero(self):
        if self.head == None:
            print("No existe la referencia!!!")
        else:
            self.head = self.head.siguiente
            self.head.anterior = None
            self.tamanio -=1

    def eliminar_final(self):
        if self.tail == None:
            print("No existe la referencia!!!")
        else:
            self.tail = self.tail.anterior
            self.tail.siguiente = None
            self.tamanio -=1

    def eliminar(self, posicion):
        aux=self.head
        posicion -=1
        for _ in range(posicion - 1):
            aux = aux.siguiente
        aux.siguiente = aux.siguiente.siguiente
        self.tamanio -=1

    def buscar(self, valor):
        contador = 1
        aux = self.head
        while aux.siguiente is not None:
            if aux.data == valor:
                return contador
            aux=aux.siguiente
            contador +=1
        print("No se encontro")
        

    def actualizar(self, a_buscar, valor):
        aux = self.head
        while aux.data != None:
            if aux.data == a_buscar:
                aux.data = valor
                return
            aux=aux.siguiente
