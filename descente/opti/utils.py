
from numpy.linalg.linalg import norm

def save_f(liste, path):
    fichier = open(path, "w")
    for e in liste:
        fichier.write(str(e[1]))
        fichier.write(";")
        fichier.write(str(norm(e[3])))
        fichier.write(";")
        fichier.write(str(e[2]))
        fichier.write(";")
        fichier.write(str(e[0][0]))
        fichier.write(";")
        fichier.write(str(e[0][1]))
        fichier.write("\n")
    fichier.close()
    
def load_f(path):
    fichier = open(path, "r")
    list = []
    lines = fichier.readlines()
    for line in lines:
        tab = line.split(";")[:-1]
        print(tab[-1])
    fichier.close()
    return list
