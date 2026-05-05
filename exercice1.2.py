Prénom = "Thomas"
Age = 24
Ville = "Genève"
Profession = "Data Engineer"
Salaire_mensuel = 8000

Salaire_annuel = Salaire_mensuel * 12
print("Salaire annuel :", Salaire_annuel, "CHF")
Message = Prénom + " habite à " + Ville + " travaille en tant que " + Profession
print(Message)

if Age >= 18: 
    print("Majeur")
else:
    print("Mineur")