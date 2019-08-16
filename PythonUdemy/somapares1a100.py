#-*- coding: utf-8 -*-
soma=0
for i in range(1, 101, 1):
    if i % 2 == 0:
        soma = soma + i
    else:
        continue
print(soma)    
