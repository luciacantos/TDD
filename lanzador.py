from src.calculator import Calculator

def lanzador():
    calculadora = Calculator()

    while True:
        print("\n================================")
        print("Calculadora")
        print("================================")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz cuadrada")
        print("6. Potencia")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Factorial")
        print("0. Salir")
        print("================================")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 0:
            print("Saliendo....")
            break

        a = float(input("Ingrese el primer número: "))
        if opcion in [1,2,3,4,6]:
            b = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print(f"Resultado: {calculadora.suma(a, b)}")
        elif opcion == 2:
            print(f"Resultado: {calculadora.resta(a, b)}")
        elif opcion == 3:
            print(f"Resultado: {calculadora.multiplicacion(a, b)}")
        elif opcion == 4:
            try:
                print(f"Resultado: {calculadora.division(a, b)}")
            except ZeroDivisionError as e:
                print(e)
        elif opcion == 5:
            print(f"Resultado: {calculadora.raiz(a)}")
        elif opcion == 6:
            print(f"Resultado: {calculadora.potencia(a, b)}")
        elif opcion == 7:
            print(f"Resultado: {calculadora.seno(a)}")
        elif opcion == 8:
            print(f"Resultado: {calculadora.coseno(a)}")
        elif opcion == 9:
            print(f"Resultado: {calculadora.tangente(a)}")
        elif opcion == 10:
            print(f"Resultado: {calculadora.factorial(int(a))}")
        else:
            print("Opción no válida, intente de nuevo.")
