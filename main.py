def sumar(a, b):
    # aqui se realiza la suma de dos numeros

def restar(a, b):
    # aqui se realiza la resta de dos numeros

def multiplicar(a, b):
    # aqui se realiza la multiplicacion de dos numeros

def dividir(a, b):
    # aqui se realiza la division de dos numeros

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    print("División:", dividir(num1, num2))

if __name__ == "__main__":
    main()
