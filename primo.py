print("Números primos")

limite = 104750
contador_primos=0
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for elemento in range(2, limite + 1):
    if es_primo(elemento):
        contador_primos=contador_primos+1
        print(elemento)

print("Total de primos: " + str(contador_primos))