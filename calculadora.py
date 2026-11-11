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

# Guarda las operaciones realizadas durante la sesión
historial = []

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
    print("--- Historial ---")
    print(" 13. Ver historial")
    print(" 14. Limpiar historial")
    print("---------------------------------")
    print("  0. Salir")
    print("=================================")


def mostrar_historial():
    if len(historial) == 0:
        print("El historial está vacío.")
        return
    print("--- Historial de operaciones ---")
    for i, registro in enumerate(historial, start=1):
        print(f"{i}. {registro}")


def limpiar_historial():
    if len(historial) == 0:
        print("El historial ya está vacío.")
        return
    historial.clear()
    print("Historial borrado.")


def ejecutar_operacion(opcion):
    # Pide los datos, calcula y devuelve (descripción, resultado)
    if opcion in DOS_NUMEROS:
        nombre, funcion = DOS_NUMEROS[opcion]
        if opcion == "7":
            a = pedir_numero("Porcentaje (X): ")
            b = pedir_numero("Cantidad (Y): ")
        else:
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")
        return f"{nombre}({a}, {b})", funcion(a, b)
    if opcion in UN_NUMERO:
        nombre, funcion = UN_NUMERO[opcion]
        n = pedir_numero("Número: ")
        return f"{nombre}({n})", funcion(n)
    if opcion == "8":
        n = pedir_numero("Número: ")
        decimales = pedir_numero("Cantidad de decimales: ")
        return f"Redondeo({n}, {decimales})", operaciones.redondeo(n, decimales)
    if opcion == "12":
        numeros = pedir_lista_numeros("Números separados por espacios: ")
        return f"Promedio({numeros})", operaciones.promedio(numeros)


def main():
    # El ciclo se repite hasta que el usuario elija salir
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion == "13":
            mostrar_historial()
            continue

        if opcion == "14":
            limpiar_historial()
            continue

        if opcion not in DOS_NUMEROS and opcion not in UN_NUMERO and opcion not in ("8", "12"):
            print("Opción no válida")
            continue

        try:
            descripcion, resultado = ejecutar_operacion(opcion)
        except ValueError as error:
            print("Error:", error)
            continue
        print("Resultado:", resultado)
        historial.append(f"{descripcion} = {resultado}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma terminado.")
