# --------------------------------------------------------------------------------------------
# Auteur: DigySky
# Date: 10/10/2023
# Version: 1.0
# Generator_password_with_interface_graphique
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# Importation des modules
import pyperclip
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from function import gener_password as pwd
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# Creation du fichier temporaire
if not os.path.exists("/home/sky/Documents/Pass_gen"):
    os.mkdir("/home/sky/Documents/Pass_gen")
if not os.path.exists("/home/sky/Documents/Pass_gen/password.txt"):
    with open("/home/sky/Documents/Pass_gen/password.txt", "w") as file:
        file.write("")
    file.close()
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
#Définition des fonctions
def result():
    num = int(number_chara.get())
    if num > 250:
        resultat = pwd(int(250), include_number.get())
    else:
        resultat = pwd(int(number_chara.get()), include_number.get())
    label_resultat.config(text=resultat)

def copier_texte():
    sherch_result = 0
    texte = label_resultat.cget("text")
    
    with open("/home/sky/Documents/Pass_gen/password.txt", "r") as file:
        for i in file:
            sherch = i.strip()
            if sherch == texte:
                sherch_result = 1
                break

    if sherch_result == 1:
        pyperclip.copy(texte)
        label_cpy.config(text="Le mot de passe a déjà été utilisé !")
    else:
        with open("/home/sky/Documents/Pass_gen/password.txt", "a") as file:
            file.write(f"{texte}\n\n")
        pyperclip.copy(texte)
        label_cpy.config(text="Le mot de passe a été copié dans le presse-papier !")

def open_file():
    file = filedialog.askopenfilename(initialdir="/home/sky/Documents/Pass_gen", title="Select a file")
    with open(file, "r") as file:
        contenu = file.read()
        window =tk.Toplevel()
        window.title("Password")
        window.geometry("800x700")
        
        # Créez une instance de Scrollbar
        scrollbar = ttk.Scrollbar(window)

        # Créez un widget Text pour afficher le contenu du fichier
        texte = tk.Text(window, wrap="word")
        texte.insert(tk.END, contenu)
        texte.configure(state="disabled")

        # Associez la Scrollbar à votre zone de texte
        texte.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=texte.yview)

        # Placez la Scrollbar et la zone de texte dans votre fenêtre
        scrollbar.pack(side="right", fill="y")
        texte.pack(side="left", fill="both", expand=True)
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# Création de la fenêtre principale
window = tk.Tk() # You want the root window to be your window
window.title("Generateur de mot de passe") # You want the title to be "Password Generator"
window.geometry("800x400") # You want the size of the app to be 500x500
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# Menu
barre_menu = tk.Menu(window) # You want the menu to be in the window

# Création du menu "Fichier"
menu_fichier = tk.Menu(barre_menu, tearoff=0) # You want the menu to be in the menu bar
menu_fichier.add_command(label="Genéré", command=result) # You want the menu to be "New" and the command to be the function you created
menu_fichier.add_command(label="Ouvrir", command=open_file) # You want the menu to be "Open" and the command to be the function you created
menu_fichier.add_separator() # You want a separator
menu_fichier.add_command(label="Quitter", command=window.quit) # You want the menu to be "Quit" and the command to be the function you created
barre_menu.add_cascade(label="Fichier", menu=menu_fichier) # You want the menu to be "File" and the menu to be the menu you created

# Création du menu "Édition"
menu_edition = tk.Menu(barre_menu, tearoff=0) # You want the menu to be in the menu bar
menu_edition.add_command(label="Copier", command=copier_texte) # You want the menu to be "Copy" and the command to be the function you created
barre_menu.add_cascade(label="Édition", menu=menu_edition) # You want the menu to be "Edit" and the menu to be the menu you created

# Configuration de la fenêtre principale pour afficher la barre de menu
window.config(menu=barre_menu) # You want the menu to be in the window
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# Création des cadres d'entrée utilisateur 
label_nbchara = tk.Label(window, text="Nombre de charactère (par defaut 12)") # You want the label to be "Number of characters (default 12)"
label_nbchara.config(font=("Helvetica", 16)) # You want the font to be Helvetica and the size to be 16
label_nbchara.pack(side="top", anchor="ne", padx=1, pady=5) # You want the label to be on the top right of the window

number_chara = tk.Spinbox(window, from_=0, to='inf') # You want the spinbox to be from 0 to infinity
number_chara.config(width=5, font=("Helvetica", 30)) # You want the width to be 5 and the font to be Helvetica and the size to be 30
number_chara.pack(side="top", anchor="ne", padx=10, pady=10)    # You want the spinbox to be on the top right of the window

include_number = tk.IntVar() # You want the variable to be an integer
include_number.set(1) # You want the variable to be 1
case1 = tk.Checkbutton(window, text="Inclure des chiffres", variable=include_number) # You want the checkbutton to be "Include numbers" and the variable to be the variable you created
case1.pack(anchor="nw", padx=10, pady=10) # You want the checkbutton to be on the top left of the window

buton = tk.Button(window, text="Generer", command=result) # You want the button to be "Generate" and the command to be the function you created
buton.pack(anchor="center", padx=10, pady=10) # You want the button to be on the center of the window
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# affichage du bouton "copier" et du resultat
label_resultat = tk.Label(window, text="") # You want the label to be empty
label_resultat.config(font=("Helvetica", 30)) # You want the font to be Helvetica and the size to be 30
label_resultat.pack(anchor="center", padx=10, pady=10) # You want the label to be on the center of the window

label_cpy = tk.Label(window, text="") # You want the label to be empty
label_cpy.config(font=("Helvetica", 16)) # You want the font to be Helvetica and the size to be 16
label_cpy.pack(anchor="center", padx=10, pady=10) # You want the label to be on the center of the window

bouton_copier = tk.Button(window, text="Copier", command=copier_texte) # You want the button to be "Copy" and the command to be the function you created
bouton_copier.pack(anchor="s", padx=10, pady=10) # You want the button to be on the bottom of the window

window.mainloop() # You want the window to loop
# --------------------------------------------------------------------------------------------

