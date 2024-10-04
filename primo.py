print("Números primos")

limite = 104750
contador_primos=0

def es_primo(n): #funcion para identificar un numero primo
    if n <= 1: #revisando que sea mayor o igual a 1
        return False
    for i in range(2, int(n ** 0.5) + 1):#se comprueba si es divisible entre 2
        if n % i == 0: #se comprueba el residu
            return False
    return True #retorna los numeros primos

for elemento in range(2, limite + 1):
    if es_primo(elemento): #si es primo se imprime 
        contador_primos=contador_primos+1 #llevando la cuenta de numeros primos
        print(elemento)

print("Total de primos: " + str(contador_primos))