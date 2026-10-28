# Aquí empieza mi app

print("=================================================")
print("               Cuentas Claras                    ")
print("             Gestión de fiados                    ")
print("            Hoy se fía, mañana no                 ")
print("=================================================")

print("¡Bienvenido a Cuentas Claras!")

comprasFiadas = []
continuar = True

while continuar:

    print()
    print("============== MENÚ PRINCIPAL ==============")
    print("1. Registrar compra fiada")
    print("2. Consultar compras registradas")
    print("3. Calcular cuotas")
    print("4. Salir")
    print("============================================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        print()
        print("========= REGISTRAR COMPRA FIADA =========")

        nombreCliente = input("Nombre del cliente: ")
        valorCompraFiada = int(
            input("¿Cuánto vale la compra fiada? $")
        )
        cantidadProductos = int(
            input("¿Cuántos productos lleva? ")
        )

        if valorCompraFiada > 0 and cantidadProductos > 0:

            compra = [
                nombreCliente,
                valorCompraFiada,
                cantidadProductos
            ]

            comprasFiadas.append(compra)

            print()
            print("¡Compra fiada registrada correctamente!")
            print(f"Cliente: {nombreCliente}")
            print(f"Cantidad de productos: {cantidadProductos}")
            print(
                f"Valor de la compra: "
                f"${valorCompraFiada:,}".replace(",", ".")
            )
            print(f"Total de compras registradas: {len(comprasFiadas)}")

        else:
            print()
            print("Error: el valor y la cantidad deben ser mayores que cero.")

    elif opcion == "2":

        print()
        print("========= COMPRAS REGISTRADAS =========")

        if len(comprasFiadas) > 0:

            for i in range(len(comprasFiadas)):

                print()
                print(f"Compra número {i + 1}")
                print(f"Cliente: {comprasFiadas[i][0]}")
                print(f"Cantidad de productos: {comprasFiadas[i][2]}")
                print(
                    f"Valor de la compra: "
                    f"${comprasFiadas[i][1]:,}".replace(",", ".")
                )
                print("---------------------------------------")

            print(f"Total de compras registradas: {len(comprasFiadas)}")

        else:
            print("Todavía no hay compras registradas.")

    elif opcion == "3":

        print()

        if len(comprasFiadas) > 0:

            print("========= SELECCIONAR COMPRA =========")

            for i in range(len(comprasFiadas)):
                print(
                    f"{i + 1}. {comprasFiadas[i][0]} - "
                    f"${comprasFiadas[i][1]:,}".replace(",", ".")
                )

            numeroCompra = int(
                input("¿De qué compra quieres calcular las cuotas? ")
            )

            if numeroCompra >= 1 and numeroCompra <= len(comprasFiadas):

                # Obtener la compra seleccionada
                compraSeleccionada = comprasFiadas[numeroCompra - 1]

                valorCompraFiada = compraSeleccionada[1]
                nombreCliente = compraSeleccionada[0]

                cantidadCuotas = int(
                    input("¿En cuántas cuotas pagará el cliente? ")
                )

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
                    print("=============================================")

                else:
                    print("Error: las cuotas deben ser mayores que cero.")

            else:
                print("Número de compra no válido.")

        else:
            print("Primero debes registrar una compra fiada.")

    elif opcion == "4":

        print()
        print("=== Gracias por utilizar Cuentas Claras. ===")
        print("============== ¡Hasta pronto! ==============")

        continuar = False

    else:
        print("Opción no válida. Selecciona una opción del 1 al 4.")