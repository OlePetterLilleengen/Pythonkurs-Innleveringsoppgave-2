# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""

# Programmet lar brukeren skrive inn alder og hvilket år det er og skriver ut alder

from datetime import datetime

alder = int(input('Hvilket år er du født: ') )
hvilketarna= datetime.now().year

alder = hvilketarna - alder

print("")
print('Du er',alder,'år')