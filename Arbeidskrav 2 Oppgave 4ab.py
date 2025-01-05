# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# Programmet lar brukeren taste inn et land og skriver ut tilsvarende hovedstad og innbyggertallet i hovedstaden

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
}   
    
land = input("Skriv inn et land: ")

hovedstad, innbyggere = data[land]

print()
print(hovedstad,"er hovedstaden i",land,"og det er",innbyggere,"mill. innbyggere i",hovedstad)