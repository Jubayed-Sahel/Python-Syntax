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
