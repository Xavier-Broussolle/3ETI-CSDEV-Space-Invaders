### ------------------------------------------------- ###
### SPACE INVADERS ###
### BROUILLON XB ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024

### - Librairies - ###
import tkinter as tk

### - Images - ###
photoVaisseau = tk.PhotoImage(file="./images/vaisseau.png")


### - Gestion des classes - ###
# creation objet bloc aliens 
class blocAlien :
    def __init__(self, position, vitesse):
        self.position = position
        self.vitesse = vitesse 

# creation objet alien 
class alien : 
    def __init__(self, position) : 
        self.position = position 

# creation protection 
class protection :
    def __init__(self, position):
        self.position = position

# creation objet vaisseau 
class vaisseau :
    def __init__(self, position, vies):
        self.position = position
        self.vies = vies 

# creation objet projectile 
class projectile : 
    def __init__(self, position):
        self.position = position 