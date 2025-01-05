# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# programmet regner fra grader til radianer

import numpy as np

v_grad = float(input('Skriv inn gradtallet: ' ))
v_rad = float(v_grad*np.pi/180)

print()
print(f"{v_grad:.1f}", 'grader er',f"{v_rad:.3f} radianer")
# skriver ut grader med en desimal og radianer med 3 desimaleler