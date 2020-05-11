# -*- coding: utf-8 -*-
from pyDatalog import pyDatalog, pyEngine
import logging
import controlador
from ui import ui

#pyEngine.Logging = True
#logging.basicConfig(level=logging.INFO)

pyDatalog.create_terms(
    'V,U,W,X,Y,Z,enfermo_de,tiene_sintoma,elimina,sintoma_de,Sintoma, Organo,Enfermedad,tratamiento_enfermedad, '
    'print_, twice, tiene_sintoma, diagnostico, enfermedad, animal')


tipos = ['', 'cuadrupedo', 'bipedo', 'volador', 'acuatico']
dieta = ['', 'carnivoro', 'hervivoro', 'omnivoro']
vive = ['', 'america', 'granja', 'selva', 'artantida', 'domestico']
granja = ['', 'consumo humano', 'extraerle recursos']
domestico = ['', 'mejor amigo del hombre', 'Independiente y apatico', 'nada', 'habla y/o canta']


def menu_juego(control):
    estado = True
    caracteristicas = []
    while estado:
        #ui.pantalla_primera_juego()
        #if opcion == '0':
            #return True
            #break
        opcion = ui.pantalla_juego()
        if opcion == '6':
            return True
            break
        caracteristicas.append(tipos[int(opcion)])
        opcion = ui.pantalla_segunda_juego()
        if opcion == '0':
            return True
            break
        caracteristicas.append(dieta[int(opcion)])
        opcion = ui.pantalla_tercera_juego()
        if opcion == '0':
            return True
            break
        caracteristicas.append(vive[int(opcion)])
        if opcion == '2':
            opcion = ui.pantalla_granja_juego()
            if opcion == '0':
                return True
                break
            caracteristicas.append(granja[int(opcion)])
            res = control.consultar_animal_granja(caracteristicas[0], caracteristicas[1], caracteristicas[2], caracteristicas[3])
            print('El sistema ha validado sus respuestas y el animal es: {}'.format(res))
            estado = False
            return estado
        if opcion == '5':
            opcion = ui.pantalla_domestico_juego()
            if opcion == '0':
                return True
                break
            caracteristicas.append(domestico[int(opcion)])
            res = control.consultar_animal_domestico(caracteristicas[0], caracteristicas[1], caracteristicas[2], caracteristicas[3])
            print('El sistema ha validado sus respuestas y el animal es: {}'.format(res))
            estado = False
            return estado
        else:
            res = control.consultar_animal_por_tipo(caracteristicas[0], caracteristicas[1], caracteristicas[2])
            print('El sistema ha validado sus respuestas y el animal es: {}'.format(res))
            estado = False
            return estado
            menu_juego()
            if opcion == '0':
                return True
                break
        if opcion == '0':
            return True
            break


def menu_informacion():
    estado = True
    while estado:
        opcion = ui.pantalla_informacion()
        print(opcion)
        if opcion == '0':
            break
        else:
            print('¡LEÉ OME! Que Presionés 0 para regresar al menú principal')


def menu_entretencion():
    estado = True
    while estado:
        opcion = ui.pantalla_entretencion()
        if opcion == '0':
            break
        else:
            print('¡LEÉ OME! Que Presionés 0 para regresar al menú principal')


def main():
    control = controlador.Controlador()
    estado = True
    while estado:
        opcion = ui.menu_principal()
        if opcion == '4':
            ui.mensaje_salida()
            break
        elif opcion == '1':
            estado = menu_juego(control)
        elif opcion == '2':
            menu_informacion()
        elif opcion == '3':
            menu_entretencion()
        else:
            print('La opción seleccionada no es válida, lea bien y vuelva a intentar,vamos tu puedes.')


if __name__ == '__main__':
    main()
