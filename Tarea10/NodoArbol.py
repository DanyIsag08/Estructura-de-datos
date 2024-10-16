class NodoArbol:
    def __init__(self, dato=None, hijo_izquierdo=None, hijo_derecho=None):
        self.dato = dato
        self.hijo_izquierdo = hijo_izquierdo
        self.hijo_derecho = hijo_derecho

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_hijo_izquierdo(self):
        return self.hijo_izquierdo

    def set_hijo_izquierdo(self, hijo_izquierdo):
        self.hijo_izquierdo = hijo_izquierdo

    def get_hijo_derecho(self):
        return self.hijo_derecho

    def set_hijo_derecho(self, hijo_derecho):
        self.hijo_derecho = hijo_derecho

    def __eq__(self, other):
        if isinstance(other, NodoArbol):
            return self.dato == other.dato
        return False

    def __hash__(self):
        return hash(self.dato)

    def __str__(self):
        return f"NodoArbol(dato={self.dato}, hijo_izquierdo={self.hijo_izquierdo}, hijo_derecho={self.hijo_derecho})"
