"""
Jeu de monstres turn based
Par Kamyar Orasi
"""
import random

def game_menu():
    niveau_vie = 20
    force_adversaire = random.randint(1, 5)
    print(f"Vous tombez sur un adversaire de niveau {force_adversaire}")
    action = input("Que voulez-vous faire?"
                   "    1- Combattre le monstre    2- Fuir le monstre   3- Afficher les règles du jeu   4- Quitter la partie")
game_menu()