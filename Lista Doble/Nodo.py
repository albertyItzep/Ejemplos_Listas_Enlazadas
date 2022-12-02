class Nodo:
    def __init__(self,numero:int):
        self.numero = numero
        self.siguienteNodo = None
        self.anteriorNodo = None
    
    def esMenor(self, numero:int):
        if self.numero < numero:
            return True
        return False