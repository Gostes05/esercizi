import math

raggio = input("Inserisci il raggio: ")

raggio = int(raggio)

#calcola la superficie


super = 4 * math.pi * raggio ** 3

#calcola il volume

vol = 4 / 3 * math.pi * raggio ** 3

print(super)

print(vol)
