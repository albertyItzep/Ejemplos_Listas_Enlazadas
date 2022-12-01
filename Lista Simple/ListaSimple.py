from NodoSimple import Nodo_Simple


class Lista_Simple:
    def __init__(self) -> None:
        self.rootNode = None
        self.endNode = None
        self.size = 0


    
    """
        Agregamos valores al final de la lista
        1 -> 2 -> 3 -> Agregamos Valor
    """
    def insertarFinal(self,numero:int):
        nuevoNodo = Nodo_Simple(numero)
        if self.rootNode == None:
            self.rootNode = nuevoNodo
            self.endNode = nuevoNodo
        else:
            self.endNode.nextNodo = nuevoNodo
            self.endNode = nuevoNodo
        self.size+=1



    """
        Agregamos al Inicio de la lista
        agregamos -> 1 -> 2 -> 3 
    """
    def insertarInicio(self,numero:int):
        nuevoNodo = Nodo_Simple(numero)
        if self.rootNode == None:
            self.rootNode = nuevoNodo
            self.endNode = nuevoNodo
        else:
            nuevoNodo.nextNodo = self.rootNode
            self.rootNode = nuevoNodo
        self.size+=1


    """
        Insercion Ordenada
        Validamos con metodo de Nodo si el numero es menor o mayor a la posicion del recorrido del While
        de ser menor recorremos nuevamente para realizar la insercion en donde es requerido
        ejemplo: 3  
            1 -> 2 -> 4  -> 5
            1 < 3
            2 < 3
            3 < 4
            realizamos recorrido e insertamos
            1 -> 2 -> 3 -> 4 -> 5
    """
    def insertarOrden(self,numero:int):
        if self.rootNode == None:
            nuevoNodo = Nodo_Simple(numero)
            self.rootNode = nuevoNodo
            self.endNode = nuevoNodo
            self.size+=1
        else:
            if self.rootNode == self.endNode:
                if self.rootNode.numero < numero:
                    self.insertarFinal(numero)
                else:
                    self.insertarInicio(numero)
            else:
                nuevoNodo = Nodo_Simple(numero)
                posicion = 0
                tmp = self.rootNode
                if nuevoNodo.numero < self.rootNode.numero:
                    self.insertarInicio(numero)
                    self.size +=1
                    return
                if nuevoNodo.numero > self.endNode.numero:
                    self.insertarFinal(numero)
                    self.size+=1
                    return
                for x in range(self.size):
                    if nuevoNodo.esMenor(tmp.numero):
                        posicion = x
                        tmp2 = self.rootNode
                        for i in range(posicion):
                            if i == x-1:
                                nuevoNodo.nextNodo = tmp2.nextNodo
                                tmp2.nextNodo = nuevoNodo
                                self.size+=1
                                return
                            tmp2 = tmp2.nextNodo

                    else:
                        tmp = tmp.nextNodo
    

    """
        Recibe un numero y realiza la busqueda por el numero ingresado
    """
    def busquedaNumero(self,numero:int):
        tmp = self.rootNode
        for x in range(self.size):
            if tmp.numero == numero:
                return tmp
            tmp = tmp.nextNodo
        return None


    """
        Recibe la posicion a la que deseamos obtenerle el valor
    """
    def busquedaPosicion(self,posicion:int):
        tmp = self.rootNode
        for x in range(self.size):
            if x  == posicion:
                return tmp
            tmp = tmp.nextNodo
        return None

    """
        eliminamos el valor seleccionado
    """
    def eliminarNumero(self,numero:int):
        if self.size > 0:
            tmp = self.rootNode
            if self.rootNode.numero == numero:
                self.rootNode = self.rootNode.nextNodo
                self.size-=1
                return                
            for x in range(self.size):
                if tmp.numero == numero:
                    tmp2 = self.rootNode
                    for i in range(x):
                        if i == x-1:
                            if tmp.nextNodo!= None:
                                tmp2.nextNodo = tmp.nextNodo
                                self.size-=1
                                return
                            else:
                                tmp2.nextNodo = None
                                self.size-=1
                                return
                        tmp2 = tmp2.nextNodo
                tmp = tmp.nextNodo
            return
    """
        eliminamos por posicion
    """
    def eliminarPosicion(self,posicion:int):
        if self.size > 0 and posicion <= self.size and posicion >= 0:
            if posicion == 0:
                self.rootNode = self.rootNode.nextNodo
                self.size-=1
                return
            if posicion == self.size:
                tmp = self.rootNode
                for x in range(self.size):
                    if x == self.size-1:
                        tmp. nextNodo = None
                        self.endNode = tmp
                        self.size-=1
                        return
                    tmp = tmp.nextNodo
            tmp = self.rootNode
            for x in range(posicion):
                if x == posicion-1:
                    tmp2 = tmp
                    tmp = tmp.nextNodo
                    tmp2.nextNodo = tmp.nextNodo
                    self.size -=1
                    return
                tmp = tmp.nextNodo
        return

    def recorrerLista(self):
        tmp = self.rootNode
        while tmp != None:
            print(tmp.numero)
            if tmp.nextNodo != None:
                tmp = tmp.nextNodo
            else:
                tmp = None 
    
lista = Lista_Simple()

#lista.insertarFinal(2)
#lista.insertarFinal(7)
#lista.insertarFinal(4)
#lista.insertarFinal(3)
#lista.insertarInicio(1)
#lista.recorrerLista()

lista.insertarOrden(2)
lista.insertarOrden(7)
lista.insertarOrden(4)
lista.insertarOrden(3)
lista.insertarOrden(1)
lista.insertarOrden(8)
lista.insertarOrden(6)
lista.insertarOrden(5)
lista.insertarOrden(51)
lista.insertarOrden(11)
lista.insertarOrden(10)
lista.insertarOrden(22)

valor1 = lista.busquedaNumero(10)
valor2 = lista.busquedaPosicion(5)
print("Busqueda 1: " + str(valor1.numero))
print("Busqueda 2: " + str(valor2.numero))
lista.recorrerLista()
lista.eliminarPosicion(5)
print("\n")
lista.recorrerLista()
