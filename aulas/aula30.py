"""
Desafio do contador.

0 10
1 9
2 8
3 7
4 6
5 5
5 4
6 3
8 2
"""

contador0_10 = 0
contador10_2 = 10

"""
print(contador0_10)
while contador0_10 < 8:
    contador0_10 += 1
    print(contador0_10)

print(" ")

print(contador10_2)
while contador10_2 > 2:
    contador10_2 -= 1
    print(contador10_2)
"""

"""
for contador10_2 in range(10, 1, -1):
    print(contador10_2)

print("          ")

for contador0_10 in range(0, 9):
    print(contador0_10)
"""

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
