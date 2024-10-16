from NodoArbol import NodoArbol
def main():
    
    raiz = NodoArbol("Diego")
    raiz.set_hijo_izquierdo(NodoArbol("Pedro"))
    raiz.set_hijo_derecho(NodoArbol("Mario"))
    raiz.get_hijo_izquierdo().set_hijo_izquierdo(NodoArbol("Susan"))
    raiz.get_hijo_izquierdo().set_hijo_derecho(NodoArbol("Diana"))
    print(raiz)

    print("------------")

    raiz2 = NodoArbol("10")
    raiz2.set_hijo_izquierdo(NodoArbol(5))
    raiz2.set_hijo_derecho(NodoArbol(15))
    raiz2.get_hijo_izquierdo().set_hijo_izquierdo(NodoArbol(1))
    raiz2.get_hijo_derecho().set_hijo_derecho(NodoArbol(25))
    print(raiz2)

if __name__ == "__main__":
    main()