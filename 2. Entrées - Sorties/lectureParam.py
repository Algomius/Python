import sys
from sys import argv
print(argv)
if len(argv) == 3:
    prog, nom, age = argv
elif len(argv) == 2:
    prog, nom = argv
    age = input("Merci de donner votre age : ")
elif len(argv) == 1:
    prog = argv[0]
    nom = input("Merci de donner votre nom : ")
    age = input("Merci de donner votre age : ")
else:
    print("Usage : lectureParam.py <nom> <age>")
    sys.exit(8)

print("Nom du programme", prog)
print("Nom de l'utilisateur", nom)
print("Age de l'utilisateur", age)
sys.exit(0)