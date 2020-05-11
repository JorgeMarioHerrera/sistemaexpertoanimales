# -*- coding: utf-8 -*- 
import os
import turtle
from turtle import *

def limpiar_pantalla():
  os.system('clear')

def mensaje_salida():
    limpiar_pantalla()
    print(""" 
            ----------------------------------------------------------------------------
                                   Ha salido de la aplicación
            ----------------------------------------------------------------------------

    """)

def menu_principal():
    limpiar_pantalla()
    print("""
            **************** SISTEMA EXPERTO PARA EL RECONOCIMIENTO DE ********
            *********************** ANIMALES DE VARIAS ESPECIES ***************

            ¿Qué desea hacer?
            1. Jugar
            2. Información
            3. Entretención gráfica
            4. Salir del programa
    """)
    opcion = raw_input('            Digíte su opción: ')
    return opcion


def pantalla_primera_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione los rasgos del animal...
            ----------------------------------------------------------------------------           
            1. Vertebrados
            2. Invertebrados
            0. Para regresar al menú principal.


    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion

def pantalla_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione los rasgos del animal...
            ----------------------------------------------------------------------------           
            1. Cuadrupedo
            2. Bipedo
            3. Volador
            4. Acuatico
            5. Insecto
            0. Para regresar al menú principal.

            
    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion


def pantalla_segunda_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione que come el animal...
            ----------------------------------------------------------------------------           
            1. Carnivoros
            2. Hervivoros
            3. Omnivoros
            0. Para regresar al menú principal.


    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion

def pantalla_tercera_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione donde vive el animal...
            ----------------------------------------------------------------------------           
            1. America
            2. Granja
            3. Selva
            4. Antartida
            5. Doméstico
            0. Para regresar al menú principal.


    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion

def pantalla_granja_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione datos generales del animal de granja...
            ----------------------------------------------------------------------------           
            1. Consumo Humano
            2. Extraerle recursos
            0. Para regresar al menú principal.
    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion

def pantalla_domestico_juego():
    limpiar_pantalla()
    print(""" 
            Seleccione datos generales del animal dometico...
            ----------------------------------------------------------------------------           
            1. Mejor amigo del hombre
            2. Independiente y apático
            3. Nada
            4. Habla o canta
            0. Para regresar al menú principal.
    """)
    opcion = raw_input('            Digíte su opción: ')
    limpiar_pantalla()
    return opcion

def pantalla_informacion():
    limpiar_pantalla()
    print(""" 
            Acerca de la aplicación...
            ----------------------------------------------------------------------------
            Desarrollada por:
            
                Jorge Mario Herrera Vargas
                Jhon Freddy Salamanca Cobos
                Diego Armando Hoyos Zarasa
                
            Desarrollada en:
            
                Pyhton 3.7
                PyCharm IDE
                Debian 10 Buster
                
            Presione 0 para regresar al menú principal.
    """)
    opcion = raw_input('            Digíte su opción: ')
    return opcion

def pantalla_entretencion():
    limpiar_pantalla()
    print(""" 
                Entretencion gráfica...
                ----------------------------------------------------------------------------        
        """)
    turtle.shape("turtle")
    color('red', 'yellow')
    begin_fill()
    turtle.speed(10)
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
            turtle.bye()
    end_fill()
    done()
    print("""
            Presione 0 para regresar al menú principal.
    """)
    opcion = raw_input('            Digíte su opción: ')
    return opcion