class cliente:
    def __init__(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente
        self.nivel = self.asignar_nivel(tipo_cliente)

    def asignar_nivel(self, tipo_cliente):
        prioridades = {
            "celebridad": 1,  
            "premium": 2,     
            "frecuente": 3,   
            "nuevo": 4,       
            "no_cliente": 5   
        }
        return prioridades.get(tipo_cliente, None)

    def __str__(self):
        return (f"[ nivel='{self.nivel}', "
                f"tipo_cliente='{self.tipo_cliente}'] ")

