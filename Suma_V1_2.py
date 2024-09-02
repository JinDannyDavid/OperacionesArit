class OperacionesAritmeticas():
    def IngreNumer(self):
        numero01 = float(input("INGRESE PRIMER NUMERO: "))
        numero02 = float(input("INGRESE SEGUNDO NUMERO: "))
        return numero01, numero02


    def suma(self, numero1, numero2):
        return numero1 + numero2

if __name__=='__main__':
    operacion = OperacionesAritmeticas()
    num1, num2 = operacion.IngreNumer()
    print(f"{num1}+{num2}={operacion.suma(num1, num2)}")

