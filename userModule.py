import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter import PhotoImage
import json
import re
from functools import partial
import urllib.parse
import subprocess
from os import system


# Variable pour garder une référence aux images
images = {}
NOTEBOOK_TEXTS = {}
CURRENT_NOTEBOOK_INDEX = -1
NOTEBOOK_WINDOWS = {}
CALLBACK_ONCHANGE_WINDOW = None

def createNoteBook(frame):
    notebook = ttk.Notebook(frame)

    def setCurrentIndex(event):
        global CURRENT_NOTEBOOK_INDEX, CALLBACK_ONCHANGE_WINDOW
        CURRENT_NOTEBOOK_INDEX = notebook.index("current")
        if CALLBACK_ONCHANGE_WINDOW is not None:
            CALLBACK_ONCHANGE_WINDOW()

    notebook.bind("<<NotebookTabChanged>>", setCurrentIndex)
    return notebook

def getCurrentEdit():
    global CURRENT_NOTEBOOK_INDEX
    return NOTEBOOK_TEXTS[CURRENT_NOTEBOOK_INDEX]

def getCurrentNotebook():
    global CURRENT_NOTEBOOK_INDEX
    return NOTEBOOK_WINDOWS[CURRENT_NOTEBOOK_INDEX]

def addTab(notebook, title, content=None, server_status='stopped'):
    # Frame pour le contenu de l'onglet
    kframe = ttk.Frame(notebook)

    # Charger les images pour les icônes de statut (cercle vert et rouge)
    if 'green_circle' not in images:
        green_circle = PhotoImage(width=10, height=10)
        green_circle.put("green", to=(0, 0, 10, 10))
        images['green_circle'] = green_circle
    else:
        green_circle = images['green_circle']

    if 'red_circle' not in images:
        red_circle = PhotoImage(width=10, height=10)
        red_circle.put("red", to=(0, 0, 10, 10))
        images['red_circle'] = red_circle
    else:
        red_circle = images['red_circle']
    
    # Créer un cercle coloré pour l'état du serveur (image)
    if server_status == 'running':
        status_icon = green_circle
    else:
        status_icon = red_circle

    # Ajouter l'onglet avec une icône + titre
    notebook.add(kframe, text=title[0], image=status_icon, compound='left')

    # Créer un widget Text pour l'éditeur de texte
    text_widget = tk.Text(kframe, wrap='word', width=130, height=35)
    NOTEBOOK_TEXTS[len(notebook.tabs())-1] = text_widget
    NOTEBOOK_WINDOWS[len(notebook.tabs())-1] = title[0]
    
    # Créer une barre de défilement
    scrollbar = ttk.Scrollbar(kframe, orient='vertical', command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
    # Placer l'éditeur de texte et la barre de défilement dans le frame
    text_widget.grid(column=0, row=0, padx=5, pady=5)
    scrollbar.grid(column=1, row=0, sticky='ns', padx=5, pady=5)
    
    # Si un contenu est passé, le mettre dans l'éditeur de texte
    if content:
        highlight_json(text_widget, content)

    notebook.pack()

def update_tab_icon(notebook, server_status, index = None):
    global CURRENT_NOTEBOOK_INDEX
    # Charger les images pour les icônes de statut (cercle vert et rouge)
    if 'green_circle' not in images:
        green_circle = PhotoImage(width=10, height=10)
        green_circle.put("green", to=(0, 0, 10, 10))
        images['green_circle'] = green_circle
    else:
        green_circle = images['green_circle']

    if 'red_circle' not in images:
        red_circle = PhotoImage(width=10, height=10)
        red_circle.put("red", to=(0, 0, 10, 10))
        images['red_circle'] = red_circle
    else:
        red_circle = images['red_circle']

    # Déterminer l'icône en fonction de l'état
    if server_status == 'running':
        status_icon = green_circle
    else:
        status_icon = red_circle
    
    # Modifier l'icône de l'onglet spécifié
    if index is None:
        notebook.tab(CURRENT_NOTEBOOK_INDEX, image=status_icon)
    else:
        notebook.tab(index, image=status_icon)

# Get the id from the responses listbox content, and return corresponding response from list
def findInResponses(id, responses):
    for r in responses:
        if r[0] == id:
            return r

def set_notebook_style():
    style = ttk.Style()

    # Définir la couleur de fond du Notebook et des onglets
    style.configure('TNotebook', background='white')
    
    # Agrandir les onglets
    style.configure('TNotebook.Tab',
                    background='white',
                    padding=[20, 10],  # Plus de padding (plus grand espace autour du texte)
                    font=('Helvetica', 12, 'bold'))  # Augmenter la taille de la police et le style
    
    # Appliquer un changement de couleur à l'onglet sélectionné
    style.map('TNotebook.Tab', background=[('selected', 'lightgray')])

def listResponses(listbox, responses):
    listbox.delete(0, "end")
    for resp in responses:
        listbox.insert("end", (resp[0], str(resp[1])[:7]))

def register_callback(callback):
    global CALLBACK_ONCHANGE_WINDOW
    CALLBACK_ONCHANGE_WINDOW = callback

def highlight_json(text_widget, json_text):
    """Applique la coloration syntaxique au texte JSON."""
    
    # Efface le texte précédent
    text_widget.delete(1.0, tk.END)
    
    # Insérer le texte JSON dans l'éditeur
    text_widget.insert(tk.END, json_text)
    
    # Définir les tags de coloration
    text_widget.tag_configure("string", foreground="green")
    text_widget.tag_configure("key", foreground="blue")
    text_widget.tag_configure("number", foreground="red")
    text_widget.tag_configure("boolean", foreground="purple")
    text_widget.tag_configure("null", foreground="gray")
    text_widget.tag_configure("comment", foreground="gray")

    # Commentaires : lignes qui commencent par '#' après des espaces
    for match in re.finditer(r'^[ \t]*#.*$', json_text, re.MULTILINE):
        text_widget.tag_add("comment", f"1.0+{match.start()}c", f"1.0+{match.end()}c")
    
    # Appliquer la coloration syntaxique avec des expressions régulières
    # Clés JSON : "key" (tout ce qui est entre guillemets)
    for match in re.finditer(r'"(.*?)":', json_text):
        text_widget.tag_add("key", f"1.0+{match.start()}c", f"1.0+{match.end()}c")
    
    # Chaînes JSON : "string" (tout ce qui est entre guillemets)
    for match in re.finditer(r'"(.*?)"', json_text):
        text_widget.tag_add("string", f"1.0+{match.start()}c", f"1.0+{match.end()}c")
    
    # Nombres : "number"
    for match in re.finditer(r'-?\d+(\.\d+)?([eE][+-]?\d+)?', json_text):
        text_widget.tag_add("number", f"1.0+{match.start()}c", f"1.0+{match.end()}c")
    
    # Booléens : "boolean" (true/false)
    for match in re.finditer(r'\b(true|false)\b', json_text):
        text_widget.tag_add("boolean", f"1.0+{match.start()}c", f"1.0+{match.end()}c")
    
    # Null : "null"
    for match in re.finditer(r'\bnull\b', json_text):
        text_widget.tag_add("null", f"1.0+{match.start()}c", f"1.0+{match.end()}c")

def deleteTab(notebook):
    global CURRENT_NOTEBOOK_INDEX
    notebook.forget(CURRENT_NOTEBOOK_INDEX)

def select_option_by_text(text, listbox):
    for index, item in enumerate(listbox.get(0, tk.END)):
        if item == text:
            listbox.select_set(index)
            break

def getCurrentIndex():
    global CURRENT_NOTEBOOK_INDEX
    return CURRENT_NOTEBOOK_INDEX

def deleteComments(text):
    ntext = ""
    for line in text.split('\n'):
        if line.strip().startswith('#'):
            continue
        ntext+=line
    return ntext

def displayTerm(xterm_frame, geomx:str = "80", geomy:str = "20") -> None:
    # x_term can display itself on a frame based on its id
    xterm_frame_id:int = xterm_frame.winfo_id()

    # check if x_term is actually installed
    existance: int = system("dpkg --list | grep 'xterm'")
    if existance != 0:
        return False

    # Now exec the terminal
    p = subprocess.Popen(["xterm", "-into", str(xterm_frame_id), "-geometry", geomx+"x"+geomy], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

USE_MODULE_FUNCS = {
    'getCurrentIndex': getCurrentIndex,
    'urlLibParse': urllib.parse
}