import os

# Clase Producto
# Representa un producto individual con ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters para acceder a los atributos del producto
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters para modificar la cantidad y el precio del producto
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para representar el objeto Producto como una cadena de texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
# Gestiona una colección de productos, incluyendo carga, guardado y operaciones CRUD.
class Inventario:
    def __init__(self, nombre_archivo='inventario.txt'):
        self.productos = []
        self.nombre_archivo = nombre_archivo
        # Carga el inventario desde el archivo al iniciar la aplicación
        self.cargar_inventario()

    # Guarda el estado actual del inventario en el archivo de texto.
    # Cada producto se guarda en una línea separada.
    def guardar_inventario(self):
        try:
            with open(self.nombre_archivo, 'w') as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            print("Inventario guardado en el archivo exitosamente.")
        except IOError as e:
            # Captura errores de entrada/salida durante la escritura
            print(f"Error al guardar el inventario: {e}")

    # Carga los productos desde el archivo de texto al inicio del programa.
    # Maneja la creación del archivo si no existe y errores de formato.
    def cargar_inventario(self):
        # Si el archivo no existe, notifica y no intenta cargarlo.
        if not os.path.exists(self.nombre_archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            return

        try:
            with open(self.nombre_archivo, 'r') as f:
                for linea in f:
                    try:
                        # Intenta dividir la línea y crear un objeto Producto
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(int(id), nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                    except ValueError:
                        # Si una línea tiene formato incorrecto, la ignora y advierte al usuario
                        print(f"Advertencia: Línea con formato incorrecto en el archivo: {linea.strip()}")
            print("Inventario cargado desde el archivo exitosamente.")
        except FileNotFoundError:
            # Este error se maneja con 'os.path.exists', pero se incluye como precaución
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except IOError as e:
            # Captura otros errores de entrada/salida durante la lectura
            print(f"Error de lectura del archivo: {e}")

    # Añade un nuevo producto al inventario.
    # Verifica que el ID sea único antes de añadir y guarda los cambios.
    def agregar_producto(self, producto):
        if not self.buscar_por_id(producto.get_id()):
            self.productos.append(producto)
            self.guardar_inventario() # Guarda los cambios
            print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")
            return True
        else:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
            return False

    # Elimina un producto del inventario por su ID.
    # Guarda los cambios después de la eliminación.
    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario() # Guarda los cambios
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
            return True
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")
            return False

    # Actualiza la cantidad o el precio de un producto por su ID.
    # Guarda los cambios después de la actualización.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self.guardar_inventario() # Guarda los cambios
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
            return True
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")
            return False
            
    # Busca un producto por su ID.
    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # Busca productos por una coincidencia parcial en el nombre.
    def buscar_por_nombre(self, nombre_buscado):
        resultados = []
        nombre_buscado_lower = nombre_buscado.lower()
        for producto in self.productos:
            if nombre_buscado_lower in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    # Muestra todos los productos actualmente en el inventario.
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for producto in self.productos:
                print(producto)
            print("-------------------------")

# Función para mostrar el menú de opciones al usuario.
def menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")

# Función principal que ejecuta el programa.
def main():
    inventario = Inventario() # Se inicializa y carga el inventario desde el archivo.

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

# Asegura que la función main se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    main()