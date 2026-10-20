# Aquí empieza mi app
print("=================================================")
print("               Cuentas Claras                    ")
print("             Gestión de fiados")
print("            Hoy se fia, mañana no")
print("=================================================")


nombreCliente = input("Nombre del cliente: ")
valorCompraFiada = int(input("¿Cuánto vale su compra fiada? $"))
cantidadProductos = int(input("¿Cuántos productos lleva? "))

print("=================================================")
print(f"Cliente: {nombreCliente}")
print(f"Cantidad de productos: {cantidadProductos}")
print(f"Valor de la compra fiada: ${valorCompraFiada:,}".replace(",", "."))
print("=================================================")
print("¡Bienvenido a Cuentas Claras!")
