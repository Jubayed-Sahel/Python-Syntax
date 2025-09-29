
'''

 Two types of modules in python 
    1. Built in Modules 
    2. Externel Modules   (My Module.py)

 '''


# Now we can use math module/Library (Built in modules)
import math
import os                           # Color change bcz i didnt use it
print(math.sqrt(16))



# Written in diff file (External Modules)
import My_Module                      
My_Module.Greet(2221173)



'''

import requests                           # in terminal : pip install request
r = requests.get("https://www.google.com")
print(r.text)

'''