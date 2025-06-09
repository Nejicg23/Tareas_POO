from abc import ABC, abstractmethod
from datetime import datetime


# ABSTRACCIÓN: Clase abstracta que define la interfaz común
class Empleado(ABC):
    """
    Clase abstracta que representa a un empleado genérico.
    Demuestra ABSTRACCIÓN al definir métodos que deben ser implementados.
    """

    def __init__(self, nombre, apellido, id_empleado, salario_base):
        # ENCAPSULACIÓN: Atributos privados (con underscore)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id_empleado = id_empleado
        self._salario_base = salario_base  # Protegido para subclases
        self._fecha_contrato = datetime.now()

    # ENCAPSULACIÓN: Métodos getter y setter para controlar el acceso
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def id_empleado(self):
        return self.__id_empleado

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario):
        if nuevo_salario > 0:
            self._salario_base = nuevo_salario
        else:
            raise ValueError("El salario debe ser positivo")

    # Método concreto común
    def info_basica(self):
        return f"ID: {self.__id_empleado}, Nombre: {self.__nombre} {self.__apellido}"

    # ABSTRACCIÓN: Métodos abstractos que deben ser implementados por subclases
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def tipo_empleado(self):
        pass


# HERENCIA: Clase que hereda de Empleado
class EmpleadoTiempoCompleto(Empleado):
    """
    Empleado de tiempo completo con beneficios y bonos.
    Demuestra HERENCIA al extender la clase Empleado.
    """

    def __init__(self, nombre, apellido, id_empleado, salario_base, bono_anual=0):
        super().__init__(nombre, apellido, id_empleado, salario_base)
        self._bono_anual = bono_anual
        self._beneficios = ["Seguro médico", "Vacaciones pagadas", "Fondo de pensiones"]

    # POLIMORFISMO: Implementación específica del método abstracto
    def calcular_salario(self):
        return self._salario_base + (self._bono_anual / 12)

    def mostrar_info(self):
        salario_mensual = self.calcular_salario()
        beneficios_str = ", ".join(self._beneficios)
        return (f"{self.info_basica()}\n"
                f"Tipo: {self.tipo_empleado()}\n"
                f"Salario mensual: ${salario_mensual:,.2f}\n"
                f"Bono anual: ${self._bono_anual:,.2f}\n"
                f"Beneficios: {beneficios_str}")

    def tipo_empleado(self):
        return "Tiempo Completo"


# HERENCIA: Otra clase que hereda de Empleado
class EmpleadoMedioTiempo(Empleado):
    """
    Empleado de medio tiempo con horas trabajadas.
    Demuestra HERENCIA y POLIMORFISMO.
    """

    def __init__(self, nombre, apellido, id_empleado, tarifa_hora, horas_semanales=20):
        salario_base = tarifa_hora * horas_semanales * 4  # Aproximado mensual
        super().__init__(nombre, apellido, id_empleado, salario_base)
        self._tarifa_hora = tarifa_hora
        self._horas_semanales = horas_semanales

    # POLIMORFISMO: Implementación diferente del mismo método
    def calcular_salario(self):
        return self._tarifa_hora * self._horas_semanales * 4

    def mostrar_info(self):
        salario_mensual = self.calcular_salario()
        return (f"{self.info_basica()}\n"
                f"Tipo: {self.tipo_empleado()}\n"
                f"Tarifa por hora: ${self._tarifa_hora:.2f}\n"
                f"Horas semanales: {self._horas_semanales}\n"
                f"Salario mensual: ${salario_mensual:,.2f}")

    def tipo_empleado(self):
        return "Medio Tiempo"


# HERENCIA: Subclase especializada de EmpleadoTiempoCompleto
class Gerente(EmpleadoTiempoCompleto):
    """
    Gerente con responsabilidades adicionales.
    Demuestra HERENCIA multinivel y POLIMORFISMO.
    """

    def __init__(self, nombre, apellido, id_empleado, salario_base, bono_anual, equipo_a_cargo=None):
        super().__init__(nombre, apellido, id_empleado, salario_base, bono_anual)
        self._equipo_a_cargo = equipo_a_cargo or []
        self._beneficios.extend(["Carro de empresa", "Gastos de representación"])

    def agregar_empleado_a_cargo(self, empleado):
        self._equipo_a_cargo.append(empleado)

    # POLIMORFISMO: Sobrescribir método para comportamiento específico
    def calcular_salario(self):
        salario_base = super().calcular_salario()
        bono_gestion = len(self._equipo_a_cargo) * 500  # Bono por empleado a cargo
        return salario_base + bono_gestion

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return (f"{info_base}\n"
                f"Empleados a cargo: {len(self._equipo_a_cargo)}\n"
                f"Bono de gestión: ${len(self._equipo_a_cargo) * 500:,.2f}")

    def tipo_empleado(self):
        return "Gerente"


# ENCAPSULACIÓN: Clase para gestionar la empresa
class Empresa:
    """
    Clase que gestiona todos los empleados de la empresa.
    Demuestra ENCAPSULACIÓN al mantener la lista de empleados privada.
    """

    def __init__(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__empleados = []  # Lista privada de empleados

    def contratar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.__empleados.append(empleado)
            print(f"✓ Empleado {empleado.nombre} {empleado.apellido} contratado exitosamente")
        else:
            raise TypeError("Solo se pueden contratar objetos de tipo Empleado")

    def despedir_empleado(self, id_empleado):
        for i, empleado in enumerate(self.__empleados):
            if empleado.id_empleado == id_empleado:
                empleado_despedido = self.__empleados.pop(i)
                print(f"✓ Empleado {empleado_despedido.nombre} {empleado_despedido.apellido} despedido")
                return empleado_despedido
        print(f"✗ No se encontró empleado con ID: {id_empleado}")
        return None

    def buscar_empleado(self, id_empleado):
        for empleado in self.__empleados:
            if empleado.id_empleado == id_empleado:
                return empleado
        return None

    # POLIMORFISMO: Funciona con cualquier tipo de empleado
    def mostrar_nomina(self):
        if not self.__empleados:
            print("No hay empleados registrados")
            return

        print(f"\n{'=' * 60}")
        print(f"NÓMINA DE {self.__nombre_empresa.upper()}")
        print(f"{'=' * 60}")

        total_nomina = 0
        for empleado in self.__empleados:
            print(f"\n{empleado.mostrar_info()}")
            total_nomina += empleado.calcular_salario()
            print("-" * 60)

        print(f"\nTOTAL NÓMINA MENSUAL: ${total_nomina:,.2f}")
        print(f"NÚMERO DE EMPLEADOS: {len(self.__empleados)}")

    def calcular_costo_total_nomina(self):
        return sum(empleado.calcular_salario() for empleado in self.__empleados)

    @property
    def total_empleados(self):
        return len(self.__empleados)


# FUNCIÓN PRINCIPAL PARA DEMOSTRAR EL PROGRAMA
def main():
    """
    Función principal que demuestra todos los conceptos de POO
    """
    print("🏢 SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("Demostrando los 4 pilares de la POO\n")

    # Crear empresa
    mi_empresa = Empresa("TechCorp Solutions")

    # Crear diferentes tipos de empleados
    empleado1 = EmpleadoTiempoCompleto("Ana", "García", "E001", 3000, 6000)
    empleado2 = EmpleadoMedioTiempo("Carlos", "López", "E002", 15, 25)
    empleado3 = Gerente("María", "Rodríguez", "G001", 5000, 12000)
    empleado4 = EmpleadoTiempoCompleto("José", "Martínez", "E003", 2800, 4000)

    # Contratar empleados
    print("📋 CONTRATANDO EMPLEADOS:")
    mi_empresa.contratar_empleado(empleado1)
    mi_empresa.contratar_empleado(empleado2)
    mi_empresa.contratar_empleado(empleado3)
    mi_empresa.contratar_empleado(empleado4)

    # El gerente tiene empleados a cargo
    empleado3.agregar_empleado_a_cargo(empleado1)
    empleado3.agregar_empleado_a_cargo(empleado4)

    # Mostrar nómina completa
    mi_empresa.mostrar_nomina()

    # Demostrar POLIMORFISMO: mismo método, diferentes comportamientos
    print(f"\n🔄 DEMOSTRANDO POLIMORFISMO:")
    print("Método calcular_salario() funciona diferente para cada tipo:")
    for empleado in [empleado1, empleado2, empleado3]:
        print(f"- {empleado.tipo_empleado()}: ${empleado.calcular_salario():,.2f}")

    # Demostrar ENCAPSULACIÓN: intentar acceder a datos privados
    print(f"\n🔒 DEMOSTRANDO ENCAPSULACIÓN:")
    print(f"Acceso controlado al nombre: {empleado1.nombre}")
    try:
        # Esto causaría error si intentáramos acceso directo: empleado1.__nombre
        empleado1.salario_base = 3500  # Usando setter
        print(f"Nuevo salario establecido: ${empleado1.salario_base}")
    except ValueError as e:
        print(f"Error controlado: {e}")

    print(f"\n📊 RESUMEN FINAL:")
    print(f"Total empleados: {mi_empresa.total_empleados}")
    print(f"Costo total nómina: ${mi_empresa.calcular_costo_total_nomina():,.2f}")


if __name__ == "__main__":
    main()