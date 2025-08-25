
class Producto:
    #incio de la clase segun el enunciado de la tarea
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    # getters y setters para los metodos de la clase
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    # metodo str para imprimir los productos
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
class Inventario:
    #inicio de la clase inventario
    def __init__(self):
        self.productos = []
    #metodo para agragar productos
    def agregar_producto(self, producto):
        if not self.buscar_por_id(producto.get_id()):
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")
            return True
        else:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
            return False
    #metodo para eliminar productos
    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
            return True
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")
            return False
    #metodo para actualizar productos
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
            return True
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")
            return False
    #metodo para buscar productos por id
    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None
    #metodo para buscar productos por nombre
    def buscar_por_nombre(self, nombre_buscado):
        resultados = []
        nombre_buscado_lower = nombre_buscado.lower()
        for producto in self.productos:
            if nombre_buscado_lower in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados
    #metodo para mostrar el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for producto in self.productos:
                print(producto)
            print("-------------------------")
# funcion para mostrar el menu
def menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    inventario = Inventario()

    # Datos de prueba para rellenar el inventario inicialmente
    inventario.agregar_producto(Producto(101, "Laptop", 10, 1200.50))
    inventario.agregar_producto(Producto(102, "Mouse USB", 50, 15.00))
    inventario.agregar_producto(Producto(103, "Teclado", 25, 45.99))
    inventario.agregar_producto(Producto(104, "Monitor", 5, 250.75))

    while True:
        opcion = menu()

        if opcion == '1':
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para ID, cantidad y precio.")

        elif opcion == '2':
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_prod)
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número para el ID.")

        elif opcion == '3':
            try:
                id_prod = int(input("Ingrese el ID del producto a actualizar: "))
                opcion_act = input("¿Desea actualizar la cantidad (C), el precio (P) o ambos (A)? ").upper()
                if opcion_act == 'C':
                    nueva_cant = int(input("Ingrese la nueva cantidad: "))
                    inventario.actualizar_producto(id_prod, nueva_cantidad=nueva_cant)
                elif opcion_act == 'P':
                    nuevo_prec = float(input("Ingrese el nuevo precio: "))
                    inventario.actualizar_producto(id_prod, nuevo_precio=nuevo_prec)
                elif opcion_act == 'A':
                    nueva_cant = int(input("Ingrese la nueva cantidad: "))
                    nuevo_prec = float(input("Ingrese el nuevo precio: "))
                    inventario.actualizar_producto(id_prod, nueva_cantidad=nueva_cant, nuevo_precio=nuevo_prec)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números.")

        elif opcion == '4':
            nombre_buscado = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre_buscado)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for producto in resultados:
                    print(producto)
                print("----------------------------------")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()