def sumar(a, b):    ##kevin steve florez benavides
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero no permitida."

def menu():
    print("===== Calculadora Básica =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '5':
            print("¡Gracias por usar la calculadora!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == '1':
                    print("Resultado:", sumar(num1, num2))
                elif opcion == '2':
                    print("Resultado:", restar(num1, num2))
                elif opcion == '3':
                    print("Resultado:", multiplicar(num1, num2))
                elif opcion == '4':
                    print("Resultado:", dividir(num1, num2))
            except ValueError:
                print("Error: Ingresa solo números válidos.")
        else:
            print("Opción no válida. Intenta de nuevo.")
        print()  

if __name__ == "__main__":
    main()
