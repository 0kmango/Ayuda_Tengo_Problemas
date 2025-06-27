# Combinaciones Posibles

from itertools import permutations

def genComb(palabra):
    combinaciones = permutations(palabra)
    resultado = set([''.join(combinacion) for combinacion in combinaciones])
    return resultado

palabra = input("\nIngrese una palabra: ")
print(f"\nLa palabra ingresada tiene {len(palabra)} caracteres.")
combinaciones = genComb(palabra)

print(f"\nTodas las combinaciones posibles de '{palabra}' son {len(combinaciones)}\n")

combinaciones = list(combinaciones)
columnas = 6 

for i in range(0, len(combinaciones), columnas):
    fila = combinaciones[i:i + columnas - 2] 
    print(' | '.join(fila))
