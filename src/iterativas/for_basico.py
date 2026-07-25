# for_basico.py - bucle for, range() y enumerate()
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

for i in range(3, 8):
    print(i, end=" ")
print()

nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posicion {indice}: {nombre}")