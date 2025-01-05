# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# Programmet beregner omkrets og areal av en figur bestående av en trekant og en halvsirkel
# Brukeren legger inn radius på halvsirkelen og lengden på en trkant som har to like sider

import math

a = float(input("Oppgi radiusen på sirkelen a: "))
b = float(input("Oppgi lengden på trekanten b: "))

arealhalvsirkel = (math.pi * a**2)/2
omkretshalvsirkel = (math.pi * a + 2 * a)

arealtrekant = (b * b) / 2
omkretstrekant = b + b

arealfigur = arealhalvsirkel + arealtrekant
omkretsfigur = omkretshalvsirkel + omkretstrekant
print()
print(f"Areal trekant {arealtrekant:.2f}")
print(f"Omkrets trekant {omkretstrekant:.2f}")
print(f"Areal halvsirkel {arealhalvsirkel:.2f}")
print(f"Omkrets halvsirkel {omkretshalvsirkel:.2f}")
print()
print(f"Arealet av figuren er: {arealfigur:.2f}")
print(f"Omkrets av figuren er: {omkretsfigur:.2f}")