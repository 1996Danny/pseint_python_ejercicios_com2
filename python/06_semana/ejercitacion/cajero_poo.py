
# HU-1

class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo

    # getters
    def get_numero_cuenta(self):
        return self.__numero_cuenta
    
    def get_saldo(self):
        return self.__saldo

    def validar_pin(self, pin_ingreso):
        return self.__pin == pin_ingreso
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto #(self.__saldo = self.__saldo + monto)
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False
    
# cuenta1 = Cuenta("1", "1234", 2000)
# print(f"Su numero de cuenta es: {cuenta1.get_numero_cuenta()}")
# print(f"Su saldo es: $ {cuenta1.get_saldo()}")


class Cajero:
    def __init__(self):
        self.cuentas = {}
        self.cuenta_actual = None
        self.cargar_cuentas()

    def cargar_cuentas(self):
        cuenta1 = Cuenta("1", "1234", 2000)
        cuenta2 = Cuenta("2", "4321", 100)
        self.cuentas[cuenta1.get_numero_cuenta()] = cuenta1
        self.cuentas[cuenta2.get_numero_cuenta()] = cuenta2
    
    def autenticar(self, numero_cuenta, pin):
        if numero_cuenta in self.cuentas:
            cuenta = self.cuentas[numero_cuenta]
            if cuenta.validar_pin(pin):
                self.cuenta_actual = cuenta
                return True
        self.cuenta_actual = None
        return False
    
    def cerrar_sesion(self):
        print("sesion cerrada")
        self.cuenta_actual = None

    def consultar_saldo(self):
        print(f"saldo actual: $ {self.cuenta_actual.get_saldo()}")

    def menu_transacciones(self):
        print(f"--- Menu de la cuenta {self.cuenta_actual.get_numero_cuenta()}")
        print()
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Extraer")
        print("4. Cerrar Sesión")
        print()

    def proceso_transaccion(self, opcion):
        if not self.cuenta_actual:
            print("No ha iniciado sesión")

        if opcion == "1":
            self.consultar_saldo()
        
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))

            if self.cuenta_actual.depositar(monto):
                print("Deposito correcto")
            else:
                print("deposito incorrecto")

        elif opcion == "3":
            monto = float(input("Ingrese el monto a extraer: "))

            if self.cuenta_actual.retirar(monto):
                print("Retiro correcto")
            else:
                print("Retiro incorrecto")

        elif opcion == "4":
            self.cerrar_sesion()



def iniciar_sistema():
    cajero = Cajero()
    print("BIenvenido al sistema")

    while True:
        print("Iniciar sesion")

        num_cuenta = input("Ingrese su numero de cuenta: ")
        pin = input("Ingrese su pin")

        if cajero.autenticar(num_cuenta, pin):
            print("Inicio correcto")

            while cajero.cuenta_actual:
                cajero.menu_transacciones()
                opcion = input("ingrese su opcion: ")

                if cajero.proceso_transaccion(opcion):
                    break
        else:
            print("autencicacion incorrecta")


iniciar_sistema()