
def pedir_datos():
    base = int(input("Ingresa la base-->"))
    altura = int(input("Ingresa la altura-->"))
    return base, altura

def calcular_area(base, altura):
    area = base * altura
    return area

print("Calculadora de area")
base, altura =  pedir_datos()
area = calcular_area(base, altura)
print(f"El área del rectangulo es: {area}")