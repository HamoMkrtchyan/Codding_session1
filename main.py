# ----1----

string = "cat"
variants = []

for i in range(len(string)):
    variant = string[:i] + string[i].upper() + string[i + 1:]
    variants.append(variant)
print('1 - ' ,variants)

# ----2----

x1 = 'problem'  # str(input('enter first string'))
x2 = 'problim'  # str(input('enter second string'))
l1 = x1.split()
l2 = x2.split()

if len(x1) == len(x2):
    for i in x1:
        if i not in x2:
            print('2 - ', i)
else:
    print('2 - ', -1)


# ----3----
def find_string_index(string1, string2):
    index = string1.find(string2)
    return index


string1 = 'HelloWorld'
string2 = 'World'
index = find_string_index(string1, string2)
print('3 - ', index)


# ----4----

def strMove(string, number, bool):
    if bool:
        shifted = string[number:] + string[:number]
    else:
        shifted = string[number:] + " " * number
    return shifted


string = "hello"
number = 3
bool = True
result = strMove(string, number, bool)
print('4 - ' , result)

# ----5----

nums = [1, 3, 5, 6]
x = 3

def init():
    if x in nums:
        ip = nums.index(x)
        return ip
    else:
        nums.append(x)
        ip = nums.index(x)
    return ip

ip = nums.index(x)
print('5 - ' , ip)



#----6----





#----7----

import re

password = input("7 - Enter your password: ")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$])[A-Za-z\d!@#$%^&*]{6,16}$"

if re.match(pattern, password):
    print("7 - ", "Password is valid")
else:
    print("7 - ", "Password is invalid")
