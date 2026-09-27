\# 📄 DAY-03.md



```markdown

\# 🐍 Day 3 — Python Loops, Strings \& Problem Solving



\## 📅 Date



September 26, 2026



\## 🎯 Day 3 Goal



Move from basic Python syntax into actual problem solving using:



\- while loops

\- for loops

\- conditions

\- counters

\- accumulators

\- strings



The main focus was learning to write code independently and debug mistakes.



\---



\# 📚 Topics Learned



\- while loops

\- for loops

\- range()

\- Counters

\- Accumulators

\- Loop + condition combinations

\- Strings

\- Iterating through strings

\- Character counting

\- Vowel counting

\- String reversal

\- Palindrome checking

\- Debugging

\- Indentation

\- Translating problems into algorithms



\---



\# 1️⃣ Sum Numbers from 1 to N



Problem:



Find the sum:



```text

1 + 2 + 3 + ... + N



Solution:



n = int(input("Enter the number: "))



total = 0

i = 1



while i <= n:

&#x20;   total = total + i

&#x20;   i = i + 1



print(total)

Key lesson



total is an accumulator.



total = total + i



stores the running result.



2️⃣ Count Even Numbers



Problem:



Count how many even numbers exist between 1 and N.



n = int(input("Enter the number: "))



i = 1

count = 0



while i <= n:

&#x20;   if i % 2 == 0:

&#x20;       count = count + 1



&#x20;   i += 1



print(count)

Important debugging lesson



Initially, the increment was placed inside the if.



That caused a problem when i was odd because i stopped changing.



Correct:



if i % 2 == 0:

&#x20;   count += 1



i += 1



The loop-control update must happen every iteration.



3️⃣ Sum Even Numbers

n = int(input("Enter the number: "))



i = 1

even\_sum = 0



while i <= n:

&#x20;   if i % 2 == 0:

&#x20;       even\_sum = even\_sum + i



&#x20;   i += 1



print(even\_sum)

4️⃣ Reverse Numbers



Problem:



Print numbers from N down to 1.



n = int(input("Enter the number: "))



i = n



while i >= 1:

&#x20;   print(i)

&#x20;   i -= 1



Example:



Input: 5



Output:

5

4

3

2

1

🔁 for Loops



Learned the basic for loop.



for i in range(1, 6):

&#x20;   print(i)



Output:



1

2

3

4

5

🧠 Understanding range()



Important rule:



range(start, stop)



includes:



start



but excludes:



stop



Therefore:



range(1, 6)



produces:



1 2 3 4 5

🔽 Descending range



Learned how to count backwards.



for i in range(5, 0, -1):

&#x20;   print(i)



Output:



5

4

3

2

1

5️⃣ Sum Using for Loop

total = 0



for i in range(1, 6):

&#x20;   total = total + i



print(total)

6️⃣ Count Even Numbers Using for Loop

count = 0



for i in range(1, 11):

&#x20;   if i % 2 == 0:

&#x20;       count = count + 1



print(count)

7️⃣ Sum Odd Numbers

n = int(input("Enter the number: "))



total = 0



for i in range(1, n + 1):

&#x20;   if i % 2 != 0:

&#x20;       total = total + i



print(total)

🔤 Strings



Learned that strings can be iterated character by character.



name = "Upendra"



for letter in name:

&#x20;   print(letter)



Output:



U

p

e

n

d

r

a

8️⃣ Count Characters Without len()

name = input("Enter the string: ")



count = 0



for letter in name:

&#x20;   count = count + 1



print(count)



This helped understand that len() is essentially answering a question that we can also solve manually using a counter.



9️⃣ Count Vowels

name = input("Enter the string: ")



count = 0



for letter in name:

&#x20;   if letter in "aeiou":

&#x20;       count = count + 1



print(count)

Key lesson



Instead of:



if letter == "a" or letter == "e" ...



Python allows:



if letter in "aeiou":

🔄 Reverse a String



Learned how to construct a reversed string.



Example:



cat



Process:



c → c

a → ac

t → tac



Code:



name = input("Enter the string: ")



reverse = ""



for letter in name:

&#x20;   reverse = letter + reverse



print(reverse)

🔍 Palindrome



A palindrome reads the same forwards and backwards.



Example:



madam



Solution:



name = input("Enter the string: ")



reverse = ""



for letter in name:

&#x20;   reverse = letter + reverse



if reverse == name:

&#x20;   print("palindrome")

else:

&#x20;   print("not palindrome")

Important lesson



The comparison should happen after building the complete reverse.



🔤 Vowels and Consonants



Practiced counting vowels and consonants.



name = input("Enter the string: ")



vcount = 0

concount = 0



for letter in name:

&#x20;   if letter in "aeiou":

&#x20;       vcount = vcount + 1

&#x20;   else:

&#x20;       concount = concount + 1



print("Vowels:", vcount)

print("Consonants:", concount)

🐛 Debugging Lessons

1\. i + 1 does not update i



Wrong:



i + 1



Correct:



i += 1

2\. Loop indentation matters



Code that belongs inside a loop must be indented.



3\. range() excludes the stop value

range(1, 5)



produces:



1 2 3 4



not 5.



4\. Build before comparing



For palindrome:



Build reverse

&#x20;    ↓

Finish loop

&#x20;    ↓

Compare reverse with original

🧠 Day 3 Assessment



I can now:



Write while loops

Write for loops

Use range()

Use counters

Use accumulators

Combine loops with conditions

Iterate through strings

Count characters

Count vowels

Reverse strings

Check palindromes

Debug basic loop mistakes

Translate simple problems into code

🚧 Current Gap



The main area that still needs practice is:



Converting an unfamiliar problem statement into code independently.



This will be addressed continuously through small coding problems.



✅ Definition of Done

&#x20;while loops

&#x20;for loops

&#x20;range()

&#x20;Counters

&#x20;Accumulators

&#x20;Loop + condition

&#x20;String iteration

&#x20;Character counting

&#x20;Vowel counting

&#x20;String reversal

&#x20;Palindrome checking

&#x20;Debugging

🏁 Status



DAY 3 — COMPLETE ✅

