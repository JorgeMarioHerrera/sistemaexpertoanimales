# -*- coding: utf-8 -*- 
from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import assert_fact, load, ask

# Variables
pyDatalog.create_terms('X,Y,V,U, W, Su_Animal_Es, _')

# Predicados y reglas
pyDatalog.create_terms('tipo, come, vive_en, respuesta, granja, domestico, respuestaGranja, respuestaDomestico')

+tipo('cuadrupedo','caballo')
+tipo('cuadrupedo','cerdo')
+tipo('cuadrupedo','toro')
+tipo('cuadrupedo','vaca')
+tipo('cuadrupedo','oveja')
+tipo('cuadrupedo','perro')
+tipo('cuadrupedo','gato')
+tipo('cuadrupedo','oso_polar')
+tipo('bipedo','chimpance')
+tipo('bipedo','pato')
+tipo('bipedo','pinguino')
+tipo('bipedo','loro')
+tipo('bipedo','suricata')
+tipo('bipedo','gallina')
+tipo('volador','aguila')
+tipo('acuatico','pez')
+come('carnivoro', 'aguila')
+come('hervivoro', 'caballo')
+come('hervivoro','chimpance')
+come('hervivoro','pez')
+come('hervivoro','oveja')
+come('hervivoro','vaca')
+come('carnivoro','pinguino')
+come('carnivoro','oso_polar')
+come('omnivoro','cerdo')
+come('omnivoro','perro')
+come('omnivoro','gato')
+come('hervivoro','loro')

+vive_en('america', 'aguila')
+vive_en('granja', 'caballo')
+vive_en('selva', 'chimpance')
+vive_en('granja', 'vaca')
+vive_en('artantida', 'pinguino')
+vive_en('artantida', 'oso_polar')
+vive_en('granja', 'cerdo')
+vive_en('granja', 'oveja')
+vive_en('domestico', 'perro')
+vive_en('domestico', 'gato')
+vive_en('domestico', 'pez')
+vive_en('domestico', 'loro')

+granja('consumo humano', 'vaca')
+granja('consumo humano', 'cerdo')
+granja('consumo humano', 'pollo')
+granja('consumo humano', 'pez')
+granja('extraerle recursos', 'oveja')

+domestico('mejor amigo del hombre', 'perro')
+domestico('Independiente y apatico', 'gato')
+domestico('nada', 'pez')
+domestico('habla y/o canta', 'loro')

respuesta(X, Y, V, _) <= tipo(X, _) & come(Y, _) & vive_en(V, _)
respuestaGranja(X, Y, V, W, _) <= tipo(X, _) & come(Y, _) & vive_en(V, _) & granja(W, _)
respuestaDomestico(X, Y, V, W, _) <= tipo(X, _) & come(Y, _) & vive_en(V, _) & domestico(W, _)

def consultar_animal_por_tipo(X, Y, V):
  return respuesta(X, Y, V, _)

def consultar_animal_granja(X, Y, V, W):
  return respuestaGranja(X, Y, V, W, _)

def consultar_animal_domestico(X, Y, V, W):
  return respuestaDomestico(X, Y, V, W, _)