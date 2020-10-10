'''
Lambda
1. It is similar to the functions when we define function then we used 'def' keyword
2. so lambda function is also called as anonymous function we used with it lambda keyword
3. it is a single line function....
4. in lambda we get multiple arguments , but it express single.
5. function k andr function use krna ho to hm lambda function use krte h 
6. filter() ye map() function k sath iska jyda use hota h
7. ye kisi function k liye as a argument hota h.


Syntax: 
lambda arguments : expression
function k andr hm ouput k liye function ko call krte the 
lkin lambda m hm lambda ko phle variable m store krte h
'''
# normal lambda function
lamvalue = lambda a, b, c : a *b *c
# finally print the lamvalue but remember our lambda function is  stored in lambalue
print('\n our lamvalue:',lamvalue(10,10,2))
# =================difference between lambda and functiom:
#normal function
def myfunc(a,b,c):
    answer = a*b*c
    print('\nmyfunc answer:',answer)
myfunc(10,10,4)    

#in normal function use lambda function
def user (num):
    return  lambda a: a + num
#function with argument with no return value
   # print('\n Answer:',answer(50))    

# remember in this case at first we will call user function
answer = user(10)    
# function with argument and with its return value
print('\n Answer:',answer(505)) 

# best use of lambda with map and filter
#filter use list and filter method
# to find only even number from the list by using filter and lambda
mylist = [1,2,3,4,5,6,7,8,9,45,66]
# we create new varible to store only even value
evenNumlist = list(filter(lambda number: (number%2 == 0),mylist))
print('\n Our even list :',evenNumlist)

#map() function using to get double all list values
# so we use our previous list mylist
doubleMylistvalues = list(map(lambda number : number*2,mylist))
print('\n Double values of mylist:',doubleMylistvalues)