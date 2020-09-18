'''
Python operaotrs:
The operayors can be defined as a sysmbol which is reponsible for a particular operation between two operands.
Basically in python there are 7 operators
# 1. Aithmetic operator: It perfrom between the two operands. It include:
a) Addition:(+)
b) Subtraction:(-)
c) Multiplication:(*)
d) Divide:(/) It gives the result in float value.
e) Remineder:(%)
f) floor division:(//)
g) exponent:(**)'''
# Arithmatic
a=10
b=10
print('\nSum:',a+b)

# Exponent It returns the Sqaure value
print('Multiply: ', 6 ** 2)

# Multiplication It simply multiply the operands 
print('Simple multiply:' ,2*8)

#Divition floor give the accurate interger value.
print('Divition floor: ', 15 // 4)

#And if we simply use the divition operator then its give the float value.
print('Divide :',10/2)
#--------------------------------------------------------------------------------#
'''
# 2. Comparison:
a). Equal to Equal to:(==)
b). Not Equal to: (!=)
c). Less then equal to:(<=)
d). Less then (<)
e). Greater then equal to:(>=)
f). Greater then(>)
'''
a = int(input("Enter the 1st number:"))
b = int(input("enter the 2nd number:"))
if a==b:
    print("a==b",a==b)
else:
    print("False",a!=b)
'''
# 3. Assignment
# 4. Logical:
a) and
b) or
c) not
# 5. Bitwise
# 6. Membership 
# 7. Identity

'''

# Arithmatic
a=10
b=10
print('\nSum:',a+b)

# Exponent It returns the Sqaure value
print('Multiply: ', 6 ** 2)

# Multiplication It simply multiply the operands 
print('Simple multiply:' ,2*8)

#Divition floor give the accurate interger value.
print('Divition floor: ', 15 // 4)

#And if we simply use the divition operator then its give the float value.
print('Divide :',10/2)
#-------------------------------------------------------------------------------#
# comparison: == < > ! >= <= !=
print('\nComaprea: ', 3 == 3)
print('\nComaprea: ', 3 != 3)

# Example:
# num1 = input('Enter 1st numeber: ')
# num2 = input('Etner 2nd numeber: ')

# # print('num1 type: ', type(num1))
# # print('\nComapre: ', num1 == num2)
# print('Yes ' + num1 + ' and ' + num2 + ' are equal.')

# logical: and or not
print('\nMultiple condtions: ', 'hi' == 'hi' or 3 > 3)

# Identity: is | is not
name = 'python'
print('Identity: ', 'python' is name)
print('Identity: ', name is not 'python')

# membership: in | not in
mylist = ['ram','shyam']
print('\nmembership: ', 'ram' in mylist)
print('\nmembership: ', 'ram' not in mylist)


'''
Excercise: 
1. Condition check karna hai ki left side string and right side string len equal hai ya nahi. Ye dono string user se input kar ke lena hai.
2. Multiple conditon ka use karna hai and user se more then 3 alat-alag input le kar unpar and | or | not ke case check karne hai.
'''
# 1. String comparision
a=input("enter your string:")
b=input("enter your 2nd string:")
if len(a)==len(b):
    print("string are equal")
else:
    print("String are not equal:")    

# 2. multiple condition are used through the user input
a = int(input("Enter your number:"))
b = int(input("Enter your number:"))
c = int(input("Enter your number:"))
if((a>b and a>c) and (a != b and a != c)): 
    print(a, " is the largest") 
elif((b>a and b>c) and (b != a and b != c)): 
    print(b, " is the largest") 
elif((c>a and c>b) and (c != a and c != b)): 
    print(c, " is the largest") 
else: 
    print("entered numbers are equal:")

