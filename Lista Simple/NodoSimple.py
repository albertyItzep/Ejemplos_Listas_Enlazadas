class Nodo_Simple:
    def __init__(self,numero:int) -> None:
        self.numero:int = numero
        self.nextNodo = None
    
    def esMenor(self,numero:int):
        if self.numero < numero:
            return True
        return False