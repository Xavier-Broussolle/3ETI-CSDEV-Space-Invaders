### ------------------------------------------------- ###
### SPACE INVADERS ###
### BROUILLON XB ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024

### - Librairies - ###
import tkinter as tk
from Affichage import SI

### - Images - ###
photoVaisseau = tk.PhotoImage(file="./images/vaisseau.png")
image_label = tk.Label(SI, image=photoVaisseau)
image_label.pack()


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
    def __init__(self, positionX, positionY, vies):
        self.positionX = positionX
        self.positionY = positionY
        self.vies = vies 
        self.canva = tk.Canvas(SI, width=160, height=187, bg='')
        self.imageVaisseau = tk.create_image(0, 0, anchor="nw", file=photoVaisseau)
        self.canva.coords(positionX, positionY, self.imageVaisseau)
        self.tk.focus_set()

    def deplacer(self):
        touche=tk.event.keysym

        if touche == "q" : 
            self.positionX -= 40
        if touche == "d" : 
            self.positionX += 40

# creation objet projectile 
class projectile : 
    def __init__(self, position):
        self.position = position 