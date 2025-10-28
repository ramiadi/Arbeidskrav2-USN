# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:30:11 2025

@author: ramin
"""
import math
import numpy as np

# Oppgave 1
alder = int(input("Hvilket år er du født? "))
print ("Du er " + str(2024 - alder) + " år gammel")

# Oppgave 2
antall_elever = int(input("Skriv inn antall elever: "))
# Ved å bruke math.ceil, runder vi opp tallet.
antall_pizzaer = math.ceil(antall_elever * 0.25)
# Bruk int slik at tallet ikke blir en desimaltall, men en heltall.
print("Det må handles inn ", int(antall_pizzaer), "pizzaer")

# Oppgave 3

# Legg til en funksjon som skal ha en parameter
def grader_til_radianer(v_grad):
    #Ta med verdien fra parameter til hit
    v_rad = v_grad * np.pi / 180
    # Returner verdien fra regningen
    return v_rad

v_grad = float(input("Skriv inn gradtallet: "))
# Vi har laget en funksjon, og vi tar inn v_grad som parameter 
v_rad = grader_til_radianer(v_grad)
print(str(v_grad) + " grader er " + str(v_rad) + " radianer.")

# Oppgave 4
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
    }

land = str(input("Skriv inn et land "))
land_value = data[land]
print(f"{land_value[0]} er hovedstaden i {land} og det er {land_value[1]} mill. innbyggere i {land_value[0]}.")
