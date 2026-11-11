"""Menú e interacción con el usuario."""

import operaciones


def mostrar_menu():
    print("===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Porcentaje (primer número % del segundo)")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio de varios números")
    print("12. Redondeo a n decimales")


def main():
    mostrar_menu()
    opcion = input("Elige una opción: ")

    # Operaciones que solo necesitan un número
    if opcion in ("7", "9", "10"):
        n = float(input("Número: "))
        try:
            if opcion == "7":
                resultado = operaciones.raiz_cuadrada(n)
            elif opcion == "9":
                resultado = operaciones.valor_absoluto(n)
            else:
                resultado = operaciones.factorial(n)
        except ValueError as error:
            print("Error:", error)
            return
        print("Resultado:", resultado)
        return

    # Promedio: recibe varios números en una sola línea
    if opcion == "11":
        entrada = input("Números separados por espacios: ")
        numeros = [float(x) for x in entrada.split()]
        try:
            resultado = operaciones.promedio(numeros)
        except ValueError as error:
            print("Error:", error)
            return
        print("Resultado:", resultado)
        return

    # Redondeo: pide el número y la cantidad de decimales
    if opcion == "12":
        n = float(input("Número: "))
        decimales = float(input("Cantidad de decimales: "))
        try:
            resultado = operaciones.redondeo(n, decimales)
        except ValueError as error:
            print("Error:", error)
            return
        print("Resultado:", resultado)
        return

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        resultado = operaciones.suma(a, b)
    elif opcion == "2":
        resultado = operaciones.resta(a, b)
    elif opcion == "3":
        resultado = operaciones.multiplicacion(a, b)
    elif opcion == "4":
        resultado = operaciones.division(a, b)
    elif opcion == "5":
        resultado = operaciones.potencia(a, b)
    elif opcion == "6":
        resultado = operaciones.modulo(a, b)
    elif opcion == "8":
        resultado = operaciones.porcentaje(a, b)
    else:
        print("Opción no válida")
        return

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
