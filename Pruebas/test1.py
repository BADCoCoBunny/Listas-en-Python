from Listas.ListaSimple import ListaSimple

if __name__ == "__main__":
    print("\n>> Creando una lista...")
    lista_numeros = ListaSimple()
    print("¿Está vacía? " + str(lista_numeros.estaVacia()))
    print("Longitud: " + str(lista_numeros.longitud()))
    print("Lista: " + str(lista_numeros))

    print("\n>> Adicionando elementos [1, 2, 3]...")
    lista_numeros.adicionarElemento(1)
    lista_numeros.adicionarElemento(2)
    lista_numeros.adicionarElemento(3)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Adicionando un elemento al inicio (0)...")
    lista_numeros.adicionarInicio(0)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Adicionando un elemento al final (4)...")
    lista_numeros.adicionarFinal(4)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Adicionando un elemento en una posición especifica (2020, 3)...")
    lista_numeros.adicionarElemento(2020, 3)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Eliminando un elemento especifico (2020)...")
    lista_numeros.eliminar(2020)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Eliminando inicial...")
    lista_numeros.eliminarInicial()
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Eliminando final...")
    lista_numeros.eliminarFinal()
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))
