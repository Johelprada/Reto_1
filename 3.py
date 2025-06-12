def es_primo(numero):
    if numero < 2:
        return False
    # Los números menores a 2 no son primos por definición
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True

def filtrar_primos(lista_numeros):
    # Función que filtra solo los números primos de una lista

    primos = []# Lista en la cual se almacenan los números primos
    
    for numero in lista_numeros:
        # Si es primo, agregarlo a la lista de resultados
        if es_primo(numero):
            primos.append(numero)
    
    return primos

# Interfas del usuario
print("FILTRADOR DE NÚMEROS PRIMOS")
print("Ingresa números separados por espacios")

entrada = input("Escribe los números: ")
numeros_texto = entrada.split()

# Convertir a enteros
numeros = []
for num in numeros_texto:
    numeros.append(int(num))

print("Lista ingresada:", numeros)

# Filtrar primos
resultado = filtrar_primos(numeros)
print("Números primos:", resultado)

