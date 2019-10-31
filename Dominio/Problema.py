import Dominio.EspacioEstados as EspacioEstados
import Dominio.Cubo as Cubo
import math, copy

class Problema:
    def __init__(self, json):
        self.espacioEstados = EspacioEstados(json)
        self.estadoInicial = Cubo(json)
        self.estadoObjetivo = self.getCuboObjetivo(self.estadoInicial)

    def esObjetivo(self, Estado):
        if not Estado.listaPendientes:
            return True
        else:
            return False
    
    def getCuboObjetivo(self, cubo_original):
        mapa_colores = {'BACK':3,'DOWN':1,'FRONT':2,'LEFT':4,'RIGHT':5,'UP':0}
        cubo_objetivo = copy.deepcopy(cubo_original)
        longitud = cubo_objetivo.getCuboSize() - 1
        for i in range(0, longitud):
            for j in range(0, longitud):
                cubo_objetivo.back[i][j] = 3
                cubo_objetivo.down[i][j] = 1
                cubo_objetivo.front[i][j] = 2
                cubo_objetivo.left[i][j] = 4
                cubo_objetivo.right[i][j] = 5
                cubo_objetivo.up[i][j] = 0
        cubo_objetivo.update_estado()
                
            