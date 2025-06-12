def es_palindromo(palabra):
     # Se convierten  las mayusculas a minisculas 
    palabra = palabra.lower()
    longitud = len(palabra)
    #dado que si son iguales se puede optimizar mirando solo hasta la mitad de la palabra
    for i in range(longitud // 2):
         # Comparar carácter del inicio con carácter del final
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    
    return True # Si todos los pares coinciden entonces es palíndromo

# Programa principal
print("Validador de Palíndromos")
# Se le solicita la palabra al usuario
palabra = input("Ingresa una palabra: ")

# se verifica si es palíndromo y se muestra el resultado
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

