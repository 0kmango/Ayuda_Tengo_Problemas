import time
import os  

def maquina_de_bebidas():
    stock_coca = 6
    stock_fanta = 4
    stock_sprite = 5
    stock_kem = 4

    while True:
        try:
            os.system("cls")  
            pago = int(input("Ingrese dinero: "))
            if pago <= 0:
                print("Por favor, ingrese un monto válido.")
                input("Presione Enter para continuar...")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

    while True:
        os.system("cls")  
        a = "Opciones Disponibles"
        for letra in a:
            print(letra, end="", flush=True) 
            time.sleep(0.03)
        print("\n____________________________________________")
        print(f"Cocacola: {stock_coca} | Fanta: {stock_fanta} | Sprite: {stock_sprite} | Kem: {stock_kem}")
        print("____________________________________________")
        op1 = "\n1. Cocacola $1500"
        op2 = "\n2. Fanta $1250"
        op3 = "\n3. Sprite $1100"
        op4 = "\n4. Kem $1000"
        op5 = "\n5. Cancelar\n"
        
        for letra in op1:
            print(letra, end="", flush=True) 
            time.sleep(0.03)  
        for letra in op2:
            print(letra, end="", flush=True) 
            time.sleep(0.03)
        for letra in op3:
            print(letra, end="", flush=True) 
            time.sleep(0.03)
        for letra in op4:
            print(letra, end="", flush=True) 
            time.sleep(0.03)
        for letra in op5:
            print(letra, end="", flush=True) 
            time.sleep(0.03)
                
        opc = input("\nSeleccione una opción: ")

        if opc not in ['1', '2', '3', '4', '5']:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue

        if opc == '5':
            print("\nCancelando", end="", flush=True)
            time.sleep(0.2)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            print(f"\nSu reembolso es de {pago} pesos")
            input("Presione Enter para salir...")
            print("\nSaliendo", end="", flush=True)
            time.sleep(0.2)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            break

        if opc == '1':
            precio = 1500
            bebida = "Cocacola"
            if stock_coca == 0:
                print("Lo sentimos, no hay stock de Cocacola.")
                input("Presione Enter para continuar...")
                continue
        elif opc == '2':
            precio = 1250
            bebida = "Fanta"
            if stock_fanta == 0:
                print("Lo sentimos, no hay stock de Fanta.")
                input("Presione Enter para continuar...")
                continue
        elif opc == '3':
            precio = 1100
            bebida = "Sprite"
            if stock_sprite == 0:
                print("Lo sentimos, no hay stock de Sprite.")
                input("Presione Enter para continuar...")
                continue
        elif opc == '4':
            precio = 1000
            bebida = "Kem"
            if stock_kem == 0:
                print("Lo sentimos, no hay stock de Kem.")
                input("Presione Enter para continuar...")
                continue

        if pago < precio:
            while pago < precio:
                os.system("cls")  
                print("Opciones Disponibles")
                print("____________________________________________")
                print(f"Cocacola: {stock_coca} | Fanta: {stock_fanta} | Sprite: {stock_sprite} | Kem: {stock_kem}")
                print("____________________________________________")
                print("\n1. Cocacola $1500")
                print("2. Fanta $1250")
                print("3. Sprite $1100")
                print("4. Kem $1000")
                print("5. Cancelar")
                print("____________________________________________")
                print(f"Dinero insuficiente. Faltan {precio - pago} pesos")
                try:
                    pago += int(input("Ingrese más dinero: "))
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    input("Presione Enter para continuar...")
            vuelto = pago - precio
        else:
            vuelto = pago - precio

        # Actualizar stock aquí para que se refleje inmediatamente en pantalla
        if bebida == "Cocacola":
            stock_coca -= 1
        elif bebida == "Fanta":
            stock_fanta -= 1
        elif bebida == "Sprite":
            stock_sprite -= 1
        elif bebida == "Kem":
            stock_kem -= 1

        # Mostrar pantalla final con stock actualizado y dinero ingresado
        os.system("cls")
        print("Opciones Disponibles")
        print("____________________________________________")
        print(f"Cocacola: {stock_coca} | Fanta: {stock_fanta} | Sprite: {stock_sprite} | Kem: {stock_kem}")
        print("____________________________________________")
        print("\n1. Cocacola $1500")
        print("2. Fanta $1250")
        print("3. Sprite $1100")
        print("4. Kem $1000")
        print("5. Cancelar")
        print("____________________________________________")
        print(f"Haz escogido {bebida} Su vuelto es de {vuelto} pesos")
        
        print("____________________________________________")
        print("¿Desea realizar otra compra?")
        print("1. Sí")
        print("2. No")
        continuar = input("Seleccione una opción: ")

        if continuar == '2' or  continuar.lower() == "no":  
            os.system("cls") 
            print("Gracias por su compra. ¡Hasta luego!")
            print("Saliendo", end="", flush=True)
            time.sleep(0.2)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            break 
        elif continuar == '1' or continuar.lower() == "si":  
            try:
                os.system("cls") 
                pago = int(input("Ingrese dinero: "))
                if pago <= 0:
                    print("Por favor, ingrese un monto válido.")
                    input("Presione Enter para continuar...")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                input("Presione Enter para continuar...")

maquina_de_bebidas()

