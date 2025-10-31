#Creation + Ecriture
f = open("test.txt", "w")
contenu = """ Ceci est un contenu d'un fichier.
              Il est utilisé pour les besoins de test.
              Il peut être effacé sans demander l'accord
              de son auteur.
          """
f.write(contenu)
f.close()

#Lecture
f = open("test.txt", "r")
contenu = f.readlines()
print(contenu)
f.close()

#Lecture
f = open("test.txt", "a")
contenu = """Ceci est la fin du contenu.
          """
f.write(contenu)
f.close()
