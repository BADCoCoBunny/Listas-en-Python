class ListaSimple:
    def __init__(self, dato=None) -> None:
        """
        Constructor de la clase ListaSimple.
        Parametros: Object - dato inicial para la lista (opcional)
        """
        if (dato != None):
            self.nodoHead = self.NodoSimple(dato)
        else:
            self.nodoHead = None

    # Adicionar
    def adicionarElemento(self, dato, posicion=None) -> None:
        """
        Adiciona un elemento a la lista. Puede especificarse la posición.
        Parametros: Object - dato a adicionar, int posicion (opcional)
        """
        if (posicion == None):  # Sino se indicó una posición
            nodo_entrada = self.NodoSimple(dato)
            if (self.estaVacia()):
                self.nodoHead = nodo_entrada
            else:
                nodo_actual = self.nodoHead
                while(nodo_actual.siguiente != None):
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_entrada
        else:  # Si se indicó una posición
            nodo_entrada = self.NodoSimple(dato)
            if (0 <= posicion < self.longitud()):  # Si la posición es válida
                if (posicion == 0):
                    self.adicionarInicio(dato)
                elif (posicion == self.longitud()-1):
                    self.adicionarFinal(dato)
                else:
                    nodo_actual = self.nodoHead
                    nodo_preActual = None
                    index = 0
                    while(nodo_actual != None):
                        if (index == posicion):
                            nodo_entrada.siguiente = nodo_actual
                            nodo_preActual.siguiente = nodo_entrada
                            break
                        nodo_preActual = nodo_actual
                        nodo_actual = nodo_actual.siguiente
                        index += 1

    def adicionarInicio(self, dato) -> None:
        """
        Adiciona un elemento al principio de la lista.
        Parametros: Object - dato a adicionar
        """
        nodo_entrada = self.NodoSimple(dato)
        if (self.estaVacia()):
            self.nodoHead = nodo_entrada
        else:
            nodo_entrada.siguiente = self.nodoHead
            self.nodoHead = nodo_entrada

    def adicionarFinal(self, dato) -> None:
        """
        Adiciona un elemento al final de la lista.
        Parametros: Object - dato a adicionar
        """
        nodo_entrada = self.NodoSimple(dato)
        if (self.estaVacia()):
            self.nodoHead = nodo_entrada
        else:
            nodo_actual = self.nodoHead
            while(nodo_actual.siguiente != None):
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_entrada

    # Eliminar
    def eliminar(self, dato, eliminar_todos=False) -> None:
        """
        Elimina la primera o todas las apariciones de un dato en la lista.
        Parametros: object - dato a eliminar
        boolean - true para eliminar todas las apariciones
        """
        if (not self.estaVacia()):
            if(eliminar_todos):
                while(self.apariciones(dato) > 0):
                    self.eliminar(dato)
            else:
                if (self.buscar(dato) == 0):
                    self.eliminarInicial
                if (self.buscar(dato) == self.longitud()-1):
                    self.eliminarFinal()
                nodo_actual = self.nodoHead
                nodo_preActual = None
                while(nodo_actual != None):
                    if (nodo_actual.dato == dato):
                        if (nodo_preActual != None):
                            nodo_preActual.siguiente = nodo_actual.siguiente
                        else:
                            self.eliminarInicial()
                        break
                    nodo_preActual = nodo_actual
                    nodo_actual = nodo_actual.siguiente

    def eliminarPos(self, posicion, eliminar_todos=False) -> None:
        """
        Elimina la primera o todas las apariciones de un dato en una posición
        especifica de la lista.
        Parametros: int - posición del dato a eliminar
        boolean - true para eliminar todas las apariciones
        """
        if (not self.estaVacia()):
            if (0 <= posicion < self.longitud()):
                if (eliminar_todos):
                    dato = self.buscarPos(posicion)
                    while (self.apariciones(dato) > 0):
                        self.eliminar(dato)
                else:
                    if (posicion == 0):
                        self.eliminarInicial()
                    elif (posicion == self.longitud()-1):
                        self.eliminarFinal()
                    else:
                        nodo_actual = self.nodoHead
                        nodo_preActual = None
                        index = 0
                        while (nodo_actual.siguiente != None):
                            if (index == posicion):
                                nodo_preActual.siguiente = nodo_actual.siguiente
                                break
                            nodo_preActual = nodo_actual
                            nodo_actual = nodo_actual.siguiente
                            index += 1

    def eliminarInicial(self) -> None:
        """
        Elimina el primer dato de la lista.
        """
        if(not self.estaVacia()):
            self.nodoHead = self.nodoHead.siguiente

    def eliminarFinal(self) -> None:
        """
        Elimina el último dato de la lista.
        """
        if (not self.estaVacia()):
            nodo_actual = self.nodoHead
            nodo_preActual = None
            while(nodo_actual.siguiente != None):
                nodo_preActual = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_preActual.siguiente = None

    # Buscar
    def buscar(self, dato) -> int:
        """
        Busca la primera posición en la que aparece un dato especifico.
        Parametros: object - dato a buscar
        Retorno: int - posicion del dato buscado
        """
        if (not self.estaVacia()):
            nodo_actual = self.nodoHead
            index = 0
            while(nodo_actual != None):
                if (nodo_actual.dato == dato):
                    return index
                nodo_actual = nodo_actual.siguiente
                index += 1
            return -1  # Si no hay resultados
        else:
            return -1

    def buscarPos(self, posicion) -> object:
        """
        Busca un dato de la lista indicando la posición especifica.
        Parametros: int - posición del dato a buscar
        Retorno: object - dato en la posición especificada
        """
        if (not self.estaVacia()):
            if (0 <= posicion < self.longitud()):
                if (posicion == 0):
                    return self.buscarInicial()
                elif (posicion == self.longitud()-1):
                    return self.buscarFinal()
                else:
                    nodo_actual = self.nodoHead
                    index = 0
                    while (nodo_actual != None):
                        if (index == posicion):
                            return nodo_actual.dato
                        nodo_actual = nodo_actual.siguiente
                        index += 1
            else:
                return None  # Posición no valida
        else:
            return None  # Lista vacía

    def buscarInicial(self) -> object:
        """
        Retorna el dato inicial de la lista.
        Retorno: object - primer dato
        """
        if(not self.estaVacia()):
            return self.nodoHead.dato
        else:
            return None

    def buscarFinal(self) -> object:
        """
        Retorna el dato final de la lista.
        Retorno: object - último dato
        """
        if (not self.estaVacia()):
            nodo_actual = self.nodoHead
            while (nodo_actual.siguiente != None):
                nodo_actual = nodo_actual.siguiente
            return nodo_actual.dato
        else:
            return None

    # Información
    def apariciones(self, dato) -> int:
        """
        Retorna el número de veces que aparece un dato especificado
        en la lista.
        Parametros: Object - dato
        """
        if(self.estaVacia()):
            return 0
        else:
            nodo_actual = self.nodoHead
            apariciones = 0
            while(nodo_actual != None):
                if (nodo_actual.dato == dato):
                    apariciones += 1
                nodo_actual = nodo_actual.siguiente
            return apariciones

    def longitud(self) -> int:
        """
        Muestra la longitud actual de la lista.
        Retorno: int - longitud de la lista
        """
        nodo_actual = self.nodoHead
        num_nodos = 0
        while(nodo_actual != None):
            num_nodos += 1
            nodo_actual = nodo_actual.siguiente
        return num_nodos

    def estaVacia(self) -> bool:
        """
        Muestra el estado actual de la lista, entre vacía y no vacía.
        Retorno: bool - True si está vacía, False sino
        """
        return self.nodoHead == None

    def __str__(self) -> str:
        """
        Retorna un String con una representación de la lista.
        """
        lista_str = ""
        if (self.estaVacia()):
            lista_str += "[]"
            return lista_str
        else:
            lista_str += "[" + str(self.nodoHead)
            nodo_actual = self.nodoHead.siguiente
            while(nodo_actual != None):
                lista_str += ", " + str(nodo_actual)
                nodo_actual = nodo_actual.siguiente
            lista_str += "]"
            return lista_str

    class NodoSimple:
        def __init__(self, dato, siguiente=None) -> None:
            """
            Constructor de la clase NodoSimple.
            Parametros: Object - dato que contendrá el nodo, NodoSimple siguiente (opcional)
            """
            self.dato = dato
            self.siguiente = siguiente

        def __str__(self) -> str:
            return str(self.dato)


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
    lista_numeros.eliminar(2020, False)
    print("Lista: " + str(lista_numeros))
    print("Longitud: " + str(lista_numeros.longitud()))

    print("\n>> Eliminando un elemento en una posición especifica (3)...")
    lista_numeros.eliminarPos(3)
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

    print("\n>> Buscando la posicion de un dato (2)...")
    print("Posición: " + str(lista_numeros.buscar(2)))

    print("\n>> Buscando el dato contenido en un posición especifica (1)...")
    print("Dato: " + str(lista_numeros.buscarPos(1)))
