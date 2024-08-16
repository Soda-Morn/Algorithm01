# Ex01
# string
# Enter text and display it one by one
text = input("Enters your letter: ")
for i in range(len(text)):
    print(text[i])

# Ex02
# String
# Enter text and display number of letter
text = input("Enters your letter: ")
for i in range(len(text)):
    print(i)

# EX03
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter

text = input("Enters your letter: ")
result = "No"
for i in range(len(text)):
    if text[i].upper() == text[i] :
        result = "Yes"
print(result)

# Ex04
# Wee hav text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

text = input("Enter your number here : ")
result = 0
letter = ""
for i in range(len(text)):
    if text[i] == " ":
        letter += ""
    else:
        letter += text[i]
        result += int(text[i])
print(letter)
print("Total :",result)


# Ex05
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 

# Q1
text = input("Enter your number here : ")
odd_count = 0
even_count = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Odd count:", odd_count)
print("Even count:", even_count)

# Q2
text = input("Enter your number here : ")
sum = 0
for i in range(len(text)):
    sum += int(text[i])
print(sum)

# Q3
text = input("Enter your number here : ")
sum_even = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        sum_even += int(text[i])
print(sum_even)

# Q4
text = input("Enter your number here : ")
lastindex = len(text) - 1
result = ""
for i in range(len(text)):
    result += text[lastindex-i]
print(result)

# Ex06
num = int(input("Enters your number here: "))
if num % 2 == 1:
    print("Odd")
else:
    print("Even")

# Ex07
isfound_num = False
while not isfound_num:
    num=int(input("Enters your number: "))
    if num >=10 and num <=20:
        print("Continue")
    else:
        isfound_num=True
print("Out of range")

# Ex08
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8

# Q1
text = "9394884039"
count = 0
for i in range(len(text)):
    if text[i] == "8":
        count += 1
print(count)

# Q2
text = "9394884039"
isfound = False
index = 0
while not isfound:
    if text[index]=="8":
        print(index)
        isfound=True
    index+=1

# Ex09
string = "3 4 5 6"
result = " "
total = " "
i = 0
while i < len(string):
    cha = string[i]
    if cha != " ":
        result += cha
        total += str(int(cha) * 2) + " "
    i += 1
print(result)  
print(total)


# Ex10
min = 0
max = 0
for i in range(5):
    num = int(input("Enters your num: "))
    if min == 0 and min == 0:
        min = num
        max = num
    else:
        if num > max:
            max = num
        elif min > num:
            min = num
print("Min",min)
print("Max",max)