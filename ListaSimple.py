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
        nuevoNodo = Nodo_Simple(numero)
        if self.rootNode == None:
            self.rootNode = nuevoNodo
            self.endNode = nuevoNodo
        else:
            tmp = self.rootNode
            while tmp != None:
                
                if nuevoNodo.esMenor(tmp.numero):
                    tmp2= self.rootNode
                    while True:
                        if tmp2.nextNodo.numero == tmp.numero:
                            tmp2.nextNodo = nuevoNodo
                            nuevoNodo.nextNodo = tmp.numero
                            return
                if tmp.nextNodo != None:
                    tmp = tmp.nextNodo
                else:
                    tmp = None
    
    def recorrerLista(self):
        tmp = self.rootNode
        while tmp != None:
            print(tmp.numero)
            if tmp.nextNodo != None:
                tmp = tmp.nextNodo
            else:
                tmp = None
    