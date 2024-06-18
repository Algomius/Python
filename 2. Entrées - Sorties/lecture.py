import sys
n1 = int(input("Nombre 1 ?"))
n2 = int(input("Nombre 2 ?"))
print("J'ecris", n1, "sur la sortie standard", file=sys.stdout)
print("J'ecris", n2, "sur la sortie standard d'erreur", file=sys.stderr)