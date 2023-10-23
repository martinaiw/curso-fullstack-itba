class CuentaBancaria:
    def __init__(self, titular):
        self._titular = titular
        self._saldo = 0
        
    def depositar(self, monto):
        self._saldo += monto
    def retirar(self, monto):
        self._saldo -= monto
    def consultar_saldo(self):
        print(f"Tu saldo es {self._saldo}")


cuenta = CuentaBancaria("Juan Pérez")
cuenta.depositar(1000)
cuenta.retirar(500)
cuenta.consultar_saldo()

print(cuenta._saldo)  # Acceso incorrecto a _saldo
print(cuenta._titular)  # Acceso incorrecto a _titular