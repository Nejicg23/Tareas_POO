#incializacion de la clase coche junto con sus atributos
class coche:
    def __init__(self,marca,modelo,color):
      self.marca = marca
      self.modelo = modelo
      self.color = color
      print("Se ha creado un coche")
#metodo para mostrar la informacion del coche
    def info(self):
      return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
#metodo para eliminar la instancia de la clase para ahorrar memoria
    def __del__(self):
      print("Se ha eliminado un coche")
# Creación de una instancia de la clase coche y uso de sus métodos
mi_coche = coche("Toyota", "Corolla", "Rojo")
print(mi_coche.info())
# Eliminación de la instancia para liberar memoria
del mi_coche