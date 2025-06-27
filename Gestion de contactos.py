import os
import time

def mostrar_menu():
    print("\nGestión de Contactos")
    print("-" * 30)
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    print("-" * 30)

def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if nombre in contactos:
        print("El contacto ya existe.")
        return

    while True:
        telefono = input("Ingrese número de celular de 9 dígitos (debe comenzar con 9): ").strip()
        if telefono.isdigit() and len(telefono) == 9 and telefono[0] == "9":
            break
        else:
            print("Número inválido. Debe tener 9 dígitos y comenzar con 9.")

    while True:
        email = input("Ingrese el correo electrónico: ").strip()
        if "@" in email and "." in email:
            arroba_index = email.index("@")
            punto_index = email.rfind(".")
            if 0 < arroba_index < punto_index < len(email) - 1:
                break
            else:
                print("Correo inválido. Verifique la posición de '@' y '.'.")
        else:
            print("Correo inválido. Debe contener '@' y '.' en la parte del dominio.")

    contactos[nombre] = {"Teléfono": telefono, "Email": email}
    print(f"Contacto '{nombre}' agregado exitosamente.")


def buscar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
    if nombre in contactos:
        print(f"\nDetalles del contacto '{nombre}':")
        print(f"Teléfono: {contactos[nombre]['Teléfono']}")
        print(f"Email: {contactos[nombre]['Email']}")
    else:
        print("El contacto no existe.")

def editar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a editar: ").strip()
    if nombre in contactos:
        print(f"\nDetalles actuales del contacto '{nombre}':")
        print(f"Teléfono: {contactos[nombre]['Teléfono']}")
        print(f"Email: {contactos[nombre]['Email']}")
        print("\n¿Qué desea editar?")
        print("1. Teléfono")
        print("2. Email")
        print("3. Nombre")
        print("4. Cancelar")
        opcion = input("Seleccione una opción (1, 2, 3 o 4): ").strip()
        if opcion == "1":
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ").strip()
            contactos[nombre]["Teléfono"] = nuevo_telefono
            print("Teléfono actualizado exitosamente.")
        elif opcion == "2":
            nuevo_email = input("Ingrese el nuevo correo electrónico: ").strip()
            contactos[nombre]["Email"] = nuevo_email
            print("Email actualizado exitosamente.")
        elif opcion == "3":
            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
            if nuevo_nombre in contactos:
                print("Ya existe un contacto con ese nombre. Intente con otro.")
            else:
                contactos[nuevo_nombre] = contactos[nombre] 
                del contactos[nombre]  
                print(f"Nombre actualizado exitosamente. Ahora se llama '{nuevo_nombre}'.")
        elif opcion == "4":
            print("Edición cancelada. Volviendo al menú principal.")
            return
        else:
            print("Opción inválida.")
    else:
        print("El contacto no existe.")

def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado exitosamente.")
    else:
        print("El contacto no existe.")

def mostrar_todos_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
    else:
        print("\nLista de contactos:")
        for nombre, detalles in contactos.items():
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {detalles['Teléfono']}")
            print(f"Email: {detalles['Email']}")

def main():
    contactos = {}
    while True:
        os.system("cls")  
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            editar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            mostrar_todos_contactos(contactos)
        elif opcion == "6":
            print("Saliendo", end="", flush=True)
            time.sleep(1)
            for i in range(3):  
                print(".", end="", flush=True)
                time.sleep(1)
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        time.sleep(2)  

if __name__ == "__main__":
    main()

