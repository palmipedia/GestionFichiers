from fichiers import *

"""f = open("data/poeme.txt", "r", encoding="utf-8")
contenu = f.read()
f.close()

#print(contenu)

#print("\n-------------------------------------------")

with open("data/poeme.txt", "r", encoding="utf-8") as f:
    contenu=f.read()

#print(contenu)

print("\n-------------------------------------------")

contenuModifie = contenu.swapcase()

#print(contenuModifie)

with open("data/poeme2.txt", "w", encoding="utf-8") as f:
    f.write(contenuModifie)

with open("data/poeme2.txt", "r", encoding="utf-8") as f:
    contenu=f.read()

print(contenu)"""

with open("data/poeme.txt", "r", encoding="utf-8") as f:
    texte=f.read()

"""lettre = input("\nLettre à trouver ? ")

occurrence = compterOccurrences(texte, lettre)

print(f"\nIl y a {occurrence} '{lettre}'")"""

caracteres = compterCaracteres(texte)

print(f"\nIl y a {caracteres} caractères")

mots = compterMots(texte)

print (f"\nIl y a {mots} mots")

lignes = compterLignes(texte)

print (f"\nIl y a {lignes}")

