def inverser_chaine(chaine):
    return chaine[::-1]

chaine = "Bonjour Merveille!"
chaine_inverse = inverser_chaine(chaine)
print(chaine_inverse)


def reverse_strings(chaine):
    # Diviser la chaîne en une liste de mots
    words = chaine.split()
    
    # Inverser chaque mot et les rejoindre avec des espaces
    reversed_words = " ".join(word[::-1] for word in words)
    
    # Retourner la chaîne inversée
    return reversed_words

chaine = "bonjour" " " "petite" " " "Merveille"
chaine_inverse =  reverse_strings(chaine)
print(chaine_inverse)

def inverser_chaine(chaine):
    return 0
chaine = ""
chaine_inverse = inverser_chaine(chaine)
print(chaine_inverse)


