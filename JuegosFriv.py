import random
import sys

#Adivina el Número
def adivina_el_numero():
    print("\n=== Adivina el Número ===")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 3  # Máximo de intentos permitidos

    while intentos < max_intentos:
        try:
            adivina = int(input(f"Intento {intentos + 1} de {max_intentos}. Adivina un número entre 1 y 100: "))
            intentos += 1
            if adivina < numero_secreto:
                print("Demasiado bajo.")
            elif adivina > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if intentos == max_intentos and adivina != numero_secreto:
        print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")

#Piedra, Papel o Tijera
def piedra_papel_tijera():
    print("\n=== Piedra, Papel o Tijera ===")
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)
    jugador = input("Elige piedra, papel o tijera: ").lower()
    if jugador not in opciones:
        print("Opción no válida.")
        return
    print(f"Computadora eligió: {computadora}")
    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
        (jugador == "papel" and computadora == "piedra") or \
        (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

#Gato X|O
def gato():
    print("\n=== Gato (Tres en Raya) ===")
    tablero = [" " for _ in range(9)]

    def imprimir_tablero():
        print("\n")
        for i in range(0, 9, 3):
            print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
            if i < 6:
                print("--+---+--")
        print("\n")

    def verificar_ganador(jugador):
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]            
        ]
        for combinacion in combinaciones_ganadoras:
            if all(tablero[pos] == jugador for pos in combinacion):
                return True
        return False

    def tablero_lleno():
        return " " not in tablero

    def movimiento_maquina():
        posiciones_disponibles = [i for i, casilla in enumerate(tablero) if casilla == " "]
        return random.choice(posiciones_disponibles)

    jugador_actual = "X"
    while True:
        imprimir_tablero()
        if jugador_actual == "X":
            try:
                movimiento = int(input("Elige una posición (1-9): ")) - 1
                if tablero[movimiento] == " ":
                    tablero[movimiento] = jugador_actual
                    if verificar_ganador(jugador_actual):
                        imprimir_tablero()
                        print("¡Felicidades! Has ganado.")
                        break
                    elif tablero_lleno():
                        imprimir_tablero()
                        print("¡Es un empate!")
                        break
                    jugador_actual = "O"
                else:
                    print("Esa posición ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Por favor, elige una posición válida (1-9).")
        else:
            print("Turno de la máquina...")
            movimiento = movimiento_maquina()
            tablero[movimiento] = jugador_actual
            if verificar_ganador(jugador_actual):
                imprimir_tablero()
                print("La máquina ha ganado. ¡Mejor suerte la próxima vez!")
                break
            elif tablero_lleno():
                imprimir_tablero()
                print("¡Es un empate!")
                break
            jugador_actual = "X"

#Ahorcado
def ahorcado():
    print("\n=== Ahorcado ===")
    palabras = ["python", "programacion", "juego", "ahorcado", "computadora"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = set()
    intentos = 6

    while intentos > 0:
        estado_actual = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(estado_actual))
        if "_" not in estado_actual:
            print("¡Felicidades! Adivinaste la palabra.")
            break

        letra = input("Adivina una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
        elif letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")

    if intentos == 0:
        print(f"¡Perdiste! La palabra era: {palabra_secreta}")

#Memoria
def juego_de_memoria():
    print("\n=== Juego de Memoria ===")
    secuencia = []
    while True:
        numero = random.randint(1, 9)
        secuencia.append(numero)
        print("Secuencia: ", " ".join(map(str, secuencia)))
        input("Presiona Enter para continuar...")
        print("\n" * 50)
        respuesta = input("Repite la secuencia: ").strip()
        if respuesta != " ".join(map(str, secuencia)):
            print(f"¡Incorrecto! La secuencia era: {' '.join(map(str, secuencia))}")
            break
        print("¡Correcto! La secuencia continúa...\n")

# Menu
def mostrar_menu():
    print("\n=== Menú de Juegos ===")
    print("1. Adivina el Número")
    print("2. Piedra, Papel o Tijera")
    print("3. Tic-Tac-Toe (Tres en Raya)")
    print("4. Ahorcado")
    print("5. Juego de Memoria")
    print("6. Salir")

def ejecutar_juego(opcion):
    if opcion == 1:
        adivina_el_numero()
    elif opcion == 2:
        piedra_papel_tijera()
    elif opcion == 3:
        gato()
    elif opcion == 4:
        ahorcado()
    elif opcion == 5:
        juego_de_memoria()
    elif opcion == 6:
        print("¡Gracias por jugar! Hasta la próxima.")
        sys.exit()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige un juego (1-6): "))
            ejecutar_juego(opcion)
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n¡Gracias por jugar! Hasta la próxima.")
            sys.exit()

        jugar_de_nuevo = input("\n¿Deseas jugar de nuevo o elegir otro juego? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()