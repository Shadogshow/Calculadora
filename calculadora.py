"""Menú e interacción con el usuario."""

import operaciones


def mostrar_menu():
    print("===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")


def main():
    mostrar_menu()
    opcion = input("Elige una opción: ")

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
    else:
        print("Opción no válida")
        return

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
