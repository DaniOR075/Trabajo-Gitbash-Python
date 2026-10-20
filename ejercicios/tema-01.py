# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: Daniel Santiago Orjuela Rojas
# Mi app se llama: CuentaClara (Posible eslogan "Hoy se fia, mañana no")
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:

# nombre = "Kamilo"
# edad = 0
# estatura = 1.80

# print(f"Soy {nombre}, tengo {edad} años y mido {estatura} m")
# print()


# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:
# a = "100"
# b = 100
# c = 100.0
# d = "cien"

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# Respuesta:"100" y 100 no son lo mismo ya que las comillas en el primero hace que python lo tome como un tipo de dato str(texto) y no como un int (numero entero)



# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:
# valorCuenta = int(input("Valor a pagar:"))
# personasQuePagan = int(input("Cuantas personas van a pagar la cuenta:"))
# porcentajePropina = int(input("Porcentaje del servicio:"))

# calculoPropina = valorCuenta * porcentajePropina / 100
# calculoTotal = valorCuenta + calculoPropina
# pagoIndividual = calculoTotal / personasQuePagan


# print(f"Propina:        ${calculoPropina:,.0f}")
# print(f"Total:          ${calculoTotal:,.0f}")
# print(f"Cada uno paga:  ${pagoIndividual:,.0f}")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:
# precio = int(input("Precio del producto: "))
# unidades = int(input("Unidades: "))
# print(f"Total a pagar: ${precio * unidades}")

# Error 1: el input por si solo solo devuelve str y no int, entonces el primer error seria intentar multiplicar dos str
# Error 2: despues seria la forma de concatenacion, teniendo en cuenta que vamos a concatenar str con int debemos usar otro metodo que seria f{}


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:
producto = input("Nombre del producto: ")
unidades = int(input("Unidades: "))
precio = int(input("Precio por unidad: "))

valorTotal = unidades * precio

print("===== INVENTARIO =====")
print(f"Producto:     {producto}")
print(f"Unidades:     {unidades}")
print(f"Precio:       ${precio:,}")
print(f"Valor total:  ${valorTotal:,}")
print("======================")



# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================