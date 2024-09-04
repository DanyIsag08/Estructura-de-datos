class Smartphone:
    def __init__(self, marca, modelo, almacenamiento, ram, camara):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.camara = camara

    # Métodos getters y setters
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_almacenamiento(self):
        return self.almacenamiento

    def set_almacenamiento(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def get_ram(self):
        return self.ram

    def set_ram(self, ram):
        self.ram = ram

    def get_camara(self):
        return self.camara

    def set_camara(self, camara):
        self.camara = camara

    def __str__(self):
        return (f"[ marca='{self.marca}', "
                f"modelo='{self.modelo}', "
                f"almacenamiento={self.almacenamiento}GB, "
                f"ram={self.ram}GB, "
                f"camara={self.camara}MP ]")



