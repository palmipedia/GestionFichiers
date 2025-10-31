import os

def compterOccurences(fichier:str, texte:str) -> int:
    if not os.path.exists(fichier):
        return -1
    if not os.path.isfile(fichier):
        return 0
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        return contenu.count(texte)

def compterLignes(fichier:str) -> int:
    if not os.path.isfile(fichier):
        return 0
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.readlines()
        return len(contenu)

def compterMots(fichier:str) -> int:
    if not os.path.isfile(fichier):
        return 0
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        listeMots = contenu.split()
        return len(listeMots)

def compterCaracteres(fichier:str) -> int:
    if not os.path.isfile(fichier):
        return 0
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        return len(contenu)

def compterMiniscules(fichier:str) -> int:
    if not os.path.isfile(fichier):
        return 0
    with open(fichier, "r", encoding="utf-8") as f:
        return [mot for mot in f.read().split() if mot.islower() and len(mot)>1]


