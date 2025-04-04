import numpy as np
import sys
import random
import math

def removeDuplicates_Method1(a):
        a=list(a)
        a.sort()
        index = 0
        notFound=True
        while(notFound):
                    try:
                            # remove all occurance except one. 
                            counts = a.count(a[index])
                            while counts > 1:
                                a.remove(a[index])
                                counts -=1
                    except:
                        # stop if a[index] in not found
                        notFound=False   
                    index += 1
    
        return a

def startToLists():
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
    # print(type(a),type(msg))
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
                            while counts > 1:
                                a.remove(a[index])
                                counts -=1
                    except:
                        # stop if a[index] in not found
                        notFound=False   
                    index += 1
    
        return a
    print(f'to {removeDuplicates_Method1(twoList)}')

def tupples():
     ages = (2,4, 5,6)
     ages=list(ages)
     ages[0]=11
     ages= tuple(ages)
     print(ages[0])
     print(type(ages))
     print(ages)
     print(ages.count(5))
     for x in ages:
          print(x)

     if 11 in ages:
          print('11 is in ages array ')
     newTupple = tuple(list(ages).copy())
     print(ages+ newTupple)
# tupples()
def sets():
     setA = {2,4,6,33,2}
     print(type(setA))
     ages = [4,5,6,7,77,88,5,77,6]
     print(ages)
     print(set(ages))
     print(removeDuplicates_Method1(ages))
     print(len(setA))
     print(2 in setA)
     setA.add(55)
     for x in setA:
          print(f"{x} is in setA")
     print(55 not in setA)
     setB = {"Html","Css","Javascript","React","Python"}
     setA.update(setB)
     setA.update(ages)
     setA.discard(55)
     setC = {True,False,99}
    #  setD =setA.union(setC)
     set1 = {1,3,4,6,8}
     set2 = {9,2,5,6,0}
     setD =setA | setC
     #  setE = set1.intersection(set2)
     setE = set1 & set2
    #  setF = set2.difference(set1)
     setF = set2 - set1
    #  setG = set1.symmetric_difference(set2)
     setG = set1 ^ set2
     set1.intersection_update(set2)
     set2.difference_update(set1)
     set1.symmetric_difference_update(set2)
     print(setD)
     print(setE,'intersection')
     print(set1,'intersection_update')
     print(setF,'difference')
     print(set2,'difference_update')
     print(setG,'symetric_difference')
     print(set1,'symetric_difference_upate')
     print(setA)
# sets()

def dictionaries(): 
     User = {
          "name": "Amadi Chile",
          "email": "amadichile@gmail.com",
          "age": "999"
     }

     print(User)
     print(User["name"])
     print(User["age"])
     print(len(User))
     print(User.get("email"))
     x =  User.keys()
     print(x)
     User["occupation"] = "Web Developer"
     print(x)
     y = User.values()
     print(y)
     User["occupation"] = "Machine Learning Engineer"
     print(y)
     z = User.items()
     print(z)
     User["age"] = 777
     print(z)
     User["color"]= "Black"
     print(z)

     if("color" in User):
          print(f'User has color of {User["color"]} ')
     if("height" not in User):
          print("User does not have Height")
     User.update({"height": "6ft","country": "Nigeria"})
     User.pop("color")
     User.popitem()
     del User["age"]
     print(User)
     for x in User:
          print(x,y)
     for x,y in User.items():
          print(x,y)
     user2 = User.copy()
     print(user2)
     user3 = dict(User)
     print(user3)
     parent = {
          "child1": {
               "name": "Amadi Chile"
          },
          "child2": {
               "name": "Amadi Chike"
          },
          "child3": {
               "name": "Amadi Chide"
          },
     }

     for x in parent.items(): 
          print(x)

     print(parent)
     for outer, inner in parent.items():
          for x in inner:
               print(f"{x} : {inner[x]} ")
     print(User.setdefault("color"))
     print(User)
     print(len(User))

# dictionaries()

def conditionals():
    a = 255
    b= 155
    c = 100
    if a> 5:
        print("a is greater than 5")
    if b > a:
        print(f"{b} is greater than {a}")
    elif b==a:
         print(f'{b} is equal to {a}')
    else:
         print(f'{a} is greater than {b}')
    if b >= a: print(f'{b} is greater than or equal to {a}')
    print(f'{b} is greater than {a}') if a > b else print(f'{a} is greater than {b}')
    print("A") if a > b else print("=") if a == b else print("B")
    if a> b and b > 66:
         print(True)
    else:
        print(False)
    if a > c or c < b:
         print(f'{c} is within the range or {a} and {b}')
    print(True) if not a > b else print(0)
    print(not True)
    if c > 30:
         print('above {c}')
         if(b > c):
              print(f'{b} above {c}')
         else:
              print(f'{c} is below {b}')
    else:
         pass
# conditionals()

def loops():
     i = 0
     while i < 10:
          i +=1
          if i== 4:
               continue
          if i == 8:
               break
          print(i)
     else:
          print(f'while loop ended at {i}')
     names = ["Chile","Amadi","John"]
     for x in names:
          print(x)
     if "Chile" in names:
          print('Chile is in names')
     almighty = "Jehovah"
     for x in almighty:
          print(x)
          if(x == 'o'):
               break
     for x in names:
          if x == "Amadi":
               continue
          print(x)
          i = 0
     for x in range(24,36,3):
          if(i==3):
               break
          i+=1
          print(x)
     else:
          print('for loop ended')

# loops()

def functions():
     def greet(name,title,type):
          print(f'good {type} {title} {name}! How can i help you today? ')
     greet(title="Mr.",name="Chile",type="Evening")
     def sum (a,b,*c):

          args  = list((a,b)) + list(c)
          added = 0
          for x in args:
           added += x
          return added
     print(sum(4,6,7,44,9,30))
     def times(a,b,c):
          result = 1
          # for x in val:
          #      result = a*b*c
          return   a*b*c
     print(times(a=4,b=7,c=12))
     def getCountry(a='Nigeria'):
          return a
     print(getCountry())
     print(getCountry('Chile'))
     print(getCountry('Poland'))
     fruits = ["Apple","banna","Orange"]
     def forFruits(arr):
          for x in arr:
               print(x)
     print("**************")
     forFruits(fruits)
     def sub(x=2,y=5,/):
          return x-y
     print(sub(14,8))
     def mod(*,x=3,y=2):
          return x%y
     print(mod(x=5,y=3))

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(16)
     ab = lambda a,b: a*b
     print(ab(5,100))

     def square(n):
          return lambda a: a**2
     square2 = square(3)
     print(square2(5))
# functions()

def arrays():
     person = ['Chile',44,"Male",'6ft']
     person.append("Christain")
     person.pop(3)
     # print(person)
     person.remove(44)
     print(person[2])
     print(person)

# arrays()

def classes():
     class User:
          x=5
     user1 = User()
     print(user1.x)
     class Person:
          def __init__(self,name,age=44):
               self.name=name
               self.age= age
          def __str__(self):
               return f"{self.name} {self.age}"
          def details(self):
               return f"Hello! My name is {self.name}. I'm {self.age if self.age else 33} years old. "
     user2 = Person("Chile",99)

     print(user2)
     print(user2.age)
     user2.age= 969
     # del user2.age
     print(user2.details())
# classes()


def convertToFraction():
     #! CONVERT TO FRACTION

     def getLengthFromDot(n1):
               n1 = f"{n1}"
               index1 = n1.find('.')
               lenghtFromDot1 = len(n1[index1+1:])
               return lenghtFromDot1

     def isInt(n1):
          n1 = f"{n1}"
          index1 = n1.find('.')
          lenghtFromDot1 = getLengthFromDot(n1)
          valAfterDot1 = n1[index1+1: index1+2]
          isAFactor1 = True if lenghtFromDot1 == 1 and valAfterDot1 == '0' else False
          return isAFactor1

     def getFactors(num,den):
          factors = []
          # find common factors
          for x in range(1,min(num,den)+1):
               n1= str(num/x)
               n2= str(den/x)
               isIntN1 = isInt(n1)
               isIntN2 = isInt(n2)

               if( isIntN1 and isIntN2):
               #   common factor
                    factors.append(x)

          return factors if len(factors) > 0 else [1]
     def isTooSmall (a):
          n1 = str(a)
          return n1.count("e") == 1 and (int(str(n1)[n1.find('-')+1:]) >=6)

     #! toFraction first method
     #  r = 0.5; num == r* 10; den = 10; r = num/dem = 5/10 = 0.5

     def toFraction(a):
          a=f"{a:.5g}" # limit to 5 significant figures
          a = float(a)
          n1= str(a)
          isInteger = isInt(n1)
          if(isTooSmall(n1)) : # ensure fraction is within e-05
               return 'too small'
          elif(isInteger):
               return int(a)
          else:
               lengthFromDot = getLengthFromDot(n1)
               num = int(a * math.pow(10,lengthFromDot))
               den = int( math.pow(10,lengthFromDot))
               commonFactors = getFactors(num,den)
               commonFactor = max(commonFactors)
               num = num // commonFactor
               den = den // commonFactor

               return f"{num}/{den}"


     #! toFraction second method
     #  r = 22/7; num == r * i = int; r = int/i

     def toFraction2 (a):
          i = 1
          check = 1
          wholeNumber = True
          n1 = str(float(a))
          isInteger = isInt(n1)
          if(isTooSmall(n1)):
               return "too small"
          elif(isInteger):
               return int(a)
          else:
               while (wholeNumber):
                    check = a * i
                    if(isInt(str(check))):
                         wholeNumber= False
                    else:
                         i +=1
               return f'{int(check)}/{i}'

     print(toFraction(0.00005)) 
     print(toFraction2(0.00005))


convertToFraction()

