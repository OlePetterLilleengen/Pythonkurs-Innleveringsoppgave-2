# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# Programmet lar brukeren taste inn nye land, hovedsteder og innbyggertall hovedsteder
# Brukeren kan fortsette å legge til nye land inntil han ikke ønsker å fortsette
# Programmet skriver ut alle land med tilsvarende hovedstad og innbyggertall i hovedstedende

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
}   
    
while True:
    land = input("Skriv inn det nye landet: ")
    hovedstad = input("skriv inn ny hovesstad: ")
    innbyggertall = (input("Skriv inn innbyggertallet: "))
    innbyggertall = float(innbyggertall)
    data[land] = [hovedstad, innbyggertall]

    fortsette = input("Vil du legge til flere land ? (ja/nei): ")
    if fortsette != "ja":
        break


for land, info in data.items():
    hovedstad, innbyggertall = info
    print()
    print(f"I {land} er hovedstaden {hovedstad} og innbyggertallet er {innbyggertall:.3f} millioner.")