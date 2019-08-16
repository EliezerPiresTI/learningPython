# -*-coding: utf-8 -*-

#Exercício 1
# Escreva um algoritmo que contenha uma função de nome estudo() e que quando executada imprima na saída padrão a frase
# "Estamos estudando as funções":

def estudo():
    print("Estamos estudando funções.")

estudo()
    
    
#Exercício 2
# Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber um número como argumento. 
# Chame este argumento de x. No corpo da função imprima a seguinte frase na tela: "Função invocada com sucesso. 
# O valor passado pelo argumento x é: <valor de x>"

def estudo(x):
    print("Função invocada com sucesso. O valor passado pelo argumento x é: {}".format(x))

estudo(10)


#Exercício 3
# Escreva um algoritmo que receba dois números através da declaração de dois parâmetros cujos nomes serão: x e y.
# No bloco de instrução faça a soma de ambos valores e imprima o resultado no monitor:

def soma(x, y):
    print(x+y)

soma(5, 15)


#Exercício 4
# Escreva um algoritmo contendo uma função que necessite de três argumentos.
# Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:

import math
def cresc_media(lista):
    lista.sort()
    print(lista)
    media = sum(lista)/len(lista)
    print(media)

x = [6.5, 7.0, 8.3, 4.5]
cresc_media(x)


#Exercício 5
# Escreva uma função que contenha dois parâmetros. O primeiro deve ser obrigatório e o segundo facultativo:

def multiplica(x, y=2):
    print(x*y)
    
multiplica(3)


#Exercício 6
# Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos.
# Invoque a primeira função de ``func1()`` e a segunda de ``func2()``. Em seguida, invoque os parâmetros
# da segunda função de x e y. Some x e y e retorne o resultado. Em func1(), ao receber o resultado, retorne-o
# também como valor de retorno da função. Por fim, imprima na tela o valor que foi calculado por func2(), retornado
# para func1() e retornado a quem invocou a função inicialmente:

def func1():
    return func2(2, 3)

def func2(x, y):
    return x+y

z = func1()
print(z)


#Exercício 7
# Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros.
# Em seguida, imprima os parâmetros recebidos na tela:

def elem_list(*args):
    lista = list(args)
    print(lista)
    
elem_list(2, 3, 5, 7, 2, 4, 9)


#Exercício 8
#Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave.
# Em seguida, imprima na tela o nome da chave e o respectivo valor:

def elem_dic(**args):
    print(args)

elem_dic(Nome="Eliezer", Sobrenome="Pires", ano_nasc=1991)

#Exerício 9
#Considere o trecho de código a seguir.
def func(a, b, c, d):
    print(a+b+c+d)
lista = 1,2,3,4
# Invoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem,
# de forma a utilizar o conceito de desempacotamento:

def func(a, b, c, d):
    print(a+b+c+d)

lista = 1,2,3,4
func(*lista)    


#Exercício 10
 #Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.
 
x = 10
y = 2
z = 5
t = 32
print(max(x,y,z,t))

#Exercício 13
# Escreva uma função que inverta a ordem dos elementos de uma lista manualmente.
# Não utilize a função interna do Python que faz inverção, crie o algoritmo que faça a inversão.
# Lista: "1234abcd"
# Saída: "dcba4321"

def inverter_lista(lista):
    tam = len(lista)
    cresc = list(range(tam))
    decres = list(range(-1, (tam+1)*(-1),-1))
    for i in range(int(tam/2)):
        lista[cresc[i]], lista[decres[i]] = lista[decres[i]], lista[cresc[i]]      
    return lista

teste = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
resultado = inverter_lista(teste)
print(resultado)

#Exercício 14
#Escreva uma função que calcule o fatorial de um número (um inteiro não negativo).
# Envie o valor do número que será calcula como argumento da função.
def fatorial_numero(numero):
    fat = numero
    for i in range(1,numero,1):
        fat = fat * (numero - i)
    return fat

numero = int(input("Digite um número inteiro não negativo, para calcular o fatorial: "))
fatorial = fatorial_numero(numero)
print(fatorial)

#Exercício 15
#Escreva uma função que verifique se um número está num intervalo determinado.
def esta_no_intervalo_entre_xey(num, x, y ):
    if num >= x and num <= y:
        return True
    return False

if esta_no_intervalo_entre_xey(4, 1, 22):
    print("4 está no intervalo")
else:
    print("4 não está no intervalo")

#Exercício 16
#Escreva uma função que aceite Strings e calcule a quantidade de letras em mauisculas e
# minúsculas que a String possui.

def qtmaius_qtminus(lista):
    def convert_ascii(string):
        i=0
        for letra in string:
            string[i] = ord(letra)
            i+=1
        return string
    
    #chamando a função para converter todas as letras em inteiro (tabela ASCII)
    lista = convert_ascii(lista)
    #contando letras maiusculas na string e minusculas
    count_minusc = 0
    count_maiusc = 0
    for letra in lista:
        if letra >= 65 and letra <=91:
            count_maiusc += 1
        elif letra >= 97 and letra <= 122:
            count_minusc += 1
    print("A quantidade de letras Maiusculas são {} e a quantidade de letra Minusculas são {}".format(count_maiusc, count_minusc))      

# frase = list(input("Digite uma frase: "))
# qtmaius_qtminus(frase)

#Exercício 17
# Escreva uma função que receba como argumento uma lista que poderá ter valores duplicados e
# retorne uma nova lista sem que haja valores iguais.
#Lista: [1,2,3,3,3,3,4,5]
#Retorno: [1, 2, 3, 4, 5]
def unique(a):
    return list(set(a))
lista = [1,2,3,3,3,3,4,4,5,6,7,5,8,2,1,1]
unique(lista)

#Exercício 18
# Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e
# imprima na telas os números primos contidos nessa lista.

def imprimirPrimosdeLista(*lista):
    def contarDivisores(x):
        contando_divisores = 0
        for divisor in range(1, x+1):
            if(x % divisor == 0): contando_divisores += 1
        return contando_divisores
    lista = list(lista)
    #compreensão de lista   sintaxe da compreensão de lista
    #[expressão for variáveis in iterável if condição]
    primosdaLista = [numeroPraSaberSeePrimo for numeroPraSaberSeePrimo in lista if contarDivisores(numeroPraSaberSeePrimo) <= 2]
    #variáveis -> numeroPraSaberSeePrimo
    #iterável -> lista
    #primosdaLista = []
    #for numeroPraSaberSeePrimo in lista:
    #     #condição
    #     if contarDivisores(numeroPraSaberSeePrimo)<=2:
    #         #expressão
    #         primosdeLista.append(numeroPraSaberSeePrimo)
    #print primosdeLista        
    return print(primosdaLista)

#Exercício 19
#Escreva uma função que imprima somente os números pares
#Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Saída: [2, 4, 6, 8]    
imprimirPrimosdeLista(2,3,4,6,7,5,13,12,11,15,17,21)
def imprimirParesdeLista(lista):
    lista = list(lista)
    pares_lista = [elemento for elemento in lista if not elemento % 2]
    return pares_lista
numeros = [1,2,3,4,5,6,7,8,9]
print(imprimirParesdeLista(numeros))

#Exercícios 20
#Escreva uma função que verifica se uma String enviada é um 
#palíndromo ou não.
#TENTATIVA SEM SUCESSO
# def identificarPalindromos(string):
#     string = list(string)
#     cresc = list(range(len(string)))
#     print(cresc)
#     decresc = list(range(-1,((len(string))+1)*(-1),-1))
#     print(decresc)
#     verificacao = [([string[cresc[i]] == string[decresc[i]]]) for i in range(int(len(string)/2))]
#     print(verificacao)
#     if all(([string[cresc[i]] == string[decresc[i]]]) for i in range(int(len(string)/2))):
#         print("É um Palíndromo.")
#     else:
#         print("Não é um Palíndromo.")

# identificarPalindromos('a')
#AJUDA CURSO EM VÍDEO EXERCÍCIO PYTHON 53 - DETECTOR DE PALÍNDROMO
def identificarPalindromo(frase):
    frase = ''.join(frase.strip().upper().split())
    inverso = frase[::-1]
    print("É um Palíndromo") if inverso == frase else print("Não é um Palíndromo")
    #inverso = ''.join([frase[letra] for letra in range(len(frase)-1,-1,-1)])
    #EQUIVALENTE
    #for letra in range(len(frase)-1,-1,-1):
    #     inverso += frase[letra]

identificarPalindromo("eliezer e um excelente programado")


