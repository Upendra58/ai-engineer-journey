\---



\# 📄 DAY-04.md



```markdown

\# 🐍 Day 4 — Python Lists \& Data Problem Solving



\## 📅 Date



September 27, 2026



\## 🎯 Day 4 Goal



Move from loops and strings into Python lists and start solving more realistic data-processing problems.



The main focus was:



```text

List

&#x20;↓

Loop

&#x20;↓

Condition

&#x20;↓

Calculation / Transformation

&#x20;↓

Result

📚 Topics Learned

Lists

List indexing

Zero-based indexing

Updating list elements

append()

remove()

Looping through lists

Counters

Accumulators

Finding largest values

Finding smallest values

Average calculation

Filtering lists

Transforming list values

Removing duplicates

Tracking multiple values

Finding second-largest values

1️⃣ Creating a List



Example:



numbers = \[1, 2, 3, 4, 5]



Lists can contain multiple values.



2️⃣ List Indexing



Python uses zero-based indexing.



Index:   0   1   2   3   4

Value:   1   2   3   4   5



Example:



numbers = \[1, 2, 3, 4, 5]



print(numbers\[0])

print(numbers\[2])

print(numbers\[4])



Output:



1

3

5

Key rule



The first element is:



numbers\[0]



not:



numbers\[1]

3️⃣ Modifying a List



List elements can be changed using their index.



numbers = \[1, 2, 3, 4, 5]



numbers\[2] = 30



print(numbers)



Result:



\[1, 2, 30, 4, 5]



General pattern:



list\[index] = new\_value

4️⃣ append()



Used to add an element to the end of a list.



numbers = \[1, 2, 3, 4, 5]



numbers.append(6)

numbers.append(7)



print(numbers)



Output:



\[1, 2, 3, 4, 5, 6, 7]

5️⃣ remove()



Used to remove a value from a list.



numbers = \[1, 2, 3, 4, 5]



numbers.remove(3)



print(numbers)



numbers.append(6)



print(numbers)



Output:



\[1, 2, 4, 5]

\[1, 2, 4, 5, 6]

Important distinction

numbers.remove(3)



means:



Remove the value 3.



Whereas:



numbers\[2]



means:



Access the element at index 2.



6️⃣ Loop Through a List



Instead of using range(), a list can be looped through directly.



numbers = \[1, 2, 3, 4, 5]



for number in numbers:

&#x20;   print(number)



This means:



For each number inside the list, perform the operation.



7️⃣ Count Even Numbers

numbers = \[1,2,3,4,5,6,7,8,9,10]



count = 0



for number in numbers:

&#x20;   if number % 2 == 0:

&#x20;       count = count + 1



print(count)



Output:



5

Pattern

List

&#x20;↓

for

&#x20;↓

if

&#x20;↓

counter

8️⃣ Sum a List

numbers = \[1,2,3,4,5,6,7,8,9,10]



total = 0



for number in numbers:

&#x20;   total = total + number



print(total)



Output:



55

Important naming lesson



Instead of:



count = 0



when storing a sum, a clearer name is:



total = 0

9️⃣ Find Largest Number

numbers = \[1,2,3,4,50,6,7,8,9,10]



largest = numbers\[0]



for number in numbers:

&#x20;   if number > largest:

&#x20;       largest = number



print(largest)



Output:



50

Important insight



Instead of assuming:



largest = 0



we use:



largest = numbers\[0]



This also works when the list contains negative numbers.



🔟 Find Smallest Number

numbers = \[1,2,3,4,50,6,7,8,9,10]



smallest = numbers\[0]



for number in numbers:

&#x20;   if number < smallest:

&#x20;       smallest = number



print(smallest)



Output:



1

1️⃣1️⃣ Average of a List



Practiced calculating an average without using sum() or len().



numbers = \[1,2,3,4,5,6,7,8,9,10]



total = 0

count = 0



for number in numbers:

&#x20;   count = count + 1

&#x20;   total = total + number



average = total / count



print(count)

print(total)

print(average)



Output:



10

55

5.5

Lesson



Inside the loop:



Collect information.



After the loop:



Calculate the final result.



1️⃣2️⃣ Filter a List



Created a new list containing only even numbers.



numbers = \[1,2,3,4,5,6,7,8,9,10]



new = \[]



for number in numbers:

&#x20;   if number % 2 == 0:

&#x20;       new.append(number)



print(new)



Output:



\[2, 4, 6, 8, 10]

🐛 Important append() Lesson



Initially attempted:



new = new.append(number)



This is incorrect.



Correct:



new.append(number)

Why?



append() changes the list directly.



It does not return the updated list.



Therefore:



new = new.append(number)



would make new become None.



1️⃣3️⃣ Filter + Transform



Practiced creating a new list containing squares of even numbers.



Concept:



Original number

&#x20;     ↓

Is it even?

&#x20;     ↓

&#x20;  YES

&#x20;     ↓

Square it

&#x20;     ↓

Append to new list



Example:



numbers = \[1, 2, 3, 4, 5, 6]



result = \[]



for number in numbers:

&#x20;   if number % 2 == 0:

&#x20;       result.append(number \* number)



print(result)



Output:



\[4, 16, 36]

1️⃣4️⃣ Remove Duplicates



Problem:



numbers = \[1,2,2,1,4,9,10,4,6,74,4,66,3,56,33,44,66,3,4,5,6,7,8,9,10]



Created a new list containing only unique values.



new = \[]



for number in numbers:

&#x20;   if number not in new:

&#x20;       new.append(number)



print(new)

Logic

Is number already in new?

&#x20;      ↓

&#x20;   YES → ignore

&#x20;   NO  → append



This introduced a basic data-processing pattern.



1️⃣5️⃣ Largest + Second Largest



Practiced tracking multiple values while iterating.



Example:



numbers = \[1,2,2,1,4,9,10,4,6,74,4,66,3,56,33,44,66,3,4,5,6,7,8,9,10]



largest = numbers\[0]

secondl = numbers\[0]



for number in numbers:



&#x20;   if number > largest:

&#x20;       secondl = largest

&#x20;       largest = number



&#x20;   elif number > secondl and number < largest:

&#x20;       secondl = number



print(largest)

print(secondl)



Output:



74

66

Core idea



Maintain two pieces of state:



largest

second-largest



When a new largest appears:



old largest → second-largest

new number  → largest



When a number is between the two:



number → second-largest

🧠 Day 4 Problem-Solving Pattern



A major focus was learning to think in terms of:



INPUT DATA

&#x20;   ↓

INITIAL STATE

&#x20;   ↓

LOOP

&#x20;   ↓

CHECK CONDITION

&#x20;   ↓

UPDATE STATE

&#x20;   ↓

FINAL RESULT



This is the beginning of algorithmic thinking.



🧪 Day 4 Mini Test



Input:



numbers = \[12, 7, 25, 7, 18, 30, 4, 25, 9, 16]



The final program independently calculated:



Largest

Smallest

Total

Even count

Unique values



Final results:



Largest: 30

Smallest: 4

Sum: 153

Even count: 6

Unique: \[12, 7, 25, 18, 30, 4, 9, 16]

📊 Day 4 Assessment

Strengths

Can create and manipulate lists

Understands zero-based indexing

Can update list elements

Can add and remove values

Can loop through lists

Can use counters

Can use accumulators

Can filter data

Can transform data

Can find largest and smallest values

Can remove duplicates using basic logic

Can maintain multiple pieces of state

Can combine multiple list operations into one program

Current Gap



Need more practice with:



Edge cases

Robust initialization

More complex list algorithms

Time and space complexity

Independent problem decomposition



These will be introduced gradually during DSA.



✅ Definition of Done

&#x20;Lists

&#x20;Indexing

&#x20;Updating elements

&#x20;append()

&#x20;remove()

&#x20;Looping through lists

&#x20;Counters

&#x20;Accumulators

&#x20;Largest

&#x20;Smallest

&#x20;Average

&#x20;Filtering

&#x20;Transformation

&#x20;Duplicate removal

&#x20;Second-largest logic

&#x20;Independent mini test

