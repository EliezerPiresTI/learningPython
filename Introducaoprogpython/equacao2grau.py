#coding: utf-8
from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = float((b**2) - 4*a*c)

if delta > 0:
    raiz1 = float((b*(-1) + math.sqrt(delta))/2*a)
    raiz2 = float((b*(-1) - math.sqrt(delta))/2*a)
    print(raiz1)
    print(raiz2)
elif delta == 0:
    raiz3 = float((b*(-1) + math.sqrt(delta))/2*a)
    
    print(raiz3)
elif delta < 0:
    print("Não existe raiz real")