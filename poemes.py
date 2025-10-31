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


lettre = input("\nLettre à trouver ? ")

with open("data/poeme.txt", "r") as f:
    texte=f.read()

occurrence = compterOccurrences(texte, lettre)

print(f"\nIl y a {occurrence} '{lettre}'")

caracteres = compterCaracteres(texte)

print(f"\nIl y a {caracteres} caractères")
