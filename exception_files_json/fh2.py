with open("notes.txt","r") as file:
    content = file.read()
    for line in file:
        print(line.strip())