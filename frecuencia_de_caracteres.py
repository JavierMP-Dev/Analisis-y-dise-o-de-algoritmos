#programa que cuente la frecuencia de un caracter
'''
Crea un programa que cuente la frecuencia de cada carácter en una cadena de texto.

Entrada:
Una cadena como "abracadabra".

Salida esperada:
Un diccionario como {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}.
'''
def contar(palabra):
    contador = {}

    for letra in palabra:
        if letra.isalpha():
            letra = letra.lower()
            contador[letra] = contador.get(letra, 0) + 1
    return contador
 

print("Contador de caracteres")
palabra = input("Ingresa tu palabra-dddddd->")
contador = contar(palabra)
print(contador)
