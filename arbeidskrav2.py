# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:30:11 2025

@author: ramin
"""
import math

# Oppgave 1
alder = int(input("Hvilket år er du født? "))
print ("Du er " + str(2024 - alder) + " år gammel")

# Oppgave 2
antall_elever = int(input("Skriv inn antall elever: "))
# Ved å bruke math.ceil, runder vi opp tallet.
antall_pizzaer = math.ceil(antall_elever * 0.25)
# Bruk int slik at tallet ikke blir en desimaltall.
print("Det må handles inn ", int(antall_pizzaer))