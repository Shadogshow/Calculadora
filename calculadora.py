"""Menú e interacción con el usuario."""

import math

import operaciones

# Operaciones agrupadas por la cantidad de datos que necesitan
DOS_NUMEROS = {
    "1": ("Suma", operaciones.suma),
    "2": ("Resta", operaciones.resta),
    "3": ("Multiplicación", operaciones.multiplicacion),
    "4": ("División", operaciones.division),
    "5": ("Potencia", operaciones.potencia),
    "6": ("Módulo", operaciones.modulo),
    "7": ("Porcentaje", operaciones.porcentaje),
}

UN_NUMERO = {
    "9": ("Raíz cuadrada", operaciones.raiz_cuadrada),
    "10": ("Valor absoluto", operaciones.valor_absoluto),
    "11": ("Factorial", operaciones.factorial),
}


def pedir_numero(mensaje):
    # Repite la pregunta hasta recibir un número válido
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
        except ValueError:
            print("Entrada no válida: escribe un número.")
            continue
        if not math.isfinite(numero):
            print("Entrada no válida: escribe un número finito.")
            continue
        return numero


def pedir_lista_numeros(mensaje):
    # Repite la pregunta hasta que todos los valores sean números
    while True:
        partes = input(mensaje).split()
        try:
            numeros = [float(x) for x in partes]
        except ValueError:
            print("Entrada no válida: escribe solo números separados por espacios.")
            continue
        if not all(math.isfinite(x) for x in numeros):
            print("Entrada no válida: escribe números finitos.")
            continue
        return numeros


def mostrar_menu():
    print()
    print("========== CALCULADORA ==========")
    print("--- Operaciones básicas ---")
    print("  1. Suma")
    print("  2. Resta")
    print("  3. Multiplicación")
    print("  4. División")
    print("--- Operaciones avanzadas ---")
    print("  5. Potencia")
    print("  6. Módulo (residuo)")
    print("  7. Porcentaje (X % de Y)")
    print("  8. Redondeo a n decimales")
    print("--- Operaciones con un número ---")
    print("  9. Raíz cuadrada")
    print(" 10. Valor absoluto")
    print(" 11. Factorial")
    print("--- Operaciones con varios números ---")
    print(" 12. Promedio")
    print("=================================")


def ejecutar_operacion(opcion):
    # Pide los datos según la operación y devuelve el resultado
    if opcion in DOS_NUMEROS:
        nombre, funcion = DOS_NUMEROS[opcion]
        if opcion == "7":
            a = pedir_numero("Porcentaje (X): ")
            b = pedir_numero("Cantidad (Y): ")
        else:
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")
        return funcion(a, b)
    if opcion in UN_NUMERO:
        nombre, funcion = UN_NUMERO[opcion]
        n = pedir_numero("Número: ")
        return funcion(n)
    if opcion == "8":
        n = pedir_numero("Número: ")
        decimales = pedir_numero("Cantidad de decimales: ")
        return operaciones.redondeo(n, decimales)
    if opcion == "12":
        numeros = pedir_lista_numeros("Números separados por espacios: ")
        return operaciones.promedio(numeros)


def main():
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    if opcion not in DOS_NUMEROS and opcion not in UN_NUMERO and opcion not in ("8", "12"):
        print("Opción no válida")
        return

    try:
        resultado = ejecutar_operacion(opcion)
    except ValueError as error:
        print("Error:", error)
        return
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
