📄 DAY-02.md

\# 🐍 Day 2 — Python Coding Foundations \& Problem Solving



\## 📅 Date



September 25, 2026



\## 🎯 Day 2 Goal



Move from recognizing Python syntax to writing small Python programs independently.



The main focus was understanding how to translate a simple problem statement into:



```text

Input → Process → Logic → Output

📚 Topics Learned

Variables

Values and data types

Strings

Integers

print()

input()

Type conversion using int()

f-strings

Comparison operators

if

if / else

if / elif / else

Basic calculations

while loops

Incrementing variables

Basic debugging

1️⃣ Variables



Started with basic variables.



name = "Upendra"

age = 25



print(name)

print(age)

Key idea



A variable is a name used to store a value.



name → "Upendra"

age  → 25

2️⃣ f-Strings



Learned how to insert variables into text.



name = "Upendra"

age = 25

role = "AI Engineer"



print(f"I am {name}, age {age}, and dreaming to become {role}")

Key idea



Use f before the string:



f"..."



and put variables inside:



{variable}

3️⃣ User Input



Learned how to take input from the user.



name = input("What is your name? ")

age = input("What is your age? ")

role = input("What is your role? ")



print(f"I am {name}, age {age}, and dreaming to become {role}")

Important



input() returns a string.



Therefore, numeric input needs conversion.



4️⃣ Type Conversion



Learned how to convert input into an integer.



age = int(input("What is your age? "))



next\_age = age + 1



print(f"Next year you will be {next\_age}")

Key idea

int("25")



converts the string "25" into the integer 25.



5️⃣ if / else



Practiced decision-making.



age = int(input("What is your age? "))



if age >= 18:

&#x20;   print("You are an adult")

else:

&#x20;   print("You are a minor")

Mental model

Condition

&#x20;  ↓

True  → if block

False → else block

6️⃣ if / elif / else



Learned how to handle multiple conditions.



Example:



number = int(input("Enter a number: "))



if number > 0:

&#x20;   print(f"{number} is positive")

elif number < 0:

&#x20;   print(f"{number} is negative")

else:

&#x20;   print(f"{number} is zero")

🐛 Debugging Lesson — Zero Condition



Initially used:



if number >= 0:



This caused a logical problem because zero was already included in the first condition.



Correct logic:



if number > 0:

&#x20;   # positive

elif number < 0:

&#x20;   # negative

else:

&#x20;   # zero

Lesson



Always check whether later conditions are actually reachable.



7️⃣ Electricity Bill Problem



Practiced combining input, conditions and calculations.



Rules:



0–100 units    → ₹2 per unit

101–200 units  → ₹3 per unit

Above 200      → ₹5 per unit



Code:



units = int(input("Enter the units: "))

charge = 0



if units <= 100:

&#x20;   charge = units \* 2

elif units <= 200:

&#x20;   charge = units \* 3

else:

&#x20;   charge = units \* 5



print(f"Total charge is {charge} rupees")

What this taught



A problem can be broken into:



Input

&#x20;↓

Check condition

&#x20;↓

Calculate

&#x20;↓

Output

8️⃣ while Loop



Learned how to repeat a block of code while a condition remains true.



n = int(input("Enter the number: "))



i = 1



while i <= n:

&#x20;   print(i)

&#x20;   i += 1



For input:



5



Output:



1

2

3

4

5

🐛 Important while Loop Lessons

i + 1 does not update i



This:



i + 1



only calculates a value.



It does not change i.



Correct:



i += 1



or:



i = i + 1

Python does not use i++



Unlike some other languages, Python uses:



i += 1

🧠 Problem-Solving Lessons



The most important lesson from Day 2 was learning to translate a problem into smaller steps.



For example:



Problem

&#x20;  ↓

What is the input?

&#x20;  ↓

What calculation/logic is required?

&#x20;  ↓

What conditions are needed?

&#x20;  ↓

What should be printed?

📊 Day 2 Assessment

Strengths

Can write basic Python independently

Can use variables

Can take user input

Can convert input types

Can use conditions

Can perform basic calculations

Can write simple while loops

Can identify basic logic mistakes

Can fix code after debugging

Current Gap



Need more practice converting unfamiliar problem statements into code without hints.



✅ Definition of Done

&#x20;Variables

&#x20;Strings

&#x20;Integers

&#x20;print()

&#x20;input()

&#x20;int()

&#x20;f-strings

&#x20;if / else

&#x20;if / elif / else

&#x20;Basic calculations

&#x20;while loops

&#x20;Basic debugging

&#x20;Problem decomposition

🚀 Next Step



Move into:



for loops

counters

accumulators

strings

lists

more independent problem solving

🏁 Status



DAY 2 — COMPLETE ✅

