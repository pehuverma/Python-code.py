'''
# All collection types are as follow:
a) List: Are changable
b) Tuples:Non Changable, Duplicate
c) Set: Non Index, Non Duplicate
d) Dictionary: Changable, Non duplicate
'''
'''
List methods are as follow:
1. append : with the help of this method we can add the one value at the end of the list.
2. clear : we can clear the list
3. copy : with the help of this we an copy the list
4. count : we can count the list values by using this method
5. extent : with the help of this we can merge the  two different list
6. index : 
7. insert :
8. pop : we want to delete the item into the list then we have to aleast pass the on argument or index value
9. remove : with the help of this we can directly delete the value into the list
10. reserve : With the help of this method we can represent our list into reverse format means it give the opposite
output.
11. sort : It represent the list by an decending order 
'''
mylist=[1,2,3,4,5,6,7]
print('\nPrint mylist', mylist)
print('\nType of mylist',type(mylist))
print('\nLenght of my list',len(mylist))
mylist.append(8)
print('\nmylist',mylist)
mylist.pop()
print('\nmylist',mylist)
'''
Difference between List and Tuples:
firstly we will see it representation difference
List syntax: to represent the list we use the Square bracket[]
Tuples syntax: To respresent the list we use the samll brackets and we use single value then we have to use comma ()


# list are changable
# tuples are not changable
List: Duplicates values are allowed
Tuple: Duplicates values are allowed
'''
# Cahngeable list
a = ["Peter","Joseph","Mathew","Ricky"]  
print('\nActual list item :',a)  
# We can change the list item by using the index value
a[0]=("Pihu")
print('\nChnaged the item :',a)
# Unchangebale Tuple item, it will give the error

#  we create a small tuple
mytuple =(1)
print('\nPrint my tuple',type(mytuple))
# if we are not using a comma it will show the interger value
# and if we use ('')then its types will be shown as string
#Or if we use ('' ,) then iten it will show the tuple types
print('\nprint my tuple :', mytuple)
'''
We can cinvert oyr tuple into the list if we want to changle oor tuple itmes then firstly we have to convert tuple
into list.
# Tuples has only two types;
1. Count
2. Index 
'''
mytuple =(1,2,3,4,5,4,2,6,7,1,1,2)
# find the item through the index value:
print('\n Index position of mytuple:',mytuple[3])
#slicing method
print('\nslicing of mytuple:',mytuple[0:2])
# Find the Positive
print('\nPostive way to find the index value of mytuple:',mytuple[1:4:2])
#negative method
print('\nnegative :', mytuple[:-5])
print('\nprint My tuple count :',mytuple.count(1))
print('\n Print my tuple index:',mytuple.index(3))

# Now we creating the friend list
mylist=["pihu","purnima","Himani","Shetal","rohan"]
print('\nFriend list:',mylist)
mytuple = tuple(mylist)
print('\nNon-changeable:',mytuple)
#--------------------------------------------------------------#
'''
SET : it is totally different from list, tuples and dict
syntan{}
in set duplicates values are not allowed
values are no index
In set we use union, intersection etc...
Myset methods: 
1. clear
2. copy
3. difference
4. difference-update
5. discard
6. intersection
7. intersection-update
8. isdisjoint
9. issubset
10. issuperset
11. pop
12. remove
'''
#code
myset={1,2,3,4,5,6,7}
print('\nPrint my set:',myset)
print(type(myset))
#membership operator : in
print('\nCompare in:',1 in myset)
#indentity operator : is check the quality
print('\nCompare is:', 1 is myset)
# adda single value in set
myset.add(8)
print(myset)
#update for storing multiple values
# to add a multiple value you must have to create a list
addlist =[9,10,11,12,13]
myset.update([9,10,11,12,13])
print(myset)
# remove a value using remove method
myset.remove(13)
print(myset)
#Again if we want remove the same value then it will give/show an error
# if we don't want to see the error message than we use the discard method

myset.discard(12)
print(myset)
myset.discard(12)
print(myset)
# make a copy of our set
myset.copy()
print('\ncopyset:',myset)
myset.clear()
print('\nclear set:',myset)
myset={1,2,3,4,5,6}
print('\nMyset :',myset)
myset.clear()
print('\n clear myset:',myset)
myset={1,2,3,4,5}
yourset={10,11,12,13,14,15}
unionset = myset.union(yourset)
print('\n Unionset:',unionset)
#merge 2 set into 1 using update()
myset.difference_update(yourset)
print()

#intersection : it will show the common item between 2 set(similar values)
x = {"anita", "yadav", "john"}
y = {"google", "microsoft", "yadav"}
z = x.intersection(y)
print('\nIntersection item:',z)

#intersection update removes the items from the original set that are not present in both the sets
x={1,2,3,6}
y={4,5,1,7,9,}
x.intersection_update(y)
print('\nintersection_update values:', x)

#------------------------------------------------------------------------#
'''
dic syntax: {Key:values}
Keys must be a single element
Value can be any type such as list, tuple, integer, etc.
difference between dic and list
in list we have to know the index value which is tough to remember
in dic we directly use the key value

Dictionary typle: (clear, get, item, key, pop, pop-item, from-key, copy, set-default, update, values)
1. clear() : It is used to delete all the items of the dictionary.
2. copy() : It returns a shallow copy of the dictionary.
3. pop() : removes an element from the dictionary. It removes the element which is associated to the specified key.
4. pop-item() : It removes arbitrary element and return its value. 
 If the dictionary is empty, it returns an error KeyError.
5. key() : It returns the all key elements 
'''

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee) 
#key() : It returns the all key elements
p = Employee.keys()
print(p)
# get on single value
print(Employee['Name'])
# The pop() method accepts the key as an argument and remove the associated value. Consider the following example.
pop = Employee.pop("Company")
print(Employee)
p = Employee.popitem()
print('\n removed ',p)
print('\n Print the popitme:',Employee)
# Creating a Dictionary   
# with dict() method   
Dict = dict({1: 'Purnima', 2: 'python', 3:'BCA'})   
print("\nCreate Dictionary by using  dict(): ",Dict)   


#Copy the DICT file using copy method
Dict.copy()
print('\nCopy file :',Dict)

