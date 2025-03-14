import numpy as np
import sys
import random

msg = "Roll a dice!"
# print(msg)

# print(np.random.randint(1,9))
# print(sys.version)
""" this is multi-line comment """
if (5>7):
    print('5 is greater than 2')
else:
    print('5 is not greater than 2')

isLoggedIn = False
if(isLoggedIn ):
    print('Welcome User')
else: 
    print('Please loggin first')

# variables
a = int(4)
dec = float(3.6)
a= "four"
print(type(a),type(msg))
print(dec)
principal,rate,time = 200,0.5,6
print(principal,rate,time)
Names = ['Amaid',"Chile"]
firstName,lastName = Names
print(firstName,lastName)
print("one"+" 1")

user = 'Amadi Chile';

def greetUser():
    # global user
    user = 'Amadi John'
    global userId
    userId = '444acd'
    print('User is: '+user)

greetUser()
print('User is: '+user)
print('UserId is: '+userId)
print(7e100)
print(3j)
print(float(1))
print(int(1.5))
# print(float(5j))
# print(int(5j))
print(complex(12))
print(random.randrange(1,1000))
print(""" This is 
      a multiline string
       """)
jd = "Consider's son!"
print(jd[0])

for item in jd:
    print(item)
# check for a value in  a string using in or not in
print(len(jd))
print('son' in jd)
print('chile' not in jd)
print(jd[0:5])
print(jd.upper())
print(jd.strip())
print(jd.replace('son',"boy"))
print(jd.split(' ')[0])
print(jd.count("s"))
print(f"{jd} is 3 years old")
price = 99
print(f'The price of 150w solar panel is {price:.5f} dollars today')
print('It is written, you \"must\" love your neighbour as yourself \t chile \t amadi')
print(bool('Chile'))
print(bool(15))
print(bool(0.5))

def rBool(a,b):
    return a>b
if(rBool(14,5)):
    print('a is greater than b')
else:
    print('b is greater than a')

print(isinstance(isLoggedIn,bool))
t=5
t |= 7
print(t)
print(14>5 and 6>3)
print(4>5 or 6>23)
print(12|4)
print(100 * 5+3)
print(5+4 - 7+3)
# python list are like javascript arrays
ages = [33,930,969,950]
agesNames =['Jesus',"Adam","Methuselah","Noah"]
print(ages)
print(len(ages))
print(ages[1:3])
ageSearch = 400
# if ageSearch in ages: 
#     print(f'The age of {agesNames[ages.index(ageSearch)]} is in ages array')
# else: 
#     print(f'{ageSearch} not in ages array')
# print(agesNames[ages.index(ageSearch)])
ages[1:3]=[940,979]
ages.insert(0,55)
ages.append("victor")
ages.extend(agesNames)
ages.remove('victor')
ages.pop(2)
# ages.clear()
# del ages
print(ages) 
print(agesNames)
print(agesNames.remove('Noah'))
print(agesNames)
print(range(4))
print(len(agesNames))

for  i in range(6):
    print('i = ',i

)
# List Comprehension
myFruits = ["apple","Grape","Banana","Orange"];
# newFruits = [fruit for fruit in myFruits if "a" in fruit.lower()]

# for fruit in myFruits:
#     if "a" in fruit.lower():
#         newFruits.append(fruit)

# print(newFruits);

# for x in range(5,10):
#     print(x)

# sort list
digits = [100,1,0,5,500,20,1,11,1,2,100,100]
def fifty(n):
    return abs(n-50)
myFruits.sort(key=str.lower)
print(myFruits);
digits.sort(key=fifty)
digits.reverse();
print(digits)
# copy list
newDigits = digits.copy()
newDigits.extend([33,66,77,99])
print(newDigits)
newFruits = list(myFruits)
print(newFruits)
newDigits2 = newDigits[:]
print(newDigits2)
# join list
twoList = newDigits2 + newDigits
print(f'from {twoList}')
# remove duplicates from a list
def removeDuplicates_Method1(a):
    a=list(a)
    a.sort()
    index = 0
    notFound=True
    while(notFound):
                try:
                        # remove all occurance except one. 
                        counts = a.count(a[index])
                        while(counts > 1):
                            a.remove(a[index])
                            counts -=1
                except:
                    # stop if a[index] in not found
                    notFound=False   
                index += 1
   
    return a
print(f'to {removeDuplicates_Method1(twoList)}')
