with open("notes.txt", "w") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")

with open("notes.txt", "r") as f:
        print(f.read())
