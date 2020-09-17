print('\n Hello python')

name = input('Enter your name : ')
print(name)

#check through the if else condition weather a number is odd or even
num = int(input("Enter a number : "))
if num%2 ==0:
    print("Number is even")
else:
        print("Number is odd")
    
#Check the person is eligible for vote or not?
age = int(input("Enter your age :"))
if age>=18:
    print("Eligible to vote")
else:
    print("Better luck next year :")    

#check grades
num = int(input("Enter a number :"))
if num>=90:
    print("A")
elif num>=80 and num<=90:
    print("Congrats you scored B ")  
elif num>=70  and num<=80:
    print("Congrats you scored C")
elif num>=60 and num<=70:
    print("you scored D") 
else:
    print("Sorry you are fail")   


# Adding a list item using the append() method
#empty list
l=[]
n= int(input("Enter the emlement : "))
for i in range(0,n):
    l.append(input("Enter the items : "))
print("Printing the list item: ")
for i in l:
    print(i,end = " ")    
l.remove()
print("printing the loist after remove the item: ")
for i in l:
    print(i,end = " ")

 # String comparision
 x = int(input("Enter the 1st string:"))
 y= int(input("Enter the 2nd string:"))   