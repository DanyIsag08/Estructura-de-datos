class paciente:
    def __init__(self, nombre, edad, altura, peso, temperatura, alergias):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.temperatura = temperatura
        self.alergias = alergias

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_temperatura(self):
        return self.temperatura

    def set_temperatura(self, temperatura):
        self.temperatura = temperatura

    def get_alergias(self):
        return self.alergias

    def set_alergiar(self, alergias):
        self.alergias = alergias

    def __str__(self):
        return (f"[ nombre='{self.nombre}', "
                f"edad={self.edad}años, "
                f"altura={self.altura}m, "
                f"peso={self.peso}kg, "
                f"temperatura={self.temperatura}°, "
                f"alergias='{self.alergias}'] ")



