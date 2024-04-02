from random import randint
import copy

def grille_vide():
    """Renvoie une grille de six ligne et sept colonnes remplie de 0"""
    liste_vide = []
    for _ in range(6):
        liste_vide.append([0 for j in range(7)])
    return liste_vide


def affiche(g):
    """Prend en argument une grille g et l’affiche avec le caractère "." pour une case vide, le
caractère "X" pour le joueur 1 et le caractère "O" pour le joueur 2"""
    grille_affiche = copy.deepcopy(g)
    for i in range(len(grille_affiche)):
        for j in range(len(grille_affiche[i])):
            if grille_affiche[i][j] == 0:
                grille_affiche[i][j] = "."
            elif grille_affiche[i][j] == 1:
                grille_affiche[i][j] ="X"
            elif grille_affiche[i][j] == 2:
                grille_affiche[i][j] = "0"
    for i in range(len(grille_affiche)):
        print(grille_affiche[i])
    return g
    

def coup_possible(g, c):
    """Prend en argument une grille g et indique si il est posible de jouer dans la colonne d'indice c."""
    checkliste = []
    for i in range(len(g)):
        checkliste.append(g[i][c])
    if 0 in checkliste:
        return True
    else:
        return False
    
def jouer(g, j, c):
    """Prend en arguments une grille g, un joueur j et un indice de colonne c et modifie
    la grille où le joueur j a joué dans la colonne c en supposant qu’il est possible de jouer dans la colonne c."""
    for i in range(len(g)-1, -1, -1):
        if g[i][c]== 0 :
            g[i][c] = j
            break
    return g

def horiz(g, j, l, c):
    """Prend en arguments une grille g, un joueur j, une ligne l et un indice de colonne
c et renvoie un booléen indiquant si le joueur j a un alignement horizontal de 4 pions à partir de la case (l, c)."""
    assert l <= 5, "Erreur d'indice de ligne"
    assert c <= 6, "Erreur d'indice de colonne"
    if c <= 3:
        if g[l][c] == g[l][c+1] == g[l][c+2] == g[l][c+3] == j:
            return True
        else:
            return False
    else:
        return False

        
def vertic(g, j, l, c):
    """Prend en arguments une grille g, un joueur j, une ligne l et un indice de colonne c et renvoie un
    booléen indiquant si le joueur j a un alignement vertical de 4 pions à partir de la case (l, c)."""
    assert l <= 5, "Erreur d'indice de ligne"
    assert c <= 6, "Erreur d'indice de colonne"
    if l <= 2:
        if g[l][c] == g[l+1][c] == g[l+2][c] == g[l+3][c] == j:
            return True
        else:
            return False
    else:
        return False
        
def diag(g, j, l, c):
    """Prend en arguments une grille g, un joueur j, une ligne l et un indice de colonne c et renvoie un
    booléen indiquant si le joueur j a un alignement vertical de 4 pions à partir de la case (l, c)."""
    assert l <= 5, "Erreur d'indice de ligne"
    assert c <= 6, "Erreur d'indice de colonne"
    if l <= 2 and c <=3:
        if g[l][c] == g[l+1][c+1] == g[l+2][c+2] == g[l+3][c+3] == j:
            return True
        else:
            return False
    elif l >= 3 and c <= 3:
        if g[l][c] == g[l-1][c+1] == g[l-2][c+2] == g[l-3][c+3] == j:
            return True
        else:
            return False
    else:
        return False
    
    
def victoire(g,j):
    """Prend en arguments une grille g et un joueur j et renvoie un booléen indiquant si
    le joueur j a gagné dans la grille g."""
    for i in range(len(g)):
        for k in range(len(g[0])):
            if horiz(g, j, i, k) or vertic(g, j, i, k) or diag(g, j, i, k) == True:
                return True
    return False

def match_nul(g):
    """prend en argument une grille g et renvoie un booléen indiquant s’il y a math nul dans
    la grille g.
    """
    if 0 not in g[0]:
        return True
    else:
        return False
    
def coup_aleatoire(g, j):
    """Prend en arguments une grille g et un joueur j et modifie la grille où le
    joueur j a joué au hasard dans une colonne parmi celles qui ne sont pas pleines."""
    verif = 0
    while verif !=1:
        colonne = randint(0, 6)
        if coup_possible(g,colonne) == True:
            jouer(g, j, colonne)
            verif += 1
            
#Programme aléatoire
            
######grille = grille_vide()
##fin = False
##while fin != True:
##    coup_aleatoire(grille, 1)
##    if victoire(grille,1) == True:
##        break
##    affiche(grille)
##    print("")
##    coup_aleatoire(grille, 2)
##    if victoire(grille,2) or match_nul(grille) == True:
##        fin = True
##        break
##    affiche(grille)
##    print("")
#affiche(grille)

#Programme avec joueur
            
grille = grille_vide()
fin = False
while fin != True:
    choix = int(input("Choisissez une colonne de 1 à 7 : "))-1
    verif = False
    while verif != True:
        if coup_possible(grille, choix):
            jouer(grille, 1, choix)
            verif = True
    if victoire(grille,1) == True:
        break
    affiche(grille)
    print("")
    coup_aleatoire(grille, 2)
    if victoire(grille,2) or match_nul(grille) == True:
        fin = True
        break
    affiche(grille)
    print("")
affiche(grille)




    
