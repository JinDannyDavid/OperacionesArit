def IngreNumer():
    numero01 = float(input("INGRESE PRIMER NUMERO: "))
    numero02 = float(input("INGRESE SEGUNDO NUMERO: "))
    return numero01, numero02


def suma(numero1, numero2):
    return numero1 + numero2

if __name__=='__main__':
    num1, num2 = IngreNumer()
    print(f"{num1}+{num2}={suma(num1, num2)}")

