import random
class cuentabancaria:
    def __init__(self,titular,saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
        self._numero_de_cuenta_interno = random.randint(1,100)
        print("Cuenta creada")
    def depositar(self,cantidad):
        if cantidad >= 0:
          self.__saldo += cantidad
          print(f"deposito de: ${cantidad}, Nuevo saldo : ${self.__saldo}")
        else:
          print("la cantidad debe ser positiva")
    def retirar(self,cantidad):
        if cantidad >0 and cantidad <= self.__saldo:
          self.__saldo -= cantidad
          print(f"Retiro de: ${cantidad}, Nuevo saldo : ${self.__saldo}")
        elif cantidad <= 0:
          print("la cantidad debe ser positiva")
        else:
          print("saldo insuficiente")
    def obtener_saldo(self):
        return self.__saldo
    def obtener_numero_cuenta(self):
        return self._numero_de_cuenta_interno
def main():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = cuentabancaria(titular)
    while True:
        print("\nOpciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Obtener Saldo")
        print("4. Obtener Número de Cuenta")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
            except ValueError:
                print("La cantidad debe ser un número válido.")
                continue
            cuenta.depositar(cantidad)
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
            except ValueError:
                print("La cantidad debe ser un número válido.")
                continue
            cuenta.retirar(cantidad)
        elif opcion == "3":
            print(f"Saldo actual: ${cuenta.obtener_saldo()}")
        elif opcion == "4":
            print(f"Número de cuenta: {cuenta.obtener_numero_cuenta()}")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
if __name__ == "__main__":
    main()