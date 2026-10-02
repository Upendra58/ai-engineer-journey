
text = "hello"
count= {}
for letter in text:
    if letter in count:
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1
for key, value in count.items():
    print(key,":",value)
