name = (input("Enter the string: "))
vcount = 0
concount= 0
for letter in name:
    if letter  in "aeiou":
        vcount = vcount + 1
    else:
        concount = concount + 1
print("Vowels:", vcount)
print("Consonants:", concount)