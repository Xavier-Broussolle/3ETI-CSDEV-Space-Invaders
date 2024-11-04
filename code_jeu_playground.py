### ------------------------------------------------- ###
### SPACE INVADERS ###
### BROUILLON XB ###
# UTF8
# Auteurs : ARRIEU Matteo, BROUSSOLLE Xavier 
# Date de creation du fichier : Lundi 4 Nov 2024
# Derniere mise a jour : Lundi 4 Nov 2024

### - Librairies - ###
import tkinter as tk

### - Gestion affichage global - ### 
class Toile : 
    def __init__(self):
        self.mf = tk.Tk()
        self.cnv = tk.Canvas(self.mf, width=1200, height=800, bg="white")
        self.cnv.pack()
        #self.btn_start = tk.Button(self.mf, text="Jouer")
        #self.btn_start.pack(padx=100, side='left')
        self.btn_quit = tk.Button(self.mf, text="Quitter", command=self.mf.quit)
        self.btn_quit.pack(padx=100, side='right')
        self.mf.mainloop()

toile1 = Toile()


### - Gestion des classes - ###
# creation objet bloc aliens 
class BlocAlien :
    def __init__(self, position, vitesse):
        self.position = position
        self.vitesse = vitesse 

# creation objet alien 
class Alien : 
    def __init__(self, position) : 
        self.position = position 

# creation protection 
class Protection :
    def __init__(self, position):
        self.position = position

# creation objet vaisseau 
# creation image vaisseau
photoVaisseau = tk.PhotoImage(file="./images/vaisseau.png")
class Vaisseau :
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.vies = 3 
        self.canva = tk.Canvas(toile1, width=160, height=187, bg='')
        self.imageVaisseau = tk.create_image(positionX, positionY, image=photoVaisseau)
        self.canva.coords(positionX, positionY, self.imageVaisseau)
        self.tk.focus_set()

    def deplacer(self):
        touche=tk.event.keysym

        if touche == "q" : 
            self.positionX -= 40
        if touche == "d" : 
            self.positionX += 40

Vaisseau(200, 200 )

# creation objet projectile 
class Projectile : 
    def __init__(self, position):
        self.position = position 