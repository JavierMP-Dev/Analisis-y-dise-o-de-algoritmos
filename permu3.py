# Author: Javier
# Date: 15/10/2024 

def permutaciones(arr, r):
    # funcion de permutaciones
    def backtrack(current_permutation, used):
        # Si la longitud de la permutación actual es r, la imprimimos
        if len(current_permutation) == r:
            print(' '.join(map(str, current_permutation)))
            return
        
        for i in range(len(arr)):
            if not used[i]:  
                # Si el elemento no ha sido uusado se marca
                used[i] = True  
              
                current_permutation.append(arr[i])  
                backtrack(current_permutation, used) 
                 # Eliminar el último elemento para retrocede
                current_permutation.pop() 
                used[i] = False  # Marcar como no usado

    arr.sort()  
    used = [False] * len(arr) 
    backtrack([], used)

#funcion principal

#entrada de datos
def main():
    entrada = input().strip().split()
    N = int(entrada[0])  # elementos
    R = int(entrada[1])  # subelementos
    #lista de elementos
    elementos = list(map(int, input().strip().split()))  

    # Generar y mostrar permutaciones
    permutaciones(elementos, R)

main()