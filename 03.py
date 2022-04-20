# Ej. 1:

'''

def calculadora(num1, num2, op):
    if op == "+":
        r = (num1 + num2)
    elif op == "-":
        r = (num1 - num2)
    elif op == "/":
        r = (num1 / num2)
    elif op == "*":
        r = (num1 * num2)
    
    print("\n", num1, op, num2, "=", r)

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    op = input ("Ingrese la operación (+, -, *, /): ")

    calculadora(num1, num2, op)

main()

'''

# Ej. 2:

'''

def orden(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        print(num3, num2, num1)
    elif num1 > num3 and num3 > num2:
        print(num2, num3, num1)
    elif num2 > num1 and num1 > num3:
        print(num3, num1, num2)
    elif num2 > num3 and num3 > num1:
        print(num1, num3, num2)
    elif num3 > num1 and num1 > num2:
        print(num2, num1, num3)
    elif num3 > num2 and num2 > num1:
        print(num1, num2, num3)

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    print("\nLos números ordenados en forma ascendente son:")
    orden(num1, num2, num3)

main()

'''

# Ej. 3:

'''

def signo(num):
    s = "positivo"
    if num == 0:
        s = "cero"
    elif num < 0:
        s = "negatvo"
    return s

def tipo(num):
    t = "real"
    if num > 0 and num % 1 == 0 :
        t = "entero natural"
    elif num <= 0 and num % 1 == 0:
        t = "entero"
    return t

def main():
    num = int(input("Ingrese un número: "))

    print("El número es", signo(num), "y", tipo(num))

main()

'''

# Ej. 4:

'''

def mayor(num1, num2):
    m = num1
    if num2 > num1:
        m = num2
    return m

def menor(num1, num2):
    min = num1
    if num2 < num1:
        min = num2
    return min

def valid(highest, lowest, num):
    r = "NO"
    if num >= lowest and num <= highest:
        r = "SI"
    return r

def main():
    num1 = int(input("Ingrese un número A: "))
    num2 = int(input("Ingrese un número B: "))

    highest = mayor(num1, num2)
    lowest = menor(num1, num2)

    num = highest - lowest

    print(valid(highest, lowest, num), "cumple la condicion.")

main()

'''

# Ej. 5:

'''

def valid(d, m, y):
    r = "La fecha es incorrecta."
    if d >= 1 and d <= 29 and m >= 1 and m <= 12:
        r = "La fecha es correcta."
    print(r)

def main():
    d = int(input("Ingrese el dia: "))
    m = int(input("Ingrese el mes: "))
    y = int(input("Ingrese el año: "))

    valid(d, m, y)

main()

'''

# Ej. 6:

'''

def hl(num1):
    m = "mayor"
    if num1 % 2 == 0:
        m = "menor"    
    return m

def check(num1, num2, m):
    if m == "mayor" and num2 > num1:
        print("Correcto!")
    elif m == "menor" and num2 < num1:
        print("Correcto!")
    else:
        print("Incorrecto!")        

def main():
    num1 = int(input("Ingrese un número entero positivo: "))
    print("Ingrese un número", hl(num1), "que", str(num1) + ": ", end="") 
    num2 = int(input())
    
    check(num1, num2, hl(num1))

main()

'''

# Ej. 7:

'''

def mayor(num1, num2):
    m = num1
    if num2 > num1:
        m = num2
    return m

def menor(num1, num2):
    min = num1
    if num2 < num1:
        min = num2
    return min

def mid(num1, num2, num3):
    min = num3
    if num1 > num2 and num1 < num3:
        min = num1
    elif num2 > num1 and num2 < num3:
        min = num2
    return min

def check(m, min, mid):
    r = "NO Están igualmente distanciados!"
    if m - mid == mid - min:
        r = "Están igualmente distanciados!"
    return r

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    mimayor = (mayor(num1, mayor(num2, num3)))
    mimenor = (menor(num1, menor(num2, num3)))
    mimid = (mid(num1, num2, num3))

    print(check(mimayor, mimenor, mimid))

main()

'''

#Ej. 8:

def rec(num1, num2, num3):
    num4 = 0
    if num1 < 4 or num2 < 4 or num3 < 4:
        num4 = int(input("Ingrese la nota del recuperatorio: "))    
    return num4

def promedio(num1, num2, num3, num4):
    prom = (num1 + num2 + num3) / 3
    if num4 != 0:
        prom = (num1 + num2 + num3 + num4) / 4
    return prom

def check(num1, num2, num3, num4, prom):
    f = "promociona la materia."
    if prom > 4 and prom < 7:
        f = "debe rendir examen final."
    elif prom < 4:
        f = "fue aplazado."
        if num4 != 0 and num4 >= 4:
            f = "debe rendir examen final."
    return f

def main():
    num1 = int(input("Ingrese la nota del primer parcial: "))
    num2 = int(input("Ingrese la nota del segundo parcial: "))
    num3 = int(input("Ingrese la nota del tercer parcial: "))

    mirec = rec(num1, num2, num3)
    miprom = promedio(num1, num2, num3, mirec)

    print("\nPromedio general = ", miprom)
    
    micheck = check(num1, num2, num3, mirec, miprom)

    print("El alumno", micheck)

main()