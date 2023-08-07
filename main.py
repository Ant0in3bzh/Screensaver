import tkinter as tk
import webbrowser
import pyautogui
import time
import keyboard
import sys
import datetime
import random
import json


# Fonction pour ouvrir le lien YouTube dans le navigateur par défaut
def open_youtube_link(youtube_link):
    webbrowser.open(youtube_link)
    time.sleep(10)  # Attendre quelques secondes pour que la vidéo soit chargée
    pyautogui.press(
        "f"
    )  # Simuler l'appui sur la touche "F" pour passer en mode plein écran


# Définir le gestionnaire d'événements pour la touche ²
def check_key_press():
    if any(keyboard.is_pressed(key) for key in keys_to_detect):
        pyautogui.press(
            "esc"
        )  # Simuler l'appui sur la touche "K" pour mettre en pause la vidéo
        pyautogui.hotkey("ctrl", "w")
        sys.exit(1)
    root.after(100, check_key_press)  # Vérifier à nouveau après 100 ms


def date_time(liste_youtube_nuit: list, liste_youtube_jour: list):
    heure_actuelle = datetime.datetime.now().time()
    heure_apres_12h = (
        datetime.datetime.combine(datetime.date.today(), heure_actuelle)
        + datetime.timedelta(hours=12)
    ).time()
    if heure_apres_12h.hour > 7 & heure_apres_12h.hour < 18:
        choix_random = random.choice(liste_youtube_nuit)
        return choix_random
    else:
        if heure_actuelle.hour > 7:
            choix_random = random.choice(liste_youtube_jour)
            return choix_random


if __name__ == "__main__":
    # Lien YouTube de la vidéo à afficher en écran de veille
    # youtube_jour = "https://www.youtube.com/watch?v=dm64fxEmRus&ab_channel=CoralGardeners"
    # youtube_nuit = "https://www.youtube.com/watch?v=AGri76vwuLc&ab_channel=Africam"

    with open("link_day.json", "r") as json_file:
        json_data = json.load(json_file)

    # Stocker la catégorie "youtube_nuit" dans la variable liste_youtube_nuit
    liste_youtube_nuit = json_data["youtube_nuit"]

    # Stocker la catégorie "youtube_jour" dans la variable liste_youtube_jour
    liste_youtube_jour = json_data["youtube_jour"]
    # Création de la fenêtre principale
    root = tk.Tk()
    root.geometry("800x600")  # Définir la taille de la fenêtre

    # Configuration de la fenêtre pour qu'elle soit en plein écran
    root.attributes("-fullscreen", True)

    # Définir la liste de touches à détecter
    keys_to_detect = ["²", "alt", "ctrl", "shift", "delete", "return", "escape"]

    # Bouton pour ouvrir le lien YouTube
    button = tk.Button(root, text="Ouvrir YouTube", command=open_youtube_link)
    button.pack(pady=10)

    # Determiner le lien à utiliser en fonction de l'heure
    youtube_link = date_time(
        liste_youtube_nuit=liste_youtube_nuit, liste_youtube_jour=liste_youtube_jour
    )
    # Ouvrir le lien YouTube dans le navigateur par défaut
    open_youtube_link(youtube_link)

    # Démarrer la vérification de la touche ²
    check_key_press()

    # Démarrage de la boucle principale de l'application
    root.mainloop()
