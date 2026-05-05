# 1. Liste de nombres 
chiffres = [1, 2, 3, 4, 5,10,15,20,30]

# 2. Boucle for : parcourir la liste 
print("Nombres dans la liste :")
for nb in chiffres:
    print(nb)

3. Calculer la somme avec une boucle 
somme = 0
for nb in chiffres: 
        somme = somme + nb 
        print("Somme totale : ", somme)

# 4. Conditions à l'intérieur de la boucle 
print("Nombres pairs :")
for nb in chiffres: 
    if nb % 2 == 0:
        print(nb, "est pair")