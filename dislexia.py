def dividir_silabas(palabra):
    vocales = "aeiouáéíóúü"
    silabas = []
    silaba = ""

    for letra in palabra:
        silaba += letra
        if letra.lower() in vocales:
            silabas.append(silaba)
            silaba = ""
    
    if silaba:
        silabas[-1] += silaba
    return silabas

def alterar_silabas(palabra):
    silabas = dividir_silabas(palabra)
    if len(silabas) > 1:
        silabas[0], silabas[-1] = silabas[-1], silabas[0]
    return "".join(silabas)

def procesar_frase(frase):
    palabras = frase.split()
    nuevas_palabras = [alterar_silabas(palabra) for palabra in palabras]
    return " ".join(nuevas_palabras)

frase = input("Di una wea po aweonao: ")
frase_alterada = procesar_frase(frase)
print("\nFrase qlia estrambotica:")
print(frase_alterada)
