import tkinter as tk


def recuperer_code(event):
    # On récupère le nom de la touche et son code
    nom_touche = event.keysym
    code_touche = event.keycode

    # On met à jour l'affichage
    label_info.config(text=f"Touche : {nom_touche}\nID (keycode) : {code_touche}")
    print(f"DEBUG: Touche pressée = {nom_touche} | ID = {code_touche}")


# Configuration de la fenêtre
root = tk.Tk()
root.title("Détecteur de touches")
root.geometry("300x200")

label_instruction = tk.Label(root, text="Appuie sur une touche pour voir son ID", pady=20)
label_instruction.pack()

label_info = tk.Label(root, text="ID : En attente...", font=("Helvetica", 14, "bold"), fg="blue")
label_info.pack(pady=20)

# On lie n'importe quelle pression de touche à notre fonction
root.bind("<Key>", recuperer_code)

root.mainloop()