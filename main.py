# PUISSANCE 4

# liste_puissance_4 correspond aux lignes du puissance 4 sous forme de liste.


def grille_init():
    liste_puissance_4 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    return liste_puissance_4


# La fonction affiche_grille renvoie les valeurs de la liste_puissance_4 sous forme de grille de puissance 4.


def affiche_grille(tab):
    # On crée la ligne intermédiaire qui sépare chaque ligne de la grille
    ligne_intermediaire = "+---+---+---+---+---+---+---+"

    # On affiche la ligne intermédiaire
    print(ligne_intermediaire)

    # On parcourt les éléments de la liste tab
    for i in range(len(tab)):

        # On parcourt les éléments de chaque liste de la liste tab
        for j in range(len(tab[i])):
            print("|", tab[i][j], end=" ")

        # On affiche une autre ligne intermédiaire à la fin de chaque ligne de la grille
        for k in range(1):
            print("|")

        # On affiche une nouvelle ligne intermédiaire pour séparer les lignes de la grille
        print(ligne_intermediaire)


# La fonction colonne_libre vérifie si la case de la ligne la plus haute du tableau est égale à 1 ou 2 en fonction de
# la colonne choisie.

# Si c'est le cas, on considère que la colonne est pleine.


def colonne_libre(tab, colonne):
    # Vérifie si la colonne demandée est valide
    if len(tab[0]) - 1 < colonne:
        return False

    # Vérifie si la colonne est libre en regardant la valeur dans la première ligne
    if tab[0][colonne] == 1 or tab[0][colonne] == 2:
        libre = False
    else:
        libre = True

    return libre


# La fonction place_jeton vérifie en premier temps si la colonne est libre avec la fonction colonne_libre.

# Si colonne_libre renvoie "True", alors on regarde si la case la plus basse est égale à 1 ou 2. Tant que c'est le
# cas, on monte d'une case.

# Lorsqu'on arrive à une case égale a 0, on remplace cette valeur par celle de "joueur" dans la liste "tab".

# On renvoie alors la fonction affiche_grille avec la valeur modifiée.


def place_jeton(tab, colonne, joueur):
    # Vérifie si la colonne est libre
    if colonne_libre(tab, colonne):

        # Cherche la première ligne vide dans la colonne
        ligne = -1
        while tab[ligne][colonne] == 1 or tab[ligne][colonne] == 2:
            ligne += -1

        # Place le jeton du joueur dans la ligne trouvée
        tab[ligne][colonne] = joueur
        affiche_grille(tab)
        return True

    # Si la colonne n'est pas libre, affiche un message d'erreur
    else:
        if len(tab[0]) - 1 < colonne:
            print("Cette colonne n'existe pas ! Merci de renseigner un chiffre entre 1 et 7.")
        else:
            print("Cette colonne est pleine.")
        return False



# La fonction horizontale vérifie pour chaque ligne si 4 mêmes chiffres de la valeur "joueur" se suivent.

# Si cette condition est validée, alors "victoire_horizontale" est assignée à "True"


def horizontale(tab, joueur):
    # déclare une variable pour enregistrer si le joueur a gagné
    victoire = False

    # parcours toutes les lignes du tableau
    for i in range(len(tab)):
        # parcours les colonnes de la ligne en cours
        for j in range(4):
            # vérifie si les quatre éléments suivants sont égaux au joueur en cours
            if tab[i][j] == joueur and tab[i][j + 1] == joueur and tab[i][j + 2] == joueur and tab[i][j + 3] == joueur:
                # si c'est le cas, met à jour la variable pour dire que le joueur a gagné
                victoire = True

    # retourne l'état de victoire du joueur
    return victoire



# Même principe que pour la fonction horizontale, sauf que cette fois on vérifie pour chaque colonne.

# Si cette condition est validée, alors "victoire_verticale" est assignée à "True"


def verticale(tab, joueur):
    # déclare une variable pour enregistrer si le joueur a gagné
    victoire = False

    # parcours les colonnes du tableau
    for i in range(3):
        # parcours les lignes de la colonne en cours
        for j in range(6):
            # vérifie si les quatre éléments suivants sont égaux au joueur en cours
            if tab[i][j] == joueur and tab[i + 1][j] == joueur and tab[i + 2][j] == joueur and tab[i + 3][j] == joueur:
                # si c'est le cas, met à jour la variable pour dire que le joueur a gagné
                victoire = True

    # retourne l'état de victoire du joueur
    return victoire



# Diagonale

def diagonale(tab, joueur):
    # parcours les lignes du tableau (à partir de la troisième ligne)
    for i in range(len(tab)-3):
        # parcours les colonnes de la ligne en cours (à partir de la quatrième colonne)
        for j in range(3, len(tab[i])):
            # vérifie si les quatre éléments suivants (en diagonale vers le haut à gauche) sont égaux au joueur en cours
            if tab[i][j]==joueur and tab[i+1][j-1]==joueur and tab[i+2][j-2]==joueur and tab[i+3][j-3]==joueur:
                # si c'est le cas, retourne True pour dire que le joueur a gagné
                return True

    # parcours les lignes du tableau (à partir de la troisième ligne)
    for i in range(len(tab)-3):
        # parcours les colonnes de la ligne en cours (à partir de la première colonne)
        for j in range(len(tab[i])-3):
            # vérifie si les quatre éléments suivants (en diagonale vers le haut à droite) sont égaux au joueur en cours
            if tab[i][j]==joueur and tab[i+1][j+1]==joueur and tab[i+2][j+2]==joueur and tab[i+3][j+3]==joueur:
                # si c'est le cas, retour
                return True
    return False


# fonction qui à chaque tour vérifie si le joueur qui vient de jouer à gagner.


def gagne(tab, joueur):
    # Vérifie si le joueur a gagné (soit horizontalement, soit verticalement ou via les diagonales)
    if diagonale(tab, joueur) or horizontale(tab, joueur) or verticale(tab, joueur):
        print("Le joueur " + str(joueur) + " vient de gagner la partie !")

        return True


# fonction qui à chaque tour permet de récupérer la colonne choisie par le joueur et d'actionner la fonction place_jeton

# qui s'occupe du reste;


def tour_joueur(tab, joueur):
    # Demande à l'utilisateur de choisir une colonne où jouer
    colonne = input("Choisissez la colonne dans laquelle vous voulez jouer joueur numéro " + str(joueur) + " : [1] [2] [3] [4] [5] [6] [7]")

    # Convertit l'entrée de l'utilisateur en un entier, en soustrayant 1 pour tenir compte de l'indexage des colonnes à partir de 0
    colonne = int(colonne) - 1

    # Appelle la fonction "place_jeton" pour placer le jeton du joueur dans la colonne choisie
    if not place_jeton(tab, colonne, joueur):
        return False
    else:
        return True




# fonction qui permet à chaque tour de vérifier si il y a égalité, et si oui terminé la partie.


def egalite(tab):
    # La colonne initiale est définie à 0
    colonne = 0

    # Vérifie si les sept colonnes du tableau ne sont pas libres (c'est-à-dire si elles sont toutes pleines)
    for i in range(7):
        if not colonne_libre(tab, colonne+i):
            print("La partie est terminée, il y a égalité")

            # Si toutes les colonnes sont pleines, retourne True pour indiquer qu'il y a égalité
            return True
    return False



def jouer(tab, joueur):
    #initialise le statut de la partie, true signifiant que la partie est terminée.
    statut = False

    while not statut:
        # Demander au joueur actuel de faire un tour
        if tour_joueur(tab, joueur):
            # Vérifier si le joueur actuel a gagné
            if gagne(tab, joueur):
                # Mettre statut à vrai pour sortir de la boucle
                statut = True

            # Vérifier si c'est une égalité
            if egalite(tab):
                # Mettre statut à vrai pour sortir de la boucle
                statut = True

            # Changer de joueur
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

    # Quand on sort de la boucle, le jeu est fini.

#fonction qui lance la partie
def start():
    #initilisation du premier jouer.
    joueur = 1
    #lancement partie
    jouer(grille_init(), joueur)


start()

#A VOIR:
# J'ai refais les égalités (de manière bien plus propre) à tester si ça fonctionne bien comme il faut.