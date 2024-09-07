class NodoDoble:
    def __init__(self, data=None, siguiente=None, anterior=None):
        self.data = data
        self.siguiente = siguiente
        self.anterior = anterior

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def get_anterior(self):
        return self.anterior

    def set_anterior(self, anterior):
        self.anterior = anterior