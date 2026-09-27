# Function to count vowels in a string
def count_letter(text):
    vowelcount = 0
    concount = 0
    for letter in text:
        # if we use if letter in "aeiou": it only checks a,e,i,o,u (case sensitive) if text given as Upendra, the U comes as false
        # so we use lower to convert all to lower
        if letter.lower() in "aeiou":
            vowelcount= vowelcount+1
        else:
            concount = concount +1
    return (vowelcount, concount)

text = "Upendra"
print(count_letter(text))