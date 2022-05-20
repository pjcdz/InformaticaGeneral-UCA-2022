# Ej. 1:

'''
def palabra(cad):
    if len(cad) >= 2:
        r = cad[-2:]*3
        # print(cad[len(cad)-2:len(cad)], end="")
    else:
        r = "La función ha retornado una palabra vacía"
    return r

def main():
    p = input("Ingrese la palabra: ")
    print(palabra(p))

main()
'''

# Ej. 2:

'''
def palabra(ext, cad):
    r = "La función ha retornado una palabra vacía"
    if len(ext) == 2 and len(cad)>0:
        r = "La funcion retornó: " + ext[0] + cad + ext[-1:]
    return r

def main():
    e = input("Ingrese los extremos: ")
    p = input("Ingrese la palabra: ")

    print(palabra(e, p))

main()
'''

# Ej. 3:

def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

def esPalabra(pal):
    res = True
    i=0
    while i<len(pal):
        if not esLetra2(pal[i]):
            res=False
        i=i+1
    return res

def pal(p):
    while len(p)%2 != 0 or not esPalabra(p):
        p = input("Ingrese una palabra de longitud par: ")
    r = "La función ha retornado: " + p[0: len(p)//2]
    return r

def main():
    p = input("Ingrese una palabra de longitud par: ")
    print(pal(p))

main()