'''string type:
1. single line-> it can help to find the indexth value
2. doubleline->
''' 
name ="Pihu verma"
print('\nname:',name)

# double/multiline 
multiline = ''' pihu verma bca student sdnfjsdnf
4sdjfnjsfn
weterhdfvjn
fgrbgjren
'''
print(multiline)

name="python"
print(name[0])
print(len(name))

#slicing positive(left to right)
print(name[1:3])
print(name[3:5])
print(name[0:])

#negtive slicing it work right to left
print(name[-1])
print(name[-6:-1])
print(name[-2:])
name="purnima0"
print('\n user title: ',name.title())
print('user capital:',name.upper())
print('user string:',name.isalpha())
# String comparision
a=input("enter your string:")
b=input("enter your 2nd string:")
if len(a)==len(b):
    print("string are equal")
else:
    print("String are not equal:")    
#multiple condition are used through the user input
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
    print("entered numbers are equal")     