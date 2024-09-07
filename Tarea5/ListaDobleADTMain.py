from DobleLista import DobleLista
def main():
	numeros = DobleLista()
	print("Se agregan los datos:")
	numeros.agregar_al_inicio(50)
	numeros.agregar_al_final(60)
	numeros.agregar_al_final(65)
	numeros.agregar_al_final(70)
	numeros.agregar_al_final(80)
	numeros.agregar_al_final(90)
	numeros.transversal(0)
	print("Se elimina la posicion 2")
	numeros.eliminar(2)
	numeros.transversal(0)
	print("Se actualiza el 80 por 88")
	numeros.actualizar(80, 88)
	numeros.transversal(0)
	print("Se realiza la busqueda")
	print(numeros.buscar(80))


if __name__ == "__main__":
    main()