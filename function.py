'''function -> hum is fucntion k through code ko again nd again use kr skte h apne program m 
function jo h vo code ko divide kr dete h taki code ko easy to understand kr ske programmer 
function are basically 2 tpyes: 
1. User defined : means user apne according function ko built krta h 
  def functionname():

2. Built in function : ye already defined hote h 
i: if(),ii: for(), iii: print()'''

def function():
    print("\nHello function")

#in this line of code the program run but it doesn't show the output
#because we have to call the function to pront the or show the output

function()
''' function can be declare 4 types:
1. function with arguments with return value.
2. function without arguments and without return vlaue.
3. funtion wihtout argumnets with return value
'''
#2nd behaviour of function
# function with argument end with return value
def studentattendence(name, rolllno):
    #print("student name and its rollno:")
 return True
#means if the value is vaild then it represent the boolena value
# after defining the function we need to call the function by its name
if(studentattendence('pihu','22')) == True:
    print("\nYes pihu is present and her rollno is 21 : ")
else:
    print("You got a wrong onformation")   

# 3rd funtion with argument but without retrun value
def singleuser(name):
    print("Hello",name, "How was your day today:")    
singleuser("pihu")     

#4th no argument but retrun value
def otheruser():
    return False 
           
# call function
if otheruser()== True:
    print("Yes other user can use the public authantication")
elif otheruser()== False:
    print("At this moment sever is down")
else:
    print("No one can access the information")

# funtion with unexpected number arguments
# we the stu as a tuple form
def studentcheckfunction(*stu):
    #print('\nGood morning',stu[0],'',stu[1],'',stu[2],'',stu[3])
    #print(type(stu))
 if 'pihu' in stu:
    print("Yes she is in class")
    
studentcheckfunction("pihu",'Himani','kashi','monika')    

#dictionary used with double star(**) we use in key ()
def keyfunction(**user):
    print("hii",user)
    print(type(user))
keyfunction(user='pihu')    