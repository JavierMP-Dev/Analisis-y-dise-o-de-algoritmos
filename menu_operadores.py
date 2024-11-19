
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

def obtNum():
    num1 = int(input("Num1-->"))
    num2 = int(input("Num2-->"))
    return num1, num2

#Funcion principal
def calculadora():
  
    while True:
        print("Menu Calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        print("Elige una opcion")
        opc = int(input("Opcion: "))

        if opc == 1:
            num1, num2 = obtNum()
            suma(num1, num2)

        elif opc == 2:
            num1, num2 = obtNum()
            resta(num1, num2)

        elif opc == 3:
            num1, num2 = obtNum()
            multi(num1, num2)

        elif opc == 4:
            num1, num2 = obtNum()
            divi(num1, num2)
        else:
            break
        
calculadora()