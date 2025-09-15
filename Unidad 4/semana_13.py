# Importamos la librería Tkinter para crear la interfaz gráfica.
import tkinter as tk
from tkinter import ttk


# --- Definición de Funciones para los Eventos ---

def agregar_item():
    # Obtenemos el texto del campo de entrada (entry_widget).
    dato = campo_texto.get()

    # Verificamos que el campo no esté vacío.
    if dato:
        # Insertamos el nuevo dato al final de la lista (lista_datos).
        lista_datos.insert(tk.END, dato)
        # Borramos el contenido del campo de texto para facilitar la siguiente entrada.
        campo_texto.delete(0, tk.END)


def limpiar_lista():
    # Borramos todos los items desde el primero (índice 0) hasta el último (tk.END).
    lista_datos.delete(0, tk.END)


# --- Configuración de la Ventana Principal ---

# Creamos la ventana principal de la aplicación.
ventana = tk.Tk()

# Establecemos el título que aparecerá en la barra superior de la ventana.
ventana.title("Gestor de Datos Simple")

# Definimos las dimensiones iniciales de la ventana (ancho x alto).
ventana.geometry("400x500")

# Creamos un frame principal para organizar mejor los widgets.
frame_principal = ttk.Frame(ventana, padding="10")
frame_principal.pack(fill=tk.BOTH, expand=True)

# --- Creación y Posicionamiento de los Componentes (Widgets) ---

# 1. Etiqueta para el campo de texto.
etiqueta_entrada = ttk.Label(frame_principal, text="Ingrese un dato:")
etiqueta_entrada.pack(pady=5)  # pack() es el método para posicionar el widget. pady añade un espacio vertical.

# 2. Campo de texto para que el usuario ingrese información.
campo_texto = ttk.Entry(frame_principal, width=40)
campo_texto.pack(pady=5)

# 3. Frame para los botones, para que estén uno al lado del otro.
frame_botones = ttk.Frame(frame_principal)
frame_botones.pack(pady=10)

# 4. Botón "Agregar", que al ser presionado llamará a la función agregar_item.
boton_agregar = ttk.Button(frame_botones, text="Agregar", command=agregar_item)
boton_agregar.pack(side=tk.LEFT, padx=5)  # side=tk.LEFT los alinea a la izquierda. padx añade espacio horizontal.

# 5. Botón "Limpiar", que al ser presionado llamará a la función limpiar_lista.
boton_limpiar = ttk.Button(frame_botones, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(side=tk.LEFT, padx=5)

# 6. Etiqueta para la lista de datos.
etiqueta_lista = ttk.Label(frame_principal, text="Datos Almacenados:")
etiqueta_lista.pack(pady=5)

# 7. Lista para mostrar los datos agregados por el usuario.
lista_datos = tk.Listbox(frame_principal, height=15)
lista_datos.pack(pady=5, fill=tk.BOTH, expand=True)  # fill y expand hacen que la lista ocupe el espacio disponible.

# --- Inicio del Bucle Principal de la Aplicación ---

# El método mainloop() pone a la ventana en un bucle de espera de eventos (clics, etc.).
# La aplicación se quedará aquí hasta que se cierre la ventana.
ventana.mainloop()