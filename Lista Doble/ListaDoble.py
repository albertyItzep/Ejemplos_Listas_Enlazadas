from Nodo import Nodo


class ListaDoble:
    def __init__(self) -> None:
        self.size = 0
        self.nodoRaiz = None
        self.nodoFinal = None
    
    """
        Agregamos valores al final de la lista
        1 -> 2 -> 3 -> Agregamos Valor
    """
    def insertarFinal(self,numero:int):
        nuevoNodo = Nodo(numero)
        self.size+=1
        if self.nodoRaiz == None:
            self.nodoRaiz = nuevoNodo
            self.nodoFinal = nuevoNodo
        else:
            self.nodoFinal.siguienteNodo = nuevoNodo
            nuevoNodo.anteriorNodo = self.nodoFinal
            self.nodoFinal = nuevoNodo
    
    """
        Agregamos al Inicio de la lista
        agregamos -> 1 -> 2 -> 3 
    """
    def insertarInicio(self,numero:int):
        nuevoNodo = Nodo(numero)
        self.size+=1
        if self.nodoRaiz == None:
            self.nodoRaiz = nuevoNodo
            self.nodoFinal = nuevoNodo
        else:
            nuevoNodo.siguienteNodo = self.nodoRaiz
            self.nodoRaiz.anteriorNodo = nuevoNodo
            self.nodoRaiz = nuevoNodo

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
        if self.nodoRaiz == None:
            nuevoNodo = Nodo(numero)
            self.nodoRaiz = nuevoNodo
            self.nodoFinal = nuevoNodo
            self.size+=1
        else:
            if self.nodoRaiz == self.nodoFinal:
                if numero < self.nodoRaiz.numero:
                    self.insertarInicio(numero)
                    return
                else:
                    self.insertarFinal(numero)
                    return
            else:
                if numero < self.nodoRaiz.numero:
                    self.insertarInicio(numero)
                    return
                if numero > self.nodoFinal.numero:
                    self.insertarFinal(numero)
                    return
                nuevoNodo = Nodo(numero)
                tmp = self.nodoRaiz
                for x in range(self.size):
                    if nuevoNodo.esMenor(tmp.numero):
                        tmp.anteriorNodo.siguienteNodo = nuevoNodo
                        nuevoNodo.anteriorNodo = tmp.anteriorNodo
                        tmp.anteriorNodo = nuevoNodo
                        nuevoNodo.siguienteNodo = tmp
                        self.size+=1
                        return
                    tmp = tmp.siguienteNodo
            return

    """
        Recibe un numero y realiza la busqueda por el numero ingresado
    """
    def busquedaNumero(self,numero:int):
        tmp = self.nodoRaiz
        for x in range(self.size):
            if tmp.numero == numero:
                return tmp
            tmp = tmp.siguienteNodo
        return None
    
    
    """
        Recibe la posicion a la que deseamos obtenerle el valor
    """   
    def busquedaPosicion(self,posicion:int):
        tmp = self.nodoRaiz
        for x in range(self.size):
            if x == posicion:
                return tmp
            tmp = tmp.siguienteNodo
        return None

    def eliminarNumero(self,numero:int):
        pass

    def recorrerLista(self):
        tmp = self.nodoRaiz
        for x in range(self.size):
            print(tmp.numero)
            tmp = tmp.siguienteNodo
        
    def recorridoInverso(self):
        tmp = self.nodoFinal
        for x in range(self.size):
            print(tmp.numero)
            tmp = tmp.anteriorNodo
    

lista = ListaDoble()
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
lista.insertarOrden(75)
lista.insertarOrden(13)
lista.insertarOrden(15)
lista.recorridoInverso()