# Calculadora

## Descripción
Calculadora de consola en Python que permite realizar operaciones matemáticas básicas y avanzadas desde un menú.
Valida las entradas del usuario, evita errores como la división entre cero, permite hacer varias operaciones
sin reiniciar el programa y guarda un historial de los cálculos de la sesión.

## Operaciones y estados

| N.º | Operación | Estado |
|-----|-----------|--------|
| - | Suma | ✅ Completada |
| - | Resta | ✅ Completada |
| - | Multiplicación | ✅ Completada |
| - | División | ✅ Completada |
| 1 | Potencia | ✅ Completada |
| 2 | Módulo | ✅ Completada |
| 3 | Raíz cuadrada | ✅ Completada |
| 4 | Porcentaje | ✅ Completada |
| 5 | Valor absoluto | ✅ Completada |
| 6 | Factorial | ✅ Completada |
| 7 | Promedio | ✅ Completada |
| 8 | Redondeo | ✅ Completada |
| 9 | Validación de entradas | ✅ Completada |
| 10 | División por cero | ✅ Completada |
| 11 | Mejorar el menú | ✅ Completada |
| 12 | Repetir operaciones | ✅ Completada |
| 13 | Historial de operaciones | ✅ Completada |
| 14 | Limpiar historial | ✅ Completada |
| 15 | Mejorar documentación | ✅ Completada |

## Estructura del proyecto

| Archivo | Contenido |
|---------|-----------|
| `calculadora.py` | Menú, entrada de datos, resultados, historial y ciclo principal |
| `operaciones.py` | Funciones matemáticas y sus validaciones |

## Tecnologías
- Python 3 (solo biblioteca estándar)
- Git
- GitHub
- Markdown

## Instalación y ejecución
```bash
git clone https://github.com/Shadogshow/Calculadora.git
cd Calculadora
python3 calculadora.py
```

## Menú
```
========== CALCULADORA ==========
--- Operaciones básicas ---
  1. Suma
  2. Resta
  3. Multiplicación
  4. División
--- Operaciones avanzadas ---
  5. Potencia
  6. Módulo (residuo)
  7. Porcentaje (X % de Y)
  8. Redondeo a n decimales
--- Operaciones con un número ---
  9. Raíz cuadrada
 10. Valor absoluto
 11. Factorial
--- Operaciones con varios números ---
 12. Promedio
--- Historial ---
 13. Ver historial
 14. Limpiar historial
---------------------------------
  0. Salir
=================================
```

## Ejemplos de uso

**Porcentaje** (15 % de 200):
```
Elige una opción: 7
Porcentaje (X): 15
Cantidad (Y): 200
Resultado: 30.0
```

**Promedio de varios números:**
```
Elige una opción: 12
Números separados por espacios: 4 8 6
Resultado: 6.0
```

**Redondeo:**
```
Elige una opción: 8
Número: 3.14159
Cantidad de decimales: 2
Resultado: 3.14
```

**División entre cero** (el programa no se cierra):
```
Elige una opción: 4
Primer número: 10
Segundo número: 0
Error: No se puede dividir entre cero
```

**Factorial de un número negativo:**
```
Elige una opción: 11
Número: -3
Error: El factorial solo existe para enteros no negativos
```

**Entrada no numérica** (se vuelve a pedir el dato):
```
Elige una opción: 1
Primer número: hola
Entrada no válida: escribe un número.
Primer número: 2
Segundo número: 3
Resultado: 5.0
```

**Historial:**
```
Elige una opción: 13
--- Historial de operaciones ---
1. Porcentaje(15.0, 200.0) = 30.0
2. Promedio([4.0, 8.0, 6.0]) = 6.0
3. Redondeo(3.14159, 2.0) = 3.14

Elige una opción: 14
Historial borrado.
```

## Autor
Alejandro Isai Sandoval Montano
