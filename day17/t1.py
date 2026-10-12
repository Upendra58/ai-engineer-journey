with open("test.txt", "w") as file:
    file.write("Python\n")
    file.write("AI Engineer\n")
    file.write("Production Ready\n")
with open("test.txt", "r") as file:
    content = file.read()
    print(content)