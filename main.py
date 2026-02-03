
def dans_alphabet(c):
    return 'A' <= c <= 'Z'
def transition (etat_ancien, lettre) :
    nouv_etat = etat_ancien
    if dans_alphabet(lettre) :
        if etat_ancien == 8:
            if lettre == 'W':
                nouv_etat = 4
            elif lettre == 'I':
                nouv_etat = 9
            else : nouv_etat = 3
        elif etat_ancien == 4:
            if lettre == 'H':
                nouv_etat = 5
            else:
                nouv_etat = 3
        elif etat_ancien == 9:
            if lettre == 'F':
                nouv_etat = 2
            else:
                nouv_etat = 3
        elif etat_ancien == 5:
            if lettre == 'I':
                nouv_etat = 6
            else:
                nouv_etat = 3
        elif etat_ancien == 6:
            if lettre == 'L':
                nouv_etat = 7
            else:
                nouv_etat = 3
        elif etat_ancien == 7:
            if lettre == 'E':
                nouv_etat = 1
            else:
                nouv_etat = 3

    print(lettre, "  ", etat_ancien ,"->", nouv_etat)
    return nouv_etat
etat_initial = 8
etats_finaux = {1, 2, 3}
etat_actuel = 8

def automate(etat_depart, mot):
    global etat_actuel
    etat_actuel = etat_depart
    for lettre in mot:


        etat_actuel = transition(etat_actuel, lettre)
        if etat_actuel is None:
            return False
    return etat_actuel in etats_finaux

print(automate(etat_initial, "A"))
print(automate(etat_initial, "B"))
print(automate(etat_initial,"C"))
print(automate(etat_initial, "WHILE"))
print(automate(etat_initial, "D"))
print(automate(etat_initial,"IF"))

print("--------------------------")

print(automate(etat_initial, "W"))
print(automate(etat_initial, "I"))
print(automate(etat_initial, "WHIL"))
print(automate(etat_initial, "WH"))
print(automate(etat_initial, "WHI"))

