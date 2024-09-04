from ListaLigada import ListaLigada 
from Smartphone import Smartphone 
def main():
    celulares = ListaLigada()
    smartphone1 = Smartphone("Apple", "Iphone XS", 64, 4, 12)
    smartphone2 = Smartphone("Samsung", "Samsung S21FE", 256, 8, 32)
    smartphone3 = Smartphone("Apple", "Iphone 13", 256, 4, 12)
    smartphone4 = Smartphone("Apple", "Iphone 14", 256, 6, 12)
    smartphone5 = Smartphone("Samsung", "SamsungZFold6", 512, 12, 50)
    smartphone6 = Smartphone("Apple", "Iphon11Pro", 256, 4, 12)
    smartphone7 = Smartphone("Apple", "IphoneSE", 128, 3, 12)
    smartphone8 = Smartphone("Samsung", "Samsung S20", 128, 6, 32)

    print("Se agregan los 5 elementos:")
    celulares.agregar_al_final(smartphone1)
    celulares.agregar_al_final(smartphone2)
    celulares.agregar_al_final(smartphone3)
    celulares.agregar_al_final(smartphone4)
    celulares.agregar_al_final(smartphone5)
    celulares.transversal()
    print("Se elimina la segunda posicion")
    celulares.eliminar(2)
    celulares.transversal()
    print("Se actualiza")
    celulares.actualizar(smartphone2,smartphone6)
    print("Se agregan elementos tanto al inicio como en el final")
    celulares.insertar_al_inicio(smartphone7)
    celulares.agregar_al_final(smartphone8)
    celulares.transversal()
    print("Se elimina el primer elemento")
    celulares.eliminar_primero()


    #celulares.agregar_despues_de(smartphone4,smartphone6)
    #celulares.eliminar(3)
    #celulares.eliminar_primero()
    #celulares.eliminar_final()
    #print("Posicion:",celulares.buscar(smartphone5))
    #celulares.actualizar(smartphone2,smartphone6)
    celulares.transversal()

    



if __name__ == "__main__":
    main()
