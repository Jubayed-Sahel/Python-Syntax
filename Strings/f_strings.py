# String Fromatting 
template = "dear {} please take the {}$ Bag"
n1 = 'sahel'
a1 = 10000
n2 = 'sifat'
a2 = 5000



# Way 1 (Old way)
result = template.format(n1,a1)
print(result)

print()
# Way 2 (New way)    ---- *** important ***
print(f"dear {n2} please take the {a2}$ Bag")





pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")


x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")