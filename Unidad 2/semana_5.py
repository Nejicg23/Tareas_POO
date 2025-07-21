"""Este programa permite registrar un miembro de un club deportivo."""
def mostrar_resumen_registro(nombre_miembro, edad, cuota, es_miembro_activo):
    #Esta función muestra un resumen del registro del miembro.
    print("\n" + "=" * 40)
    print("=" * 40)
    print(f"Nombre Completo: {nombre_miembro}")
    print(f"Edad: {edad} años")
    print(f"Cuota Mensual: ${cuota:.2f}")#controla el formato de la cuota
    print("=" * 40)
    print("\n  Bienvenido al Club")

# Mostrar estado del miembro
    estado = "Activo" if es_miembro_activo else "Inactivo"
    print(f"Nombre: {nombre_miembro}, Edad: {edad}, Cuota: {cuota}, Estado: {estado}")
def registrar_miembro():
    # Esta función permite registrar un nuevo miembro del club deportivo.
    print("-----Formulario de Registro-----")
    nombre_miembro = input("Nombre del miembro: ")
    edad = 0
    # Validación de la edad
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
    # Validación de la cuota mensual
    cuota = 0.0
    while True:
        try:
            cuota = float(input("Cuota mensual: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la cuota.")
    # Validación del estado de miembro activo
    es_miembro_activo = False
    respuesta = input("¿Es miembro activo? (S/N): ")
    if respuesta.lower().strip() == 's':
        es_miembro_activo = True
    mostrar_resumen_registro(nombre_miembro, edad, cuota, es_miembro_activo)
# Fin del registro del miembro
if __name__ == '__main__':
# Ejecutar la función de registro del miembro
    registrar_miembro()

