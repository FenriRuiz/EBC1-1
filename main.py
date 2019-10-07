#!/usr/bin/python3
# -*- coding: utf-8 -*-

import utils, copy, cmd
import FormarCubo.construirImagen as GenerarImagen
import GUI.VIEW_rubiks as Gui
from Cubo import Cubo as Objeto_Cubo

GENERAR_IMAGENES = False

def main():
    json_file = utils.jsonRead('cuboSolucionado.json')
    
    orig_cubo = Objeto_Cubo(json_file)
    orig_cubo.updateEstado()
    print(str(orig_cubo))
    
    new_cubo = copy.deepcopy(orig_cubo) 
    
    new_cubo.desplazamientob(2) #Está todo bien
    new_cubo.updateEstado()
    print(str(new_cubo))

    
class CubeShell(cmd.Cmd):
    intro = 'Shell del cubo de Rubik. ? o Help para ayuda\n'
    prompt = '(Cubo)> '

    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual'''
        
    
    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual'''
    
    def do_probar_giros(self,arg):
        pass
    
    def do_generar_imagenes(self, arg):
        '''Generar imagenes de cada accion hecha con el cubo 
        Syntax: (Cubo)> generar_imagenes <true/false>
        '''
        print('Valor actual: ' + str(GENERAR_IMAGENES) + '\n')
        try:
            opt = eval(arg)
            if isinstance(opt, bool):
                GENERAR_IMAGENES = opt
        except NameError:
            print('Error en los argumentos.')
        pass
        
        
    def do_iniciar_gui(self, arg):
        '''Iniciar entorno grafico (En construccion)'''
        Gui.start()    


def moverCubo(cubo, movimiento, fila):
    movimientos = {
        'B' : cubo.desplazamientoB(fila),
        'b' : cubo.desplazamientob(fila),
        'L' : cubo.desplazamientoL(fila),
        'l' : cubo.desplazamientol(fila),
        'D' : cubo.desplazamientoD(fila),
        'd' : cubo.desplazamientod(fila)
    }
    movimientos.get(movimiento)
    cubo.updateEstado()
    

def initResources():
    utils.createFolder(utils.PATHS.get('image_folder'))
    utils.createFolder(utils.PATHS.get('json_folder'))
    
    
if __name__ == "__main__":
    print('''
--------------------------------          
    Rubik Resolver v.0.0.1.
--------------------------------    
    ''')
    initResources()
    main()
    