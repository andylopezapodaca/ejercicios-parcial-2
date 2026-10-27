from unittest import case


nombre = ""
frecuenciadecomprasanual = 0
preferenciasdecompras = ""
metododepago = ""
ubicacion = ""
telefono = 0
cumpleanos = 0

print("Bienvenido al sistema de registro de clientes")
print("Por favor, ingrese la información del cliente a continuación:")
print("--------------------ingrese al menu principal------------------------------")
print("1. Agregar cliente")
print("2. Ver frecuencia de compras anual")
print("3. Ver preferencias de compras")
print("4. Ver método de pago")
print("5. Ver ubicación")
print("6. Ver teléfono")
print("7. Ver cumpleaños")
print("8. Salir del sistema")
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
        print("Cliente agregado exitosamente.")
    case 2:
        print("nombre", nombre, "frecuencia de compras anual", frecuenciadecompras, "preferencias de compras", preferenciasdecompras, "método de pago", metododepago, "ubicación", ubicacion, "teléfono", telefono, "cumpleaños", cumpleanos
              )
case 3: 
nombre = ""
frecuenciadecomprasanual = 0   
preferenciasdecompras = ""
metododepago = ""
ubicacion = ""
telefono = 0
cumpleanos = 0