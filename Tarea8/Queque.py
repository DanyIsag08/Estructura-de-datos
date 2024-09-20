class Queque:
    def __init__(self):
        self.data = []

    def est_vacia(self):
        return len(self.data) == 0

    def encolar(self, valor):  
        self.data.append(valor)

    def desencolar(self):
        if self.est_vacia():
            return None
        else:
            return self.data.pop(0)
        
    def imprimir_cola(self):
        if self.est_vacia():
            return  
        else:
            for cliente in self.data:
                print(cliente)