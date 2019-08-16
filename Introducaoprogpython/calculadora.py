#coding: utf-8


valor1 = float(input("Digite o primeiro número: "))
operador = str(input("Digite a operação matemática: (+-*/) "))
valor2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = sum(valor1, valor2)
    print(resultado)
elif operador == "-":
    resultado = valor1 - valor2
    print(resultado)
elif operador == "*":
    resultado = valor1 * valor2
    print(resultado)
elif operador == "/":
    resultado = valor1 / valor2
    print(resultado)