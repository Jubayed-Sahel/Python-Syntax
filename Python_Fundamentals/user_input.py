user_num = input("Enter Number: ")
print(user_num)             #  is string
print(type(user_num))

user_num = int(user_num)    # Now its a integer
print(type(user_num))


print("Tell me your name")
nameByUser = input()        # By Default its int
print(type(user_num))





#   ******* Another example *********

a = input("Enter Num 1 : ")
a = int(a)             #typecast
b = int(input("Enter Num 1 : "))  #typecast in a single line

print(a+b)