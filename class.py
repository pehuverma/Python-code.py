# class
''' so firstly we will talk on opps class
oops have 2 behaviour :
 class:
     attributes: variable
     behaviour : function = methods

     Constructor method:_int_()its like a wild card entry to all existing
     methods in class and by use construct will pass values as current instance to all methods
Example : attributes: singer, songname
   behaviour : singerdetails
'''

# create class
class MyClass:
    # name = 'Hello Python'
    # creating constructer
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile
    
    def mydetail(self):
        print('\n' + self.name + ' and ' + self.mobile)

    def mypersionaldetail(self, email):
        print('''
        Hello {}, how are you?
        Is this your mobile number {}
        Is this your email id {}
        '''.format(self.name, self.mobile, email))

# create objecte
# myclass()
myobj = MyClass('purnima','8700262044')

myobj.mydetail()
myobj.mypersionaldetail('python@gmail.com')
# print(myobj.name)

# we are trying to make a calculator using a class
class calculator():
    def __init__(self,a,b): # def is used as a constructor
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b 
    def multiply(self):
        return self.a * self.b 
    def divide(self):
        return self.a / self.b  

a = int(input('Enter the first number :')) 
b = int(input('Enter the second number :'))
# now create a object 
obj = calculator(a,b)
while True:
    def menu():
        x=('1. Add\n2.Subtract \n3. Multiply\n4. Divide') 
        print(x)
    menu()
    choice = int(input('please select one of the following :'))
    if choice == 1:
        print("Result:",obj.add())
    elif choice == 2:
        print("Result :",obj.sub())
    elif choice == 3:
        print("Result :",obj.multiply())   
    elif choice == 4:
        print("Result :",obj.divide())
    elif choice == 0:
        print("Again try one of the following")                                 
        break
    else:
        print("Invaild option")
        break
    print()