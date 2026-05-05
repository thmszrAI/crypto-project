with open ("note.txt","w") as f:
    f.write("Première ligne:\n")
    f.write("Deuxième ligne:\n")

    with open("note.txt", "r") as f:
        print(f.read())