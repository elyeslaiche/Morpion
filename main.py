import tkinter as tk
#Variables utiles a plusieurs fonctions
GameOver = ""
fenetre = ""
interface = ""
compteur = 0
#Permet de faire la vérification pour ne pas superposer deux formes
L1 =["","",""]
L2 =["","",""]
L3 =["","",""]
C1 =["","",""]
C2 =["","",""]
C3 =["","",""]
#Permet de connaître le vainqueur de la partie avec un count sur les variables ci-dessus.
L1R=0
L2R=0
L3R=0
C1R=0
C2R=0
C3R=0
L1C=0
L2C=0
L3C=0
C1C=0
C2C=0
C3C=0

#Fonction permettant de centrer les formes et de connaitre la position X
def positionX(X):
    if(X < 200):
        X = 100
    elif(X>200 and X<400):
        X=300
    else:
        X=500
    return X

#Fonction permettant de centrer les formes et de connaitre la position Y
def positionY(Y):
    if (Y < 200):
        Y = 100
    elif ((Y > 200) and (Y < 400)):
        Y = 300
    else:
        Y = 500
    return Y

#Vérfie la non-superposition de deux formes
def verif_case(X,Y, value):
    global L1, L2, L3, C1, C2, C3
    if (X < 200):
        if (Y < 200):
            if(L1[0]=="" ):
                L1[0] = value
                C1[0] = value
                return 0
        elif ((Y > 200) and (Y < 400)):
            if (L2[0] == "" ):
                L2[0] = value
                C1[1] = value
                return 0
        else:
            if (L3[0] == ""):
                L3[0] = value
                C1[2] = value
                return 0
    elif (X > 200 and X < 400):
        if (Y < 200):
            if(L1[1]=="" ):
                L1[1] = value
                C2[0] = value
                return 0
        elif ((Y > 200) and (Y < 400)):
            if (L2[1] == ""):
                L2[1] = value
                C2[1] = value
                return 0
        else:
            if (L3[1] == ""):
                L3[1] = value
                C2[2] = value
                return 0
    else:
        if (Y < 200):
            if (L1[2] == ""):
                L1[2] = value
                C3[0] = value
                return 0
        elif ((Y > 200) and (Y < 400)):
            if (L2[2] == ""):
                L2[2] = value
                C3[1] = value
                return 0
        else:
            if (L3[2] == ""):
                L3[2] = value
                C3[2] = value
                return 0
    return 1

#Permet de connaitre le vainqueur de la partie
def verif_win():
    global L1, L2, L3, C1, C2, C3, L1R, L2R, L3R, C1R, C2R, C3R, L1C, L2C, L3C, C1C, C2C, C3C
    L1R = L1.count(2)
    L2R = L2.count(2)
    L3R = L3.count(2)
    C1R = C1.count(2)
    C2R = C2.count(2)
    C3R = C3.count(2)
    L1C = L1.count(1)
    L2C = L2.count(1)
    L3C = L3.count(1)
    C1C = C1.count(1)
    C2C = C2.count(1)
    C3C = C3.count(1)

    if (L1R == 3 or L2R ==3 or L3R == 3 or C1R == 3 or C2R ==3 or C3R ==3):
        partie_terminee_winner(2)
    elif (L1C == 3 or L2C ==3 or L3C == 3 or C1C == 3 or C2C ==3 or C3C ==3):
        partie_terminee_winner(1)
    elif((L1[0] == 1 and L2[1] == 1 and L3[2] == 1)or(L1[2] == 1 and L2[1] == 1 and L3[0] == 1)):
        partie_terminee_winner(1)
    elif ((L1[0] == 2 and L2[1] == 2 and L3[2] == 2) or (L1[2] == 2 and L2[1] == 2 and L3[0] == 2)):
        partie_terminee_winner(1)

#Gère l'événement "clic" de la souris
def clic(event):
    # On récupère la position du pointeur de la souris
    global compteur
    X = event.x
    Y = event.y
    X = positionX(X)
    Y = positionY(Y)

    if compteur % 2 != 0:
        a = 2
        okay = verif_case(X, Y,a)
        if okay == 0:
            interface.create_oval(X - 75, Y - 75, X + 75, Y + 75)
            verif_win()
            compteur += 1

    else:
        a = 1
        okay = verif_case(X, Y,a)
        if okay == 0:
            interface.create_line(X - 75, Y - 75, X + 75, Y + 75)
            interface.create_line(X + 75, Y - 75, X - 75, Y + 75)
            verif_win()
            compteur += 1

    if compteur == 9:
        partie_terminee()
        compteur = 0

def partie_terminee():
    Menu()
    interface.unbind("<Button-1>")

def partie_terminee_winner(a):
    Menu_Win(a)
    interface.unbind("<Button-1>")

def Menu():
    global GameOver
    GameOver = tk.Tk()
    interface2 = tk.Canvas(GameOver, width = 200, height = 150, bg = "white")
    interface2.pack(padx=5, pady=5)
    interface2.create_text(100,20,fill="black",text="Game Over")
    B = tk.Button(GameOver, text="Quitter", command=Quitter)
    A = tk.Button(GameOver, text="Rejouer", command=Rejouer)
    A.pack()
    B.pack()

def Menu_Win(a):
    global GameOver
    GameOver = tk.Tk()
    interface2 = tk.Canvas(GameOver, width=200, height=150, bg="white")
    interface2.pack(padx=5, pady=5)
    interface2.create_text(100, 20, fill="black", text="Player "+ str(a) + " wins")
    B = tk.Button(GameOver, text="Quitter", command=Quitter)
    A = tk.Button(GameOver, text="Rejouer", command=Rejouer)
    A.pack()
    B.pack()

def Rejouer():
    fenetre.destroy()
    GameOver.destroy()
    init()
def Rejouer_principal():
    fenetre.destroy()
    init()
def Quitter():
    global GameOver
    fenetre.destroy()
    GameOver.destroy()
def Quitter_principal():
    global GameOver
    fenetre.destroy()


def init() :
    global fenetre
    global interface
    global compteur
    global L1, L2, L3, C1, C2, C3, L1R, L2R, L3R, C1R, C2R, C3R, L1C, L2C,L3C,C1C,C2C,C3C
    L1 = ["", "", ""]
    L2 = ["", "", ""]
    L3 = ["", "", ""]
    C1 = ["", "", ""]
    C2 = ["", "", ""]
    C3 = ["", "", ""]

    L1R = ["", "", ""]
    L2R = ["", "", ""]
    L3R = ["", "", ""]
    C1R = ["", "", ""]
    C2R = ["", "", ""]
    C3R = ["", "", ""]
    L1C = ["", "", ""]
    L2C = ["", "", ""]
    L3C = ["", "", ""]
    C1C = ["", "", ""]
    C2C = ["", "", ""]
    C3C = ["", "", ""]
    compteur = 0
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    #notre interface
    interface = tk.Canvas(fenetre, width = 600, height =600, bg ="white")
    interface.pack(padx =5, pady =5)
    #création des lignes du jeu
    interface.create_line(200,0,200,600,fill="black",width=4)
    interface.create_line(400,0,400,600,fill="black",width=4)
    interface.create_line(0,200,600,200,fill="black",width=4)
    interface.create_line(0,400,600,400,fill="black",width=4)
    interface.bind("<Button-1>", clic)
    B = tk.Button(GameOver, text="Quitter", command=Quitter_principal)
    A = tk.Button(GameOver, text="Rejouer", command=Rejouer_principal)
    A.pack()
    B.pack()

init()
fenetre.mainloop()
