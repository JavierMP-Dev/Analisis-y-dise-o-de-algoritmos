
def suma(num1, num2):
    suma = num1 + num2
    print("Suma: ", num1, "+", num2, "=",suma)
    
def resta(num1, num2):
    resta = num1 - num2
    print("Resta:", num1, "-", num2, "=", resta)

def multi(num1, num2):
    multi = num1 * num2
    print("Multiplicacion: ", num1, "*", num2, "=", multi)

def divi(num1, num2):
    divi = num1 / num2
    print("Division: ", num1, "/", num2, "=", divi)

print("Programa de funciones")
num1 = int(input("Num1-->"))
num2 = int(input("Num2-->"))

suma(num1, num2)
resta(num1, num2)
divi(num1, num2)
multi(num1, num2)