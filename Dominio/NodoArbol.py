
class NodoArbol:

    def __init__(self, nodoPadre, Cubo, profundidad, costoCamino, f,costeAccion):
        self.estado = Cubo
        self.nodoPadre = None
        self.f = f
        if nodoPadre == None:
            self.costoCamino = 0
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.nodoPadre=nodoPadre
            self.costoCamino=costoCamino
            self.profundidad=profundidad
            self.accion = "     "+nodoPadre.estado.nodoActual + "->" + self.estado.nodoActual + " | " +" f:"+ str(self.f) + " p: " + str(profundidad) + " coste Camino: "  + str(costoCamino)+" |"
        

