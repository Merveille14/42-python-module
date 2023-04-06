import sys

# Vérifie si le nombre est impair, pair ou zéro
def check_number(number):
    if not isinstance(number, int):
        print("Erreur : L'argument n'est pas un entier.")
        return
    if number == 0:
        print("Le nombre est zéro.")
    elif number % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

# Vérifie s'il y a un seul argument et s'il est un entier, puis appelle la fonction check_number
if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
        check_number(number)
    except ValueError:
        print("Erreur : L'argument n'est pas un entier.")
else:
    print("Erreur : Vous devez fournir un seul argument qui est un entier.")
