import random
import string
import time

# SALUDO
a = "\nBienvenido al generador de contraseñas\n"
for letra in a:
    print(letra, end="", flush=True)
    time.sleep(0.05)

b = "\nTipos de dificultad:\n"
for letra in b:
    print(letra, end="", flush=True)
    time.sleep(0.05)

# DIFICULTADES
d1 = "\n1. Simple (Solo letras)\n"
for letra in d1:
    print(letra, end="", flush=True)
    time.sleep(0.02)

d2 = "2. Avanzada (Letras y números)\n"
for letra in d2:
    print(letra, end="", flush=True)
    time.sleep(0.02)

d3 = "3. Compleja (Letras, números y caracteres especiales)\n"
for letra in d3:
    print(letra, end="", flush=True)
    time.sleep(0.02)

# SELECCIÓN DE DIFICULTAD Y LONGITUD
while True:
    dificultad = input("\n¿Cuál es la dificultad que desea para su contraseña? (1, 2 o 3): ")
    if dificultad not in ["1", "2", "3"]:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
        continue
    break

while True:
    try:
        caracteres = int(input("Ingrese la cantidad de caracteres que desea para su contraseña (máx 18): "))
        if caracteres > 18:
            print("Demasiados caracteres. Inténtalo de nuevo.")
        elif caracteres <= 0:
            print("La cantidad de caracteres debe ser mayor a 0. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# GENERACIÓN DE CONTRASEÑAS
if dificultad == "1":
    print("Has seleccionado dificultad simple")
    # Solo letras
    contra_generada = ''.join(random.choice(string.ascii_letters) for _ in range(caracteres))
    print(f"Tu contraseña generada es: {contra_generada}")

elif dificultad == "2":
    print("Has seleccionado dificultad avanzada")
    # Letras y números
    contra_generada = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(caracteres))
    print(f"Tu contraseña generada es: {contra_generada}")

elif dificultad == "3":
    print("Has seleccionado dificultad compleja")
    # Letras, números y caracteres especiales
    contra_generada = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(caracteres))
    print(f"Tu contraseña generada es: {contra_generada}")