# Function to count vowels in a string
def count_vowel(text):
    count = 0
    for letter in text:
        # if we use if letter in "aeiou": it only checks a,e,i,o,u (case sensitive) if text given as Upendra, the U comes as false
        # so we use lower to convert all to lower
        if letter.lower() in "aeiou":
            count= count+1
    return count
text = "Upendra"
print(count_vowel(text))