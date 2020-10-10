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