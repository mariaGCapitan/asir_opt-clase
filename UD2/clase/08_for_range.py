#!/usr/bin/env python3
"""
Bucle for con range()
"""

for n in range(5): #(0,1,2,3,4)
    print(n)

print()
print()

#Puedo hacer un acumulador dentro de un for
total = 0
for n in range(1,11):
    total+= n
    print(f"La iteración es {n}")
    print(f"Por ahora TOTAL vale {total}")

print(f"Al final TOTAL vale {total}")

