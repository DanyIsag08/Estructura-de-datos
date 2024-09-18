from paciente import paciente
from Queque import Queque

def main():
    hospital = Queque()
    hospital.encolar(paciente("David", 20, 1.76, 75, 37, "Ninguna"))
    hospital.encolar(paciente("Aaron", 19, 1.70, 75, 37, "Ninguna"))
    hospital.encolar(paciente("Daniel", 23, 1.70, 80, 37, "Sulfas"))
    hospital.imprimir_cola()
    print("Consulta del siguiente: ", hospital.frente())
    print("Atendiendo a:", hospital.desencolar())
    hospital.imprimir_cola()
    hospital.encolar(paciente("Diana", 23, 1.64, 69, 37, "Ninguna"))
    hospital.encolar(paciente("Fabiola", 20, 1.60, 65, 37, "Ninguna"))
    print("Atendiendo a:", hospital.desencolar())
    hospital.imprimir_cola()

if __name__ == "__main__":
    main()
