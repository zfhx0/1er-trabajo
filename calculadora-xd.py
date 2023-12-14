a1 = False
a2 = False
a3 = False
b1 = False
b2 = False
b3 = False
cg = True


p1 = float(input("Introduce el primer porcentaje: "))
p11 = p1 / 100
if p1 > 100 :
    print("Tu porcentaje no puede superar el 100%")
elif p1 < 1 :
    print("Tu porcentaje tiene que ser mayor a 1")
else :
    a1 = True


p2 = float(input("Introduce el segundo porcentaje: "))
p12 = p2 / 100
if p2 > 100.00 :
    print("Tu porcentaje no puede superar el 100%")
elif p2 < 1 :
    print("Tu porcentaje tiene que ser mayor a 1")
else :
    a2 = True


p3 = float(input("Introduce el tercer porcentaje: "))
p13 = p3 / 100
if p3 > 100 :
    print("Tu porcentaje no puede superar el 100%")
elif p3 < 1 :
    print("Tu porcentaje tiene que ser mayor a 1")
else :
    a3 = True

if p1 + p2 + p3 != 100 :
    print("La suma de los porcentajes necesita de dar 100%")
    cg = False




Nota1 = float(input("Primera nota: "))
if Nota1 > 10.00 :
    print("Tu nota no puede ser mayor a 10")
elif Nota1 < 0 :
    print("Tu nota tiene que ser mayor a 0")
else :
    b1 = True
    
Nota2 = float(input("Segunda nota: "))
if Nota2 > 10.00 :
    print("Tu nota no puede ser mayor a 10")
elif Nota1 < 0 :
    print("Tu nota tiene que ser mayor a 0")
else :
    b2 = True    

Nota3 = float(input("Tercera nota: "))
if Nota3 > 10.00 :
    print("Tu nota no puede ser mayor a 10")
elif Nota1 < 0 :
    print("Tu nota tiene que ser mayor a 0")
else :
    b3 = True
    
Nota_Final = Nota1 * p11 + Nota2 * p12 + Nota3 * p13

if a1 and a2 and a3 and b1 and b2 and b3 == True :
    print(Nota_Final)
else :
    print("Porfavor vuelve a hacer la introduccion de las notas y porcentajes, porque uno de los valores esta fuera del rango permitido")