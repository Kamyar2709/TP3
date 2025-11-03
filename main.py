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
    nombre_victoires_consecutives = 0
    while game == True:
        if nombre_victoires_consecutives % 3 == 0 and nombre_victoires_consecutives != 0:
            force_adversaire = random.randint(4, 5) + random.randint(4, 5)
            print(f"Vous tombez sur un boss de niveau {force_adversaire}")
            action = input("Que voulez-vous faire?    \n\n1- Combattre le monstre    \n2- Fuir le monstre   \n3- Afficher les règles du jeu   \n4- Quitter la partie \n")
        else:
            force_adversaire = random.randint(1, 5) + random.randint(1, 5)
            print(f"Vous tombez sur un adversaire de niveau {force_adversaire}")
            action = input("Que voulez-vous faire?    \n\n1- Combattre le monstre    \n2- Fuir le monstre   \n3- Afficher les règles du jeu   \n4- Quitter la partie \n")
            if action == "1":
                numero_combat += 1
                dice_score = random.randint(1, 6) + random.randint(1, 6)
                print(f"Vous avez lancé un {dice_score}")
                if dice_score > force_adversaire:
                    battle_status = "victoire"
                    nombre_victoires += 1
                    nombre_victoires_consecutives += 1
                    niveau_vie = niveau_vie + force_adversaire
                    print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}   \nstatut: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites} Victoires consecutives:\n{nombre_victoires_consecutives}")
                else:
                    battle_status = "défaite"
                    nombre_defaites += 1
                    nombre_victoires_consecutives = 0
                    niveau_vie = niveau_vie - force_adversaire
                    print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}    \nCombat: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites} \nVictoires consecutives:{nombre_victoires_consecutives}")
            elif action == "2":
                niveau_vie -= 1
                print("vous avez echappé les monstre. Vous avez perdu 1 point de vie.")
            elif action == "3":
                print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
            elif action == "4":
                game = False
                print("À revoir!")
            elif niveau_vie == "0":
                game = False
                print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")

game_menu()