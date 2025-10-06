"""
Jeu de monstres turn based
Par Kamyar Orasi
"""
import random

def game_menu():
    game = True
    niveau_vie = 20
    numero_adversaire = 1
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    force_adversaire = random.randint(1, 5)
    print(f"Vous tombez sur un adversaire de niveau {force_adversaire}")
    action = input("Que voulez-vous faire?    \n\n1- Combattre le monstre    \n2- Fuir le monstre   \n3- Afficher les règles du jeu   \n4- Quitter la partie \n")

    while game == True:
        if action == "1":
            numero_combat += 1
            dice_score = random.randint(1, 6)
            print(f"Vous avez lancé un {dice_score}")
            if dice_score > force_adversaire:
                battle_status = "victoire"
                nombre_victoires += 1
                niveau_vie = niveau_vie + force_adversaire
                print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}   \nstatut: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites}")
                st
            else:
                battle_status = "défaite"
                nombre_defaites += 1
                niveau_vie = niveau_vie - force_adversaire
                print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}    \nCombat: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites}")
                statut_jeu = input("que voulez vous faire maintenant? 1/2/3/4")
        if action == "2":
            niveau_vie -= 1
            print("vous avez echappé le monstre. Vous avez perdu 1 point de vie.")
            action = input("que voulez vous faire?")
        if action == "3":
            print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
        if action == 4:





        if niveau_vie == 0
            print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
game_menu()