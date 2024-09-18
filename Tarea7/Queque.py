class Queque:
    def __init__(self):
        self.data = []

    def est_vacia(self):
        return len(self.data) == 0

    def longitud(self):
        return len(self.data)

    def frente(self):
        if self.est_vacia():
            return None
        else:
            return self.data[0]

    def encolar(self, valor):  
        self.data.append(valor)

    def desencolar(self):
        if self.est_vacia():
            return None
        else:
            return self.data.pop(0)
        
    def imprimir_cola(self):
        if self.est_vacia():
            print("La cola está vacía.")
        else:
            print("Cola actual:")
            for paciente in self.data:
                print(paciente)

    