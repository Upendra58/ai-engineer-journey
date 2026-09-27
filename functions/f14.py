def is_vowel(letter):
    if letter.lower()in "aeiou":
        return True
    else:
        return False

def count_vowel(text):
    count = 0
    for letter  in text:
        if is_vowel(letter):
            count= count+1
    return count
text = "Upendra"
print(count_vowel(text))