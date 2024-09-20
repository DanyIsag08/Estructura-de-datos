from cliente import cliente
from BoundedPriorityQueue import BoundedPriorityQueue
def main():
	cola_prioridad = BoundedPriorityQueue(8)

	cliente1 = cliente("nuevo")
	cliente2 = cliente("nuevo")
	cliente3 = cliente("no_cliente")
	cliente4 = cliente("no_cliente")
	cliente5 = cliente("no_cliente")
	cliente6 = cliente("celebridad")
	cliente7 = cliente("frecuente")
	cliente8 = cliente("premium")


	cola_prioridad.encolar(cliente1)
	cola_prioridad.encolar(cliente2)
	cola_prioridad.encolar(cliente3)
	cola_prioridad.encolar(cliente4)
	cola_prioridad.encolar(cliente5)
	cola_prioridad.encolar(cliente6)

	cola_prioridad.imprimir_cola()
	print("Sea atiende y retira 100,000 pesos de su cuenta",cola_prioridad.desencolar())
	cola_prioridad.encolar(cliente7)
	cola_prioridad.encolar(cliente8)
	print("Se atiende a:",cola_prioridad.desencolar())
	cola_prioridad.imprimir_cola()
	print("Se atiende a:",cola_prioridad.desencolar())
	print("Se atiende a:",cola_prioridad.desencolar())
	print("Se atiende a:",cola_prioridad.desencolar())
	print("Se atiende a:",cola_prioridad.desencolar())
	print("Se atiende a:",cola_prioridad.desencolar())
	print("Se atiende a:",cola_prioridad.desencolar())
	cola_prioridad.imprimir_cola()




    

if __name__ == "__main__":
    main()