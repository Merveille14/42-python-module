import sys

def calculate(a, b):
    # Vérifie que les arguments sont des entiers
    if not isinstance(a, int) or not isinstance(b, int):
        print("Erreur : Les arguments doivent être des entiers.")
        return
    
# Calcule et imprime les résultats
a = input( "Entrez le premier nombre : " )
b = input("Entrez le second nombre : ")
print("Somme:", a + b)
print("Différence:", a - b)
print("Produit:", a * b)
if b != 0:
   print("Quotient:", a / b)
   print("Reste:", a % b)
else:
   print("Erreur : division par zéro.") 

# Vérifie le nombre d'arguments fournis
if len(sys.argv) != 3:
   print("Erreur : Deux arguments entiers sont nécessaires.")
else:
# Essaie de convertir les arguments en entiers
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        calculate(a, b)
    except ValueError:
        print("Erreur : Les arguments doivent être des entiers.")
