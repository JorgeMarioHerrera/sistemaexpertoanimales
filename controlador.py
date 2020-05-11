from base_conocimiento import base_conocimiento

class Controlador:

  def __init__(self):
      pass

  def consultar_animal_por_tipo(self, X, Y, V):
    return base_conocimiento.consultar_animal_por_tipo(X, Y, V)

  def consultar_animal_granja(self, X, Y, V, W):
    return base_conocimiento.consultar_animal_granja(X, Y, V, W)

  def consultar_animal_domestico(self, X, Y, V, W):
    return base_conocimiento.consultar_animal_domestico(X, Y, V, W)