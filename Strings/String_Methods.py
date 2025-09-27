

# String Are Immutable
s = "sahel ahmed"     
#s[0] = "R"     # Can not Do This

a=len(s)                     # find length of the string
print(a)  
print()


print(s.upper() , s)         # original 's' is not change , as string is immutable
print(s.lower() )
print(s.capitalize() )       # Capitalize only the first character
print(s.title())             # each word er first letter capitalize
print()

text = "Python is Fun"
print(text.find("is"))                   # output: 7
print(text.replace("is", "was"))         # Replace word
print()


text1= "apple,banana,mango"
print(text1.split(","))                           # Split by comma and make a LIST
print(",".join(['apple', 'banana', 'mango']))     # join by comma and make a string
print()
print()


text3="Python123"
print(text3.isalpha())       #false
print(text3.isdigit())       #false
print(text3.isspace())       #false (Have space or not)
print(text3.isalnum())       # true (alphabet and numeric)
