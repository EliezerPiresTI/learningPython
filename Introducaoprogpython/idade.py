#coding: utf-8

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade.")
elif idade > 0 and idade < 18:
    print("Menor de idade")
else:
    print("Idade invalida")