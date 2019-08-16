#-*- coding: utf-8 -*-

for i in range(2, 101, 2):
    print(i)

print("")

for i in range(1, 101, 1):
    if i % 2 == 0:
        print(i)
    else:
        continue