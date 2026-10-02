text = "python is easy and python is powerful and python will be  fun"
words = text.split()
count = {}
rep_word = ""
high_count = 0
for word in words:
    if word in count:
        count[word] = count[word]+ 1
    else:
        count[word] = 1
    if count[word] > high_count:
        high_count = count[word]
        rep_word = word
print(rep_word, ":", high_count)
