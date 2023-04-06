ingredient = {}
ingredient["sandwish"] = "le jambon, " "le pain, " "fromage, " "tomates, "
ingredient["gateau"] = " la farine, " "le sucre, " "et" "les œufs, "
ingredient["salade"] = "l’avocat,"  "la roquette," "les tomates, " "et" "les épinards"

repas = {}
repas["sandwish"] = "un déjeuner "
repas["gateau"] = "un dessert "
repas["salade"] = "un dejeuner"

prep_time = {}
prep_time["sandwish"] = "10 min"
prep_time["gateau"]= "60 min"
prep_time["salade"] = "15 min"



for cle, valeur in ingredient.items():
    print("les ingrédients de",cle,"sont:" ,valeur)
for cle, valeur in repas.items():
     print(cle,"est :" ,valeur)
for cle, valeur in prep_time.items():
     print("le temps necessaire pour preparer",cle,"est",valeur )



def noms_de_recette(cle):  
    print(valeur)
    return
print("Entrez le nom de repas",cle)
cle = input(ingredient )

