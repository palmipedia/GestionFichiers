def compterOccurrences(t,c):
    nbocc = t.count(c)
    return nbocc

def compterCaracteres(t):
    nbcar = len(t)
    return nbcar

def compterMots(t):
    nbmots = t.split()
    return len(nbmots)

def compterLignes(t):
    nblignes = t.readlines()
    return len(nblignes)


