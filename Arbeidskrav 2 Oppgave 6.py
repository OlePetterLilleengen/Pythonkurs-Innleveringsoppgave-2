# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:27 2024

@author: OlePetterLilleengen
"""
# Programmet tegner en graf ut i fra gitte x og y verdier

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2 - 5

plt.figure(figsize=(9, 7))
plt.plot(x, y, label="y = -x^2 - 5$", color="red")
plt.title("Oppgave 6 = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("y)")
plt.axhline(0, color="black", linewidth=1.0, linestyle="--")
plt.axvline(0, color="black", linewidth=1.0, linestyle="--")
plt.grid(True)
plt.legend()
plt.show()
