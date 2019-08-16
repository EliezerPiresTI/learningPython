#-*- coding: utf-8 -*-

#for i in range(1, 101):
#    if i == 1:
#        continue
#    elif i == 2 or i == 3:
#        print(i)
#    else:
#        if i % 2 != 0:
#           divisor = 3
#           while(divisor < i):
#                if (i % divisor == 0):
#                   break               
#                    print(i)
#                    break
#                divisor += 2

for numero_pra_saber_primo in range(1, 101):
    contando_divisores = 0
    for divisor in range(1, numero_pra_saber_primo):
        if (numero_pra_saber_primo % divisor == 0):
            contando_divisores += 1
    if contando_divisores <= 2:
        print(numero_pra_saber_primo)