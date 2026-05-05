crypto1 = input("Nom de la crypto 1 : ")
quantite1 = float(input("Quantité : ") ) 
prix1 = float(input("Prix actuel en $ : "))

crypto2 = input("Nom de la crypto 2 : ")
quantite2 = float(input("Quantité : "))
prix2 = float(input("Prix actuel en $ : "))

crypto3 = input("Nom de la crypto 3 : ")
quantite3 = float(input("Quantité : "))
prix3 = float(input("Prix actuel en $ : "))

valeur1 = quantite1 * prix1 
valeur2 = quantite2 * prix2
valeur3 = quantite3 * prix3 

total = valeur1 + valeur2 + valeur3 

print("--Mon Wallet--")
print(f"{crypto1} : {quantite1} x {prix1}$ = {valeur1}$")
print(f"{crypto2} : {quantite2} x {prix2}$ = {valeur2}$")
print(f"{crypto3} : {quantite3} x {prix3}$ = {valeur3}$")
print("----------------")
print(f"Total : {total}$")
