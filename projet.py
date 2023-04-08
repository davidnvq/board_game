import string
import sys

### DATA REPRESENTATION
# matrices to represent the grid
#1 for player 1 positions, 2 for player 2 positions
grille_vide = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
grille_depart = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2]]
grille_milieu = [[0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 1],
                 [0, 2, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 2, 1, 0],
                 [0, 0, 1, 0, 2, 0, 2, 0, 0], [0, 0, 2, 0, 0, 1, 0, 0, 0], [2, 0, 0, 0, 2, 2, 0, 2, 0]]
grille_fin = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 2, 0, 2, 0], [0, 2, 2, 0, 0, 1, 2, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]]

#### REPRESENTATION GRAPHIQUE


def afficher_carre(carre):
    # Si c'est le position de joueur 1, affichez '*'
    if carre == 1:
        return '•'
    # Si c'est le position de joueur 2, affichez '@'
    elif carre == 2:
        return '∘'
    # Si le carre n'est pas occupé, affichez une espace vide
    else:
        return ' '


def afficher_grille(grille):
    # afficher la ligne d'indice de colonne de 0-9:
    print('    ' + '   '.join([str(i) for i in range(len(grille) + 1)]))
    print('  -------------------------------------')

    #afficher le reste de grille:
    cpt = 0
    for ligne in grille:
        chaque_ligne = ''
        #afficher chaque ligne avec son indice de A - I
        for col in ligne:
            chaque_ligne += afficher_carre(col) + ' | '
        print(string.ascii_uppercase[cpt], '|', chaque_ligne)
        print('  -------------------------------------')
        cpt += 1
    print("Jouer 1:•                    Jouer 2: ∘")


#afficher_grille(grille_depart)

#### SAISIE


###fonction de verification
### verification de format
def est_au_bon_format(ligne, col):
    # Si l'indice de ligne est une lettre majuscule
    est_char = str(ligne).isupper()
    # Si l'indice de colonne est un chiffre
    est_int = isinstance(col, int)
    if est_char == 1 & est_int == 1:
        return True
    else:
        return False


def test_est_au_bon_format():
    assert est_au_bon_format('A', 7) == True
    assert est_au_bon_format('U', 9) == True
    assert est_au_bon_format('b', 9) == False
    assert est_au_bon_format('Abc', 90) == False
    assert est_au_bon_format(10, 'E') == False
    assert est_au_bon_format('Abc', 'H') == False
    assert est_au_bon_format(7, 90) == False
    print("1. Les coordonnee sont au bonne format")


### verification dans grille
def est_dans_grille(ligne, col, grille):
    taille = len(grille)
    # Verifier la position par rapport a la taille de la grille:
    pos_ligne = string.ascii_uppercase.index(ligne)
    if (pos_ligne < taille) & (col < taille):
        return True
    else:
        return False


def test_est_dans_grille():
    assert est_dans_grille('E', 5, grille_depart) == True
    assert est_dans_grille('C', 8, grille_depart) == True
    assert est_dans_grille('Y', 10, grille_depart) == False
    print('2. Les coordonnee sont dans la grille')


### fonction de saisir
def saisir_coordonnees(grille):
    ligne = str(input("Saisir le ligne de depart vous voulez jouer : "))
    col = int(input("Saisir le colonne de depart vous voulez jouer : "))
    while (est_au_bon_format(ligne, col) == False or est_dans_grille(ligne, col, grille) == False):
        print("Les coordonnees {}{} ne sont pas au bon format ou ne sont pas dans la grille, essayez a nouveau!".format(
            ligne, col))
        ligne = str(input("Saisir le ligne vous voulez jouer : "))
        col = int(input("Saisir le colonne vous voulez jouer : "))
    #print("Les coordonnes {}{} sont au bon format et sont dans la grille".format(ligne,col))
    #print(type(ligne))
    return ligne, col


def saisir_jouer():
    jouer = int(input("Saisir le tour de jouer :"))
    while jouer != 1 and jouer != 2:
        print("Le jouer doit etre 1 ou 2, essayez a nouveau!")
        jouer = int(input("Saisir le tour de jouer :"))
    return jouer


# pour savoir si le pion est jouable par le jouer
def jouable_par_un_jouer(grille):
    jouer = saisir_jouer()
    ligne, col = saisir_coordonnees(grille)
    lig = string.ascii_uppercase.index(ligne)
    while grille[lig][col] != jouer:
        print("Le pion {}{} ne peux pas être joue par le jouer {}. Reessayez a nouveau".format(ligne, col, jouer))
        jouer = saisir_jouer()
        ligne, col = saisir_coordonnees(grille)
        lig = string.ascii_uppercase.index(ligne)
    return (lig, col, jouer)


# pour savoir si le cas est occuppe
def est_occuppee(ligne, col, grille):
    if grille[ligne][col] != 0:
        return True
    else:
        return False


#### TESTER LES DIRECTIONS
def sont_orthogonale(lig1, col1, lig2, col2):
    if (lig1 == lig2) or (col1 == col2):
        return True
    else:
        return False


def test_sont_orthogonale():
    assert sont_orthogonale(2, 1, 2, 3) == True
    assert sont_orthogonale(3, 4, 5, 4) == True
    assert sont_orthogonale(3, 4, 5, 6) == False
    assert sont_orthogonale(8, 7, 4, 7) == True
    print("3. Test bien orthogonale ")


test_sont_orthogonale()


def sont_diagonale(lig1, col1, lig2, col2):
    if (lig1 - lig2 == col1 - col2) or (lig1 - lig2 == col2 - col1):
        return True
    else:
        return False


def test_sont_diagonale():
    assert sont_diagonale(0, 0, 5, 5) == True
    assert sont_diagonale(2, 3, 4, 5) == True
    assert sont_diagonale(2, 3, 1, 2) == True
    assert sont_diagonale(4, 3, 3, 4) == True
    assert sont_diagonale(4, 1, 1, 4) == True
    assert sont_diagonale(2, 3, 1, 5) == False
    assert sont_diagonale(2, 1, 5, 4) == True
    print("4. Test bien diagonale")


test_sont_diagonale()


def est_bon_direction(lig1, col1, lig2, col2):
    if sont_orthogonale(lig1, col1, lig2, col2) or sont_diagonale(lig1, col1, lig2, col2):
        return True
    else:
        return False


def test_est_bon_direction():
    assert est_bon_direction(2, 1, 5, 4) == True
    assert est_bon_direction(2, 1, 2, 6) == True
    assert est_bon_direction(4, 3, 2, 5) == True
    assert est_bon_direction(2, 1, 3, 4) == False
    print("5. Test bonne direction")


test_est_bon_direction()


#test_est_bon_direction()
def cases_au_milieu_vide_ortho(lig1, col1, lig2, col2, grille):
    if lig1 == lig2:
        if col1 < col2:
            for col in range(col1 + 1, col2):
                if grille[lig1][col] != 0:
                    return False
            return True
        elif col1 > col2:
            for col in range(col2 - 1, col1, -1):
                if grille[lig1][col] != 0:
                    return False
            return True
    elif col1 == col2:
        if lig1 < lig2:
            for lig in range(lig1 + 1, lig2):
                if grille[lig][col1] != 0:
                    return False
            return True
        elif lig1 > lig2:
            for lig in range(lig1 - 1, lig2, -1):
                if grille[lig][col1] != 0:
                    return False
            return True
    else:
        return False


###TESTER LES ESPACES ENTRE DEUX PIONS


def test_cases_au_milieu_vide_ortho():
    assert cases_au_milieu_vide_ortho(1, 1, 1, 4, grille_milieu) == True
    assert cases_au_milieu_vide_ortho(1, 4, 1, 1, grille_milieu) == True
    assert cases_au_milieu_vide_ortho(2, 2, 2, 6, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(8, 4, 8, 7, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(5, 2, 5, 6, grille_milieu) == True
    assert cases_au_milieu_vide_ortho(5, 2, 8, 6, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(6, 6, 1, 6, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(8, 4, 1, 4, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(1, 4, 8, 4, grille_milieu) == False
    assert cases_au_milieu_vide_ortho(7, 5, 3, 5, grille_milieu) == True
    print("6. test milieu vide ortho passe")


test_cases_au_milieu_vide_ortho()


def cases_au_milieu_vide_diago(lig1, col1, lig2, col2, grille):
    #### si pion 1 est au dessous (under) de pion 2:
    if lig1 > lig2:
        # cas 1: si pion 1 est diagonale a gauche de pion 2:
        if col1 < col2:
            somme = lig1 + col1
            for lig in range(lig1 - 1, lig2, -1):
                col = somme - lig
                if grille[lig][col] != 0:
                    return False
            return True
        # cas 2: si pion 1 est diagonale a droite de pion 2:
        elif col1 > col2:
            diff = lig1 - col1
            for lig in range(lig1 - 1, lig2, -1):
                col = lig - diff
                if grille[lig][col] != 0:
                    return False
            return True

    ####si pion 1 est au dessus (above) de pion 2:
    elif lig1 < lig2:
        # si pion 1 est diagonale a gauche de pion 2:
        if col1 < col2:
            diff = lig1 - col1
            for lig in range(lig1 + 1, lig2):
                col = lig - diff
                if grille[lig][col] != 0:
                    return False
            return True

        # si pion 1 est diagonale a droite de pion 2:
        elif col1 > col2:
            somme = lig1 + col1
            for lig in range(lig1 + 1, lig2):
                col = somme - lig
                if grille[lig][col] != 0:
                    return False
            return True

    else:
        return False


def test_cases_au_milieu_vide_diago():
    #cas 1
    assert cases_au_milieu_vide_diago(2, 0, 0, 2, grille_milieu) == False  #C0, A2
    assert cases_au_milieu_vide_diago(3, 1, 0, 4, grille_milieu) == False  #D1, A4
    assert cases_au_milieu_vide_diago(6, 4, 3, 7, grille_milieu) == True  #G4, D7
    assert cases_au_milieu_vide_diago(5, 0, 1, 4, grille_milieu) == False  #F0, B4
    assert cases_au_milieu_vide_diago(7, 0, 1, 6, grille_milieu) == False

    # cas 2
    assert cases_au_milieu_vide_diago(8, 5, 5, 2, grille_milieu) == True
    assert cases_au_milieu_vide_diago(5, 6, 2, 3, grille_milieu) == True
    assert cases_au_milieu_vide_diago(6, 6, 2, 2, grille_milieu) == False

    # cas 3

    assert cases_au_milieu_vide_diago(5, 2, 8, 5, grille_milieu) == True
    assert cases_au_milieu_vide_diago(2, 3, 5, 6, grille_milieu) == True
    assert cases_au_milieu_vide_diago(2, 2, 6, 6, grille_milieu) == False
    #cas 4
    assert cases_au_milieu_vide_diago(0, 2, 2, 0, grille_milieu) == False
    assert cases_au_milieu_vide_diago(3, 7, 6, 4, grille_milieu) == True
    assert cases_au_milieu_vide_diago(0, 4, 3, 1, grille_milieu) == False  #D1, A4
    assert cases_au_milieu_vide_diago(1, 4, 5, 0, grille_milieu) == False
    assert cases_au_milieu_vide_diago(1, 6, 7, 0, grille_milieu) == False

    print("7. test milieu vide diago passe")


test_cases_au_milieu_vide_diago()


def nombre_d_espace_entre(lig1, col1, lig2, col2):
    if lig1 == lig2:
        return (abs(col1 - col2) - 1)
    elif col1 == col2:
        return (abs(lig1 - lig2) - 1)
    else:
        return (abs(col1 - col2) - 1)


def cases_au_milieu_vide(lig1, col1, lig2, col2, grille):
    if cases_au_milieu_vide_diago or cases_au_milieu_vide_ortho:
        return True
    else:
        return False


def test_nombre_d_espace_entre():
    assert nombre_d_espace_entre(3, 4, 5, 4) == 1
    assert nombre_d_espace_entre(2, 1, 2, 3) == 1
    assert nombre_d_espace_entre(1, 2, 1, 3) == 0
    assert nombre_d_espace_entre(2, 5, 3, 5) == 0
    assert nombre_d_espace_entre(0, 0, 5, 5) == 4
    assert nombre_d_espace_entre(4, 5, 2, 3) == 1
    assert nombre_d_espace_entre(2, 3, 4, 5) == 1
    assert nombre_d_espace_entre(4, 3, 3, 4) == 0
    assert nombre_d_espace_entre(5, 1, 2, 4) == 2
    assert nombre_d_espace_entre(2, 4, 5, 1) == 2
    print("8. test nombre d'espace passee")


test_nombre_d_espace_entre()


#### fonction a retourner le numero de l'opponent
def adversaire(jouer):
    if jouer == 1:
        return 2
    elif jouer == 2:
        return 1
    else:
        print("The number of jouer is wrong")
        return False


# fonction a retourner coordinnees de cas juste avant (pour enchainement)
def retourn_N(lig, col):
    return (lig - 1, col)


def retourn_E(lig, col):
    return (lig, col + 1)


def retourn_S(lig, col):
    return (lig + 1, col)


def retourn_W(lig, col):
    return (lig, col - 1)


def retourn_NE(lig, col):
    return (lig - 1, col + 1)


def retourn_SE(lig, col):
    return (lig + 1, col + 1)


def retourn_SW(lig, col):
    return (lig + 1, col - 1)


def retourn_NW(lig, col):
    return (lig - 1, col - 1)


def test_retourn_1_etape():
    assert retourn_E(2, 3) == (2, 4)
    assert retourn_N(3, 4) == (2, 4)
    assert retourn_S(4, 3) == (5, 3)
    assert retourn_S(4, 7) == (5, 7)
    assert retourn_W(4, 2) == (4, 1)
    assert retourn_NE(3, 2) == (2, 3)
    assert retourn_SE(4, 3) == (5, 4)
    assert retourn_SW(1, 2) == (2, 1)
    assert retourn_NW(3, 2) == (2, 1)

    print("9. Test jump 1 step passe")


test_retourn_1_etape()


# fonction to test la direction de pion de l'arrive par rapport au pion de depart
def est_occuppee(ligne, col, grille):
    if grille[ligne][col] != 0:
        return True
    else:
        return False


def p2_est_au_nord_de_p1(l1, c1, l2, c2):
    if (c1 == c2) and (l2 < l1):
        return True
    return False


def p2_est_a_l_est_de_p1(l1, c1, l2, c2):
    if (c1 < c2) and (l1 == l2):
        return True
    return False


def p2_est_au_sud_de_p1(l1, c1, l2, c2):
    if (c2 == c1) and (l2 > l1):
        return True
    return False


def p2_est_a_l_oest_de_p1(l1, c1, l2, c2):
    if (c1 > c2) and (l1 == l2):
        return True
    return False


def p2_est_a_NE_de_p1(l1, c1, l2, c2):
    if (c1 < c2) and (l1 > l2):
        return True
    return False


def p2_est_a_SE_de_p1(l1, c1, l2, c2):
    if (c1 < c2) and (l1 < l2):
        return True
    return False


def p2_est_a_SW_de_p1(l1, c1, l2, c2):
    if (c1 > c2) and (l1 < l2):
        return True
    return False


def p2_est_a_WN_de_p1(l1, c1, l2, c2):
    if (c1 > c2) and (l1 > l2):
        return True
    return False


def test_8_direction():
    assert p2_est_a_l_est_de_p1(3, 2, 3, 4) == True
    assert p2_est_au_nord_de_p1(2, 2, 0, 2) == True
    assert p2_est_au_sud_de_p1(4, 2, 6, 2) == True
    assert p2_est_a_l_oest_de_p1(4, 4, 4, 2) == True
    assert p2_est_a_NE_de_p1(3, 3, 1, 5) == True
    assert p2_est_a_SE_de_p1(3, 2, 5, 4) == True
    assert p2_est_a_SW_de_p1(3, 2, 5, 0) == True
    assert p2_est_a_WN_de_p1(3, 2, 1, 0) == True
    print("10. Test 8 direction passee")


test_8_direction()


# fonction a retourner nombre de cases occuppee entre deux pion
def nb_cases_occuppee(l1, c1, l2, c2, grille):
    count = 0
    if p2_est_au_nord_de_p1(l1, c1, l2, c2):
        for lig in range(l1 - 1, l2, -1):
            if est_occuppee(lig, c1, grille):
                count += 1
    elif p2_est_a_l_est_de_p1(l1, c1, l2, c2):
        for col in range(c1 + 1, c2):
            if est_occuppee(l1, col, grille):
                count += 1
    elif p2_est_au_sud_de_p1(l1, c1, l2, c2):
        for lig in range(l1 + 1, l2):
            if est_occuppee(lig, c1, grille):
                count += 1
    elif p2_est_a_l_oest_de_p1(l1, c1, l2, c2):
        for col in range(c1 - 1, c2, -1):
            if est_occuppee(l1, col, grille):
                count += 1
    elif p2_est_a_NE_de_p1(l1, c1, l2, c2):
        somme = l1 + c1
        for lig in range(l1 - 1, l2, -1):
            col = somme - lig
            if est_occuppee(lig, col, grille):
                count += 1
    elif p2_est_a_SW_de_p1(l1, c1, l2, c2):
        somme = l1 + c1
        for lig in range(
                l1 + 1,
                l2,
        ):
            col = somme - lig
            if est_occuppee(lig, col, grille):
                count += 1
    elif p2_est_a_SE_de_p1(l1, c1, l2, c2):
        diff = l1 - c1
        for lig in range(l1 + 1, l2):
            col = lig - diff
            if est_occuppee(lig, col, grille):
                count += 1
    elif p2_est_a_WN_de_p1(l1, c1, l2, c2):
        diff = l1 - c1
        for lig in range(l1 - 1, l2, -1):
            col = lig - diff
            if est_occuppee(lig, col, grille):
                count += 1
    return count


def test_nb_cases_occuppee():
    assert nb_cases_occuppee(8, 4, 0, 4, grille_milieu) == 2
    assert nb_cases_occuppee(3, 2, 3, 7, grille_milieu) == 2
    assert nb_cases_occuppee(0, 6, 7, 6, grille_milieu) == 4
    assert nb_cases_occuppee(3, 6, 3, 0, grille_milieu) == 3
    assert nb_cases_occuppee(7, 1, 1, 7, grille_milieu) == 3
    assert nb_cases_occuppee(2, 8, 7, 3, grille_milieu) == 2
    assert nb_cases_occuppee(1, 2, 6, 7, grille_milieu) == 2
    assert nb_cases_occuppee(8, 6, 4, 2, grille_milieu) == 2
    print("11. Test nb de cases occuppee passee")


test_nb_cases_occuppee()


#### Fonctions de deplacement:
### 1. Enchainement:
##a. est_enchainement()
def est_enchainement_possible(lig1, col1, lig2, col2, grille, jouer):
    if est_bon_direction(lig1, col1, lig2, col2) == False:
        return False
    else:
        if est_occuppee(lig2, col2, grille):
            return False
        else:
            adver = adversaire(jouer)
            if nombre_d_espace_entre(lig1, col1, lig2, col2) == 0:
                return False
            else:
                if nb_cases_occuppee(lig1, col1, lig2, col2, grille) != 1:
                    return False
                else:
                    if p2_est_au_nord_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_S(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_au_sud_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_N(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_l_est_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_W(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_l_oest_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_E(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_NE_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_SW(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_SE_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_NW(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_SW_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_NE(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False
                    elif p2_est_a_WN_de_p1(lig1, col1, lig2, col2):
                        l, c = retourn_SE(lig2, col2)
                        if est_occuppee(l, c, grille) == False:
                            return False
                        else:
                            if grille[l][c] == adver:
                                return True
                            else:
                                return False


def test_est_enchainement_possible():
    #cas general
    assert est_enchainement_possible(4, 1, 3, 5, grille_milieu, 1) == False
    assert est_enchainement_possible(8, 4, 1, 4, grille_milieu, 2) == False
    assert est_enchainement_possible(1, 4, 1, 5, grille_milieu, 1) == False, "No empty space!"
    assert est_enchainement_possible(6, 1, 6, 7, grille_milieu, 1) == False, "More than 1 piece in between!"
    #cas N
    assert est_enchainement_possible(8, 4, 0, 4, grille_milieu, 2) == False
    assert est_enchainement_possible(2, 5, 8, 5, grille_milieu, 2) == False
    assert est_enchainement_possible(8, 4, 4, 4, grille_milieu, 2) == False
    assert est_enchainement_possible(8, 4, 4, 4, grille_milieu, 2) == False
    assert est_enchainement_possible(6, 2, 3, 2, grille_milieu, 1) == False
    assert est_enchainement_possible(6, 2, 4, 2, grille_milieu, 1) == True
    assert est_enchainement_possible(6, 2, 4, 2, grille_milieu, 1) == True

    # cas S
    assert est_enchainement_possible(1, 1, 5, 1, grille_milieu, 1) == False
    assert est_enchainement_possible(1, 1, 4, 1, grille_milieu, 1) == True
    assert est_enchainement_possible(1, 1, 5, 1, grille_milieu, 1) == False

    # cas E
    assert est_enchainement_possible(7, 2, 7, 7, grille_milieu, 2) == False
    assert est_enchainement_possible(7, 2, 7, 6, grille_milieu, 2) == True
    assert est_enchainement_possible(3, 1, 3, 4, grille_milieu, 2) == True

    # cas W
    assert est_enchainement_possible(7, 5, 7, 1, grille_milieu, 1) == True
    assert est_enchainement_possible(7, 5, 7, 0, grille_milieu, 1) == False
    #est_enchainement_possible(8,5,2,5,grille_milieu, 2)

    # cas NE
    assert est_enchainement_possible(8, 0, 5, 3, grille_milieu, 2) == True
    assert est_enchainement_possible(8, 0, 4, 4, grille_milieu, 2) == False
    # cas SW
    assert est_enchainement_possible(3, 7, 7, 3, grille_milieu, 1) == True
    assert est_enchainement_possible(3, 7, 8, 2, grille_milieu, 1) == False
    # cas SE
    assert est_enchainement_possible(3, 3, 7, 7, grille_milieu, 1) == True
    assert est_enchainement_possible(3, 3, 8, 8, grille_milieu, 1) == False
    # cas NW
    assert est_enchainement_possible(8, 4, 5, 1, grille_milieu, 2) == True
    assert est_enchainement_possible(8, 4, 4, 0, grille_milieu, 2) == False
    print("12. test enchainement possible passee")


test_est_enchainement_possible()


##b. changer_de_campe()
### Fonction a changer la couleur, (l1,c1) sont les coordonnees du pion de depart,
###                                (l2,c2) sont les coordonnees du pion d'arrivee,
###                                 aussi on va changer la couleur du pion au milieu
def changer_de_campe(l1, c1, l2, c2, grille, jouer):
    # Si coordonnees de depart == coordonnees d'arrivee -> on ne change rien
    if ((l1 == l2) and (c1 == c2)) == True:
        return grille
    # Si non
    else:
        # Le pion de d'arrivee sera occupee, le cas de depart devient vide
        grille[l1][c1] = 0
        grille[l2][c2] = jouer
        print("changed the starting and ending pos")
        # Si deux positions sont orthogonales:
        if sont_orthogonale(l1, c1, l2, c2):
            # Si elles sont dans la meme ligne:
            if l1 == l2:
                # Si pos. 1 est a gauche de pos. 2:
                if c1 < c2:
                    l, c = retourn_W(l2, c2)
                    grille[l][c] = jouer
                    ligne = string.ascii_uppercase[l]
                    print("Le pion {}{} est change de campe".format(ligne, c))
                # Si pos. 1 est a droite de pos. 2:
                elif c1 > c2:
                    l, c = retourn_E(l2, c2)
                    grille[l][c] = jouer
                    ligne = string.ascii_uppercase[l]
                    print("Le pion {}{} est change de campe".format(ligne, c))
            # Si elles sont dans la meme colonne:
            elif c1 == c2:
                # Si pos. 1 est au dessus de pos. 2:
                if l1 < l2:
                    l, c = retourn_N(l2, c2)
                    grille[l][c] = jouer
                    ligne = string.ascii_uppercase[l]
                    print("Le pion {}{} est change de campe".format(ligne, c))
                # Si pos. 1 est au dessous de pos. 2:
                elif l1 > l2:
                    l, c = retourn_S(l2, c2)
                    grille[l][c] = jouer
                    ligne = string.ascii_uppercase[l]
                    print("Le pion {}{} est change de campe".format(ligne, c))
        # Si deux positions sont diagonales:
        elif sont_diagonale(l1, c1, l2, c2):
            # si pos. 2 est de nord-est de pos.1:
            if p2_est_a_NE_de_p1(l1, c1, l2, c2):
                l, c = retourn_SW(l2, c2)
                grille[l][c] = jouer
                ligne = string.ascii_uppercase[l]
                print("Le pion {}{} est change de campe".format(ligne, c))
            # si pos. 2 est de sud-oest de pos.1:
            elif p2_est_a_SW_de_p1(l1, c1, l2, c2):
                l, c = retourn_NE(l2, c2)
                grille[l][c] = jouer
                ligne = string.ascii_uppercase[l]
                print("Le pion {}{} est change de campe".format(ligne, c))
            # si pos. 2 est de sud-est de pos.1:
            elif p2_est_a_SE_de_p1(l1, c1, l2, c2):
                l, c = retourn_NW(l2, c2)
                grille[l][c] = jouer
                ligne = string.ascii_uppercase[l]
                print("Le pion {}{} est change de campe".format(ligne, c))
            # si pos. 2 est de nord-oest de pos.1:
            elif p2_est_a_WN_de_p1(l1, c1, l2, c2):
                l, c = retourn_SE(l2, c2)
                grille[l][c] = jouer
                ligne = string.ascii_uppercase[l]
                print("Le pion {}{} est change de campe".format(ligne, c))
        return grille
    #elif sont_diagonale(l1, c1, l2, c2):
    #    if


#g1 = changer_de_campe(5,2,0,7,grille_milieu,2)
#afficher_grille(g1)
### Jouer a nouveau:
def enchainement_a_nouveau():
    play_again = str(input("Voulez vous appliquer un autre enchainement? Tapez y/n!\n"))
    while (play_again != 'y') and (play_again != 'n'):
        play_again = str(input("Reessayez (y/n)?"))
    return play_again


enchainement_a_nouveau()


### 2. Enchainement
def est_elimination_possible(lig1, col1, lig2, col2, grille, jouer):
    if est_bon_direction(lig1, col1, lig2, col2) == False:
        return False
    else:
        if est_occuppee(lig2, col2, grille) == False:
            return False
        else:
            adver = adversaire(jouer)
            if grille[lig2][col2] != adver:
                return False
            else:
                if nombre_d_espace_entre(lig1, col1, lig2, col2) == 0:
                    return True
                else:
                    if nb_cases_occuppee(lig1, col1, lig2, col2, grille) == 0:
                        return True
                    else:
                        return False


def test_est_elimination_possible():
    # cas general :
    assert est_elimination_possible(3, 1, 2, 3, grille_milieu, 2) == False
    assert est_elimination_possible(3, 1, 3, 4, grille_milieu, 2) == False
    # no space
    assert est_elimination_possible(6, 2, 7, 2, grille_milieu, 1) == True
    assert est_elimination_possible(2, 2, 2, 3, grille_milieu, 1) == False
    #with space
    assert est_elimination_possible(5, 7, 8, 7, grille_milieu, 1) == True
    assert est_elimination_possible(5, 7, 3, 7, grille_milieu, 1) == False
    print("test est elimination passe")


#test_est_elimination_possible()

##### Appliquer le deplacement


### 1. Enchainement
def enchainement(grille, jouer):
    print("TOUR DE JOUER {} :".format(jouer))
    print("Saisir les coordonnees de depart:")
    l1, c1 = saisir_coordonnees(grille)
    l1 = string.ascii_uppercase.index(l1)
    while grille[l1][c1] != jouer:
        print("Le pion choisi n'est pas de jouer {}! Ressayez a nouveau!".format(jouer))
        l1, c1 = saisir_coordonnees(grille)
        l1 = string.ascii_uppercase.index(l1)
    print("Saisir les coordonnees de arrivee:")
    l2, c2 = saisir_coordonnees(grille)
    l2 = string.ascii_uppercase.index(l2)
    while est_enchainement_possible(l1, c1, l2, c2, grille, jouer) == False:
        print("L'enchainement ne peut pas etre applique, reessayez les coordinees a nouveau!")
        l1, c1 = saisir_coordonnees(grille)
        l1 = string.ascii_uppercase.index(l1)
        print("Saisir les coordonnees de arrivee:")
        l2, c2 = saisir_coordonnees(grille)
        l2 = string.ascii_uppercase.index(l2)

    grille = changer_de_campe(l1, c1, l2, c2, grille, jouer)
    afficher_grille(grille)
    play_again = enchainement_a_nouveau()
    while play_again != 'n':
        l1, c1 = l2, c2
        l1_alphabet = string.ascii_uppercase[l1]
        print("Le coordonnees du depart est mis a jour a {}{}".format(l1_alphabet, c1))
        print("Saisir les coordonnees de l'arrivee:")
        l2_nouv, c2_nouv = saisir_coordonnees(grille)
        l2_nouv = string.ascii_uppercase.index(l2_nouv)
        # Tant que l'enchainement ne peut pas appliquee et coor de debut == coor d'arrivee:
        while est_enchainement_possible(l1, c1, l2_nouv, c2_nouv, grille,
                                        jouer) == False and ((l1, c1) != (l2_nouveau, c2_nouveau)):
            print("L'enchainement ne peut pas etre applique, reessayez les coordinees a nouveau!")
            play_again = enchainement_a_nouveau()
            if play_again == 'y':
                l2_nouv, c2_nouv = saisir_coordonnees(grille)
                l2_nouv = string.ascii_uppercase.index(l2)
            else:
                l2_nouv, c2_nouv = l1, c1
        l2, c2 = l2_nouv, c2_nouv
        grille = changer_de_campe(l1, c1, l2, c2, grille, jouer)
        afficher_grille(grille)
        play_again = str(input("Voulez-vous appliquer un autre enchainement? (y/n)?"))
    return grille


afficher_grille(grille_milieu)
enchainement(grille_milieu, 2)

### 2. Elimination
#def elimination(grille)

#afficher_grille(grille_actuel)
sys.stdin.readline()

#### CODE PRINCIPAL
# execution affichage sur les 3 grilles et autres variables de jeuxy
# tester chaque fonction séparament
#print("Affichage de la grille au debut")
#afficher_grille(grille_depart)
#print("Affichage de la grille au milieu")
#afficher_grille(grille_milieu)
#print("Affichage de la grille a la fin")
#afficher_grille(grille_fin)
#execution test est_dans_grille
#test_est_dans_grille()
#test_est_au_bon_format()
#affichage des coordonnees saisies pour chaque jouer
# jouer 1 : *
# jouer 2 : @
#saisir_coordonnees(grille_depart)
#jouable(grille_milieu)
