class CuentaBancaria:
    def __init__(self, titular, interes):
        self.titular = titular
        self.interes = interes
        self.saldo = 0          
    
    def depositar(self, monto):
        self.saldo += monto
        
    def retirar(self, monto):
        self.saldo -= monto
        
    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes
        
    def __str__(self):
        return f"Hola {self.titular}, tu saldo actual es ${self.saldo:.2f}"
        
cuenta = CuentaBancaria("Martina Ibanez", 0.07)
print(cuenta)

cuenta.depositar(1000)
print(cuenta)

cuenta.retirar(200)
print(cuenta)

cuenta.aplicar_interes()
print(cuenta)
