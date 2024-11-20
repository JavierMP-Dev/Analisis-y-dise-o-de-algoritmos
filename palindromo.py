def palindromo_librerias():
    palabra = input("Digite una palabra: ")
    palabra = palabra.lower()
    
    palabra = palabra.replace(" ", "")
    if palabra == palabra[::-1]:
        print("Es palindromo")
    else:
        print("No es palindromo")
            

print("Palindromos")
palindromo_librerias() 