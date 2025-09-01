import os

class Producto:
    """
    Clase que representa un producto en el inventario.
    Contiene los atributos básicos de un producto.
    """
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_string(self):
        """
        Convierte el objeto Producto a una cadena de texto para su almacenamiento.
        El formato es: ID|Nombre|Cantidad|Precio
        """
        return f"{self.producto_id}|{self.nombre}|{self.cantidad}|{self.precio}"

    @staticmethod
    def from_string(data):
        """
        Crea un objeto Producto a partir de una cadena de texto.
        """
        try:
            partes = data.strip().split('|')
            if len(partes) == 4:
                return Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))
            else:
                return None
        except (ValueError, IndexError):
            print(f" Error: Formato de línea no válido: '{data}'")
            return None

class Inventario:
    """
    Clase que gestiona el inventario de productos.
    Utiliza un diccionario para almacenar los productos.
    """
    def __init__(self):
        # El diccionario almacena los productos. La clave es el ID y el valor es el objeto Producto.
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica si el ID ya existe para evitar duplicados.
        """
        if producto.producto_id in self.productos:
            print(f" Error: El producto con ID {producto.producto_id} ya existe.")
            return False
        self.productos[producto.producto_id] = producto
        print(f" Producto '{producto.nombre}' añadido correctamente.")
        return True

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto del inventario por su ID.
        """
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f" Producto con ID {producto_id} eliminado correctamente.")
            return True
        else:
            print(f" Error: No se encontró ningún producto con ID {producto_id}.")
            return False

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto existente.
        """
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print(f" Producto con ID {producto_id} actualizado correctamente.")
            return True
        else:
            print(f" Error: No se encontró ningún producto con ID {producto_id}.")
            return False

    def buscar_producto_por_nombre(self, nombre_busqueda):
        """
        Busca y muestra productos cuyo nombre contenga la cadena de búsqueda.
        """
        encontrados = [
            producto for producto in self.productos.values()
            if nombre_busqueda.lower() in producto.nombre.lower()
        ]
        if encontrados:
            print(f"\nProductos encontrados para '{nombre_busqueda}':")
            self.mostrar_productos(encontrados)
        else:
            print(f" No se encontraron productos con el nombre '{nombre_busqueda}'.")
        return encontrados

    def mostrar_todos_los_productos(self):
        """
        Muestra una lista de todos los productos en el inventario.
        """
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            self.mostrar_productos(self.productos.values())

    def mostrar_productos(self, lista_productos):
        """
        Función auxiliar para imprimir una lista de productos.
        """
        for p in sorted(lista_productos, key=lambda x: x.producto_id):
            print(f"ID: {p.producto_id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")
            
    def guardar_inventario(self, nombre_archivo):
        """
        Guarda el inventario en un archivo de texto.
        """
        try:
            with open(nombre_archivo, 'w') as f:
                for p in self.productos.values():
                    f.write(p.to_string() + '\n')
            print(" Inventario guardado correctamente.")
        except IOError as e:
            print(f" Error al guardar el archivo: {e}")

    def cargar_inventario(self, nombre_archivo):
        """
        Carga el inventario desde un archivo de texto.
        """
        if not os.path.exists(nombre_archivo):
            print(" Archivo de inventario no encontrado. Se iniciará con un inventario vacío.")
            return

        try:
            with open(nombre_archivo, 'r') as f:
                for linea in f:
                    producto = Producto.from_string(linea)
                    if producto:
                        self.productos[producto.producto_id] = producto
            print(" Inventario cargado correctamente.")
        except IOError as e:
            print(f" Error al cargar el archivo: {e}")

def mostrar_menu():
    """
    Muestra las opciones del menú principal al usuario.
    """
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Añadir un nuevo producto")
    print("2. Eliminar un producto")
    print("3. Actualizar un producto")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todo el inventario")
    print("6. Salir")

def main():
    """
    Función principal que ejecuta el programa.
    """
    nombre_archivo = "inventario.txt"
    inventario = Inventario()
    inventario.cargar_inventario(nombre_archivo)  # Carga los datos al iniciar

    while True:
        mostrar_menu()
        opcion = input(" Seleccione una opción: ")

        if opcion == '1':
            try:
                producto_id = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print(" Error: Cantidad o precio deben ser números válidos.")

        elif opcion == '2':
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            producto_id = input("ID del producto a actualizar: ")
            print("Deje en blanco si no desea actualizar.")
            nueva_cantidad_str = input("Nueva cantidad: ")
            nuevo_precio_str = input("Nuevo precio: ")
            nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None
            inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)
            
        elif opcion == '4':
            nombre_busqueda = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre_busqueda)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            inventario.guardar_inventario(nombre_archivo)  # Guarda los datos antes de salir
            print(" ¡Gracias por usar el sistema! Saliendo...")
            break

        else:
            print(" Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()