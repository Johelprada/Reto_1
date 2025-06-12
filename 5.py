# Función para verificar si dos palabras tienen los mismos caracteres
def tienen_mismos_caracteres(palabra1, palabra2):
    # Convertir a minúsculas para comparar
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Si no tienen la misma longitud, no pueden tener los mismos caracteres
    if len(palabra1) != len(palabra2):
        return False
    
    # Contar caracteres en cada palabra
    for letra in palabra1:
        contador1 = 0
        contador2 = 0
        
        # Contar cuántas veces aparece la letra en la primera palabra
        for char in palabra1:
            if char == letra:
                contador1 += 1
        
        # Contar cuántas veces aparece la letra en la segunda palabra
        for char in palabra2:
            if char == letra:
                contador2 += 1
        
        # Si los contadores no coinciden, no son anagramas
        if contador1 != contador2:
            return False
    
    return True

# Función para filtrar palabras que tienen anagramas
def filtrar_anagramas(lista_palabras):
    resultado = []
    
    # Revisar cada palabra de la lista
    for i in range(len(lista_palabras)):
        palabra_actual = lista_palabras[i]
        encontro_pareja = False
        
        # Comparar con todas las otras palabras
        for j in range(len(lista_palabras)):
            if i != j:  # No comparar la palabra consigo misma
                if tienen_mismos_caracteres(palabra_actual, lista_palabras[j]):
                    encontro_pareja = True
                    break
        
        # Si encontró pareja y no está ya en el resultado, agregarla
        if encontro_pareja and palabra_actual not in resultado:
            resultado.append(palabra_actual)
    
    return resultado

# Programa principal
print("FILTRADOR DE ANAGRAMAS")
print("Ingresa palabras separadas por espacios")

entrada = input("Escribe las palabras: ")
palabras = entrada.split()

print("Lista ingresada:", palabras)

# Filtrar anagramas
resultado = filtrar_anagramas(palabras)
print("Palabras con los mismos caracteres:", resultado)

# Mostrar con quien hacen pareja las palbras
if len(resultado) > 0:
    print("\nComparaciones encontradas:")
    for palabra in resultado:
        print(f"'{palabra}' tiene pareja:")
        for otra_palabra in palabras:
            if palabra != otra_palabra and tienen_mismos_caracteres(palabra, otra_palabra):
                print(f"  - '{palabra}' y '{otra_palabra}' tienen los mismos caracteres")
else:
    print("No se encontraron palabras con los mismos caracteres")