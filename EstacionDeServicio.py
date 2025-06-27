import time
import msvcrt  

def ingresar_pin():
    pin = ""
    print("Ingrese la contraseña de su tarjeta: ", end="", flush=True)
    while len(pin) < 4:
        tecla = msvcrt.getch()  
        if tecla.isdigit():  
            pin += tecla.decode("utf-8")  
            print("*", end="", flush=True)  
        elif tecla == b"\r":  
            break
    print()  
    return pin

print("Bienvenido a la Estación de Servicio\n")

# Precios por tipo de combustible
precios_combustible = {
    93: 800,  
    95: 900,  
    97: 1000,  
}

while True:
    try:
        nivel = int(input("¿Cuál es su nivel de combustible? "))
        if nivel < 0 or nivel >= 100:
            print("El nivel de combustible no es válido. Intente de nuevo.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

if nivel < 10 or nivel > 0:
    print("Nivel de combustible adecuado, ¿desea cargar combustible de igual forma?")
    print("1. Sí")
    print("2. No")

    while True:
        respuesta = input("Respuesta: ").strip().lower()
        if respuesta in ["1", "si"]:
            print("")
            print("Tipos de combustible:")
            print("1. 93 ($800 por litro)")
            print("2. 95 ($900 por litro)")
            print("3. 97 ($1000 por litro)\n")

            while True:
                try:
                    tipo_combustible = (input("Seleccione tipo de combustible: "))
                    if tipo_combustible not in ["1", "2", "3", "93", "95", "97"]:
                        print("Opción no válida. Intente nuevanmente\n")
                    else:
                        if tipo_combustible == "1" or tipo_combustible == "93":
                            precio_por_litro = precios_combustible[93]
                            tipo = 93
                        elif tipo_combustible == "2" or tipo_combustible == "95":
                            precio_por_litro = precios_combustible[95]
                            tipo = 95
                        elif tipo_combustible == "3" or tipo_combustible == "97":
                            precio_por_litro = precios_combustible[97]
                            tipo = 97
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            print(f"Ha seleccionado combustible {tipo} a ${precio_por_litro} por litro.\n")
            while True:
                try:
                    cantidad = int(input("¿Cuánto desea cargar? "))
                    if cantidad <= 0 or nivel + cantidad > 100:
                        print(f"La cantidad no es válida. Puede cargar un máximo de {100 - nivel} litros. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    
            total = cantidad * precio_por_litro
            print(f"El total a pagar es: ${total} pesos.")
            
            # Método de pago
            print("")
            print("Seleccione el método de pago:")
            print("1. Débito")
            print("2. Efectivo")

            while True:
                metodo_pago = input("Método de pago: ").strip()
                print("")
                if metodo_pago == "1" or metodo_pago == "debito":  # Pago con débito
                    while True:
                        pin = ingresar_pin()  
                        if len(pin) == 4 and pin.isdigit():
                            
                            print("Procesando pago", end="", flush=True)
                            time.sleep(2)
                            for i in range(3):  
                                print(".", end="", flush=True)
                                time.sleep(1)
                            print("")
                            print("Pago exitoso.")
                            print (f"Ha cancelado ${total}\n")
                            break
                        else:
                            print("El PIN debe tener exactamente 4 dígitos. Intente de nuevo.")
                    break
                elif metodo_pago == "2"  or metodo_pago == "efectivo":  # Pago con efectivo
                    while True:
                        try:
                            efectivo = int(input("Ingrese dinero: "))
                            if efectivo < total:
                                print("El dinero ingresado no es suficiente. Intente de nuevo.\n")
                            else:
                                vuelto = efectivo - total
                                print(f"Pago realizado con éxito. Su vuelto es: ${vuelto} pesos.\n")
                                break
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                    break
                else:
                    print("Opción no válida. Seleccione 1 o 2.")
            
            print("Cargando combustible", end="", flush=True)
            time.sleep(2)
            for i in range(3): 
                print(".", end="", flush=True)
                time.sleep(1)
            print("\n")
            print(f"Se han cargado {cantidad} litros de combustible.") 
            print(f"Su nivel de combustible ahora es de: {nivel + cantidad} litros.\n")   
            
            #Recibo de compra
            print("Recibo de compra:")
            print(f"Tipo de combustible: {tipo}")
            print(f"Cantidad: {cantidad} litros")
            print(f"Precio por litro: ${precio_por_litro} pesos")
            print(f"Total: ${total} pesos")
            print(f"Pago: {'Débito' if metodo_pago == '1' else 'Efectivo'}")
            print(f"Vuelto: ${vuelto} pesos\n" if metodo_pago == "2" else "Sin vuelto\n")                                
            print("Gracias por su compra.\n")
            break
        elif respuesta in ["2", "no"]:
            print("")
            print("Cancelando", end="", flush=True)
            time.sleep(2)
            for i in range(3):  
                print(".", end="", flush=True)
                time.sleep(1)
            print("\n")
            print("No se ha cargado combustible. Gracias por su visita.\n")
            break  
        else:
            print("Respuesta no válida. Por favor, seleccione '1' o '2'.")
else:
    print("Su nivel de combustible es adecuado. No requiere cargar combustible.")

