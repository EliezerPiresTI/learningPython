#coding: utf-8

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print("Sua média é %f" %(media))
if media >= 6.0:
    print("Aprovado")
else:
    print("Reprovado")