"""
Use these exercises to strengthen your understanding of strings and become
confident in manipulating them.


1. Basic String Operations : 
Create a string variable name with your full name. 
Print:
The first character
The last character
The length of the string

Concatenate two strings: "Hello" and "World" with a space in between.





2. String Slicing and Indexing
Given text = "Python Programming" ,
do the following:
Print the first 6 characters
Print the last 6 characters
Print every second character from the string
Reverse the string text using slicing.



3. String Methods and Functions
Take the string " i love python programming " and:
Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
Check if the string "123abc" is alphanumeric.




4. String Formatting and f-Strings
Using format() , create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

Do the same using f-strings.




5. String Manipulation Challenges
Given sentence = "Coding in Python is fun" , replace "fun" with
"awesome" and print it.
Find the index of the word "Python" in sentence .
Convert the entire sentence to uppercase and print it.




6. Bonus Questions
Write a program that counts how many vowels are in a given string.

Take a user input string and check if it is a palindrome (same forwards and
backwards).


"""


# 1. Basic String Operations
name = "harry"
print(name[0])  # First character
print(name[-1])  # Last character   
print(len(name))  # Length of the string

greeting = "Hello" + " " + "World"
print(greeting) 
print("\n \n \n")


# 2. String Slicing and Indexing
text = "Python Programming" 
print(text[:6])  # First 6 characters
print(text[-6:])  # Last 6 characters
print(text[::2])  # print every second character 
print(text[::-1]) # Reverse the string using slicing
print("\n\n\n")


# 3. String Methods and Functions
text2 = " i love python programming "
print(text2.strip())  # Remove extra spaces from both ends 
print(text2.title())  # Convert the string intpo title case 
print(text.count("o")) # Count how how many times a character is given

text3 = "123abc"
print(text3.isalpha())  # Check if the string is alphanumeric or not
print("\n\n\n")


# 4. String Formatting & f-strings
test = "my name is {} and i am {} years old"
a1 = "John"
a2 = 25
print(test.format(a1,a2))    # Using Formatting
print("my name is {} and i am {} years old".format(a1,a2))     # Another way of using formatting

print(f"my name is {a1} and i am {a2} years old")   # Using f-string
print("\n\n\n")




# 5.String Manipulation Chellenges
sentence = "Coding in python is fun"
print(sentence.replace("fun","awesome"))    # Replace "fun" with "awesome"
print(sentence.index("python"))             # Finding the index
upperCasing = sentence.upper()
print(upperCasing)                          # Convert in Upper Case
print("\n\n\n")



# 6. Bonus Question 1 
sentence2 = "Coding in python is fun"
sum = 0
vowels = ['a','e','i','o','u']

for word in sentence2.lower():
    if (word in vowels):
        sum += 1

print(f"total vowels = {sum}")
print("\n\n")


# 6. Bonus Question 2 
check101=input("Enter a string : ")
if (check101 == check101[::-1]):
    print("The string is a palindrome")     
else:
    print("The string is not a palindrome")

    