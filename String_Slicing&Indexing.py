name = "Sahel123456"

# Slicing With Positive indices
print(name[0:3])     # 0 to 2
print()

# Slicing With Negative Indices
print(name[2:-1])    # Same as [2:4]
print()

# print(name[0:10:n])    #Same as skip n-1 character
print(name[0:10:1])    #Same as skip 0 character
print(name[0:10:2])    #Same as skip 2-1=1 character
print(name[0:10:3])    #Same as skip 3-1=2 character
print()
print()

print(name[:5])   #Replace The first number with 0  --  name[0:4]
print(name[0:])   #Replace the empty number with length   -- name[0:11]