def average(a,b,c):
    result = (a+b+c)/3.0
    return print(f"Result = {result}")             # Print can be used too

def sum(a,b):
    return a+b


average(2,4,3)

ans = sum(2,8)
print(f"Sum = {ans}")





# Default Argument - ******
def work (a,b,plus=0):                     # Passing the value of "Plus" is optional now
    ans = a+b+plus
    return ans

c = work(1,2)
d = work(1,2,2)
print(f"c={c}")
print(f"d={d}")




# Keyword argumument
res = sum (b=1,a=2)
print(f"result = {res}")