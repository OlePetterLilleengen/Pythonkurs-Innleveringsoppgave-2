# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# Programmet beregner hvor mange pizzaer som må kjøpes inn for at hver enkelt skal få minimum fire pizzastykker

import math

antall_elever = int(input('Skriv inn antall elever: ' ))

antall_pizzaer = antall_elever / 4

antall_pizzaer = math.ceil(antall_pizzaer)

# math.ceil er en funksjon som runder opp til heltall

print()
print('Antall pizzaer som må kjøpes inn er',antall_pizzaer)

