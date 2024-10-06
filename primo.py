#print("Números primos")

#import time

#start_time = time.perf_counter()

limite = 104750  #numero limite para encontrar el numero 10001 primo
contador_primos=0  #variable para imprimir iteraciones
arreglo_primos = list()

def es_primo(n): #funcion para identificar un numero primo
    if n <= 1: #revisando que sea mayor o igual a 1
        return False
    for i in range(2, int(n ** 0.5) + 1):#se comprueba si es divisible entre 2
        if n % i == 0: #se comprueba el residuo
            return False
    return True #retorna los numeros primos

for elemento in range(2, limite + 1):
    if es_primo(elemento): #si es primo se imprime 
        contador_primos=contador_primos+1 #llevando la cuenta de numeros primos
        arreglo_primos.append(elemento)
        #print(elemento)  #si se imprime el programa se vuelve 1.5s mas lento
        
#print("Total de primos: " + str(contador_primos))

print(  str(arreglo_primos[-1]))

#print(arreglo_primos[-1])

#end_time = time.perf_counter()
#print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")