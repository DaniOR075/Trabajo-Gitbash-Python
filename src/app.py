# Aquí empieza mi app
print("=================================================")
print("               Cuentas Claras                    ")
print("             Gestión de fiados")
print("            Hoy se fia, mañana no")
print("=================================================")


print("============== MENÚ PRINCIPAL ==============")
print("=======  ¡Bienvenido a Cuentas Claras! =======")

nombreCliente = ""
valorCompraFiada = 0
cantidadProductos = 0
compraRegistrada = False

continuar = True

while continuar:

    print()
    print("============== MENÚ PRINCIPAL ==============")
    print("1. Registrar compra fiada")
    print("2. Consultar última compra")
    print("3. Calcular cuotas")
    print("4. Salir")
    print("============================================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        print()
        print("========= REGISTRAR COMPRA FIADA =========")

        nombreCliente = input("Nombre del cliente: ")
        valorCompraFiada = int(input("¿Cuánto vale la compra fiada? $")
        )
        cantidadProductos = int(input("¿Cuántos productos lleva? ")
        )

        if valorCompraFiada > 0 and cantidadProductos > 0:

            compraRegistrada = True

            print()
            print("¡Compra fiada registrada correctamente!")
            print(f"Cliente: {nombreCliente}")
            print(f"Cantidad de productos: {cantidadProductos}")
            print(
                f"Valor de la compra: "
                f"${valorCompraFiada:,}".replace(",", ".")
            )

        else:
            print()
            print("Error: los valores deben ser mayores que cero.")

    elif opcion == "2":

        print()

        if compraRegistrada:

            print("========= ÚLTIMA COMPRA REGISTRADA =========")
            print(f"Cliente: {nombreCliente}")
            print(f"Cantidad de productos: {cantidadProductos}")
            print(
                f"Valor de la compra: "
                f"${valorCompraFiada:,}".replace(",", ".")
            )

        else:
            print("Todavía no has registrado ninguna compra.")

    elif opcion == "3":

        print()

        if compraRegistrada:

            cantidadCuotas = int(input("¿En cuántas cuotas pagará el cliente? "))

            if cantidadCuotas > 0:

                valorCuota = valorCompraFiada / cantidadCuotas

                print()
                print("============= CÁLCULO DE CUOTAS =============")
                print(f"Cliente: {nombreCliente}")
                print(
                    f"Valor total: "
                    f"${valorCompraFiada:,}".replace(",", ".")
                )
                print(f"Cantidad de cuotas: {cantidadCuotas}")
                print(
                    f"Valor aproximado por cuota: "
                    f"${valorCuota:,.0f}".replace(",", ".")
                )

            else:
                print("Error: la cantidad de cuotas debe ser mayor que cero.")

        else:
            print("Primero debes registrar una compra fiada.")

    # Opción 4: Salir
    elif opcion == "4":

        print()
        print("=== Gracias por utilizar Cuentas Claras. ===")
        print("============== ¡Hasta pronto! ==============")

        continuar = False

    else:
        print("Opción no válida. Selecciona una opción del 1 al 4.")
