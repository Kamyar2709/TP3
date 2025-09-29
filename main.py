"""
Jeu de monstres turn based
Par Kamyar Orasi
"""
import random

def game_menu():
    niveau_vie = 20
    numero_adversaire = 1
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    force_adversaire = random.randint(1, 5)
    print(f"Vous tombez sur un adversaire de niveau {force_adversaire}")
    action = input("Que voulez-vous faire?    \n\n1- Combattre le monstre    \n2- Fuir le monstre   \n3- Afficher les règles du jeu   \n4- Quitter la partie \n")

    while action != 4:
        if action == "1":
            numero_combat += 1
            dice_score = random.randint(1, 6)
            if dice_score > force_adversaire:
                battle_status = "victoire"
                nombre_victoires += 1
                niveau_vie = niveau_vie + force_adversaire
                print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}   \nstatut: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites}")
                statut_jeu = input("que voulez vous faire maintenant?")
            else:
                battle_status = "défaite"
                nombre_defaites += 1
                niveau_vie = niveau_vie - force_adversaire
                print(f"Adversaire : {numero_adversaire}  \nForce de l’adversaire : {force_adversaire}    \nCombat: {battle_status} \nNiveau de vie: {niveau_vie}  \nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites}")
game_menu()