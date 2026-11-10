100 %
nombre = []
frecuenciadecomprasanual = []
preferenciasdecompras = []
metododepago = []
ubicacion = []
telefono = []
cumpleanos = ¨[]
opcion = 0

while True:
print("Bienvenido al sistema de registro de clientes")
print("Por favor, ingrese la información del cliente a continuación:")
print("--------------------ingrese al menu principal------------------------------")
print("1. Agregar cliente")
print("2. Mostrar información del cliente")
print("3. Eliminar información del cliente")
print("4. Modificar información del cliente")
print("5. Salir del sistema")
opcion = int(input("Ingrese el número de la opción que desea realizar: "))

match opcion:
    case 1:
        nombre = input("Ingrese el nombre del cliente: ")
        frecuenciadecompras = int(input("Ingrese la frecuencia de compras anual: "))
        preferenciasdecompras = input("Ingrese las preferencias de compras: ")
        metododepago = input("Ingrese el método de pago: ")
        ubicacion = input("Ingrese la ubicación: ")
        telefono = int(input("Ingrese el teléfono: "))
        cumpleanos = int(input("Ingrese el cumpleaños (en formato DDMM): "))
        print("Cliente agregado exitosamente, con el ID ")
    case 2:
        print("nombre", nombre, "frecuencia de compras anual", frecuenciadecompras, "preferencias de compras", preferenciasdecompras, "método de pago", metododepago, "ubicación", ubicacion, "teléfono", telefono, "cumpleaños", cumpleanos)
    case 3:
        nombre = ""
        frecuenciadecomprasanual = 0   
        preferenciasdecompras = ""
        metododepago = ""
        ubicacion = ""
        telefono = 0
        cumpleanos = 0
    case 4:
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        frecuenciadecompras = int(input("Ingrese la nueva frecuencia de compras anual: "))
        preferenciasdecompras = input("Ingrese las nuevas preferencias de compras: ")
        metododepago = input("Ingrese el nuevo método de pago: ")
        ubicacion = input("Ingrese la nueva ubicación: ")
        telefono = int(input("Ingrese el nuevo teléfono: "))
        cumpleanos = int(input("Ingrese el nuevo cumpleaños (en formato DDMM): "))
        print("Información del cliente modificada exitosamente.")
    case 5:
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    case _:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
