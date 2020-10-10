# inheritance
'''
Inheritance are 2 types:
1. multilevel : 
    a(this all are class ) a is our parent class
    b child class
    c child class
    d child class
    agr koi class kisi class se inherit krti h vo parent class khelayi jati h
    a=>b=>c=>d
2. multiple
  a b c => parent class
  d=> child class
 Class = class is a combination of 
      variable = attribute
      function = method

inheritance mtlb ek class ko dusri class m inherit krna
assume:
mainclass = super/parent class
subclass = child class     
'''

# we create a class for user
class Aclassparent:
    #constructor 
    def __init__(self, name):
        self.name = name
#method
    #def userNameOutput(self):
          #print('\nUser name:', self.name)  

    def userNameOutput(self):
         print('''
         -----------------------------------
               Parent User name
         ----------------------------------
         user name:{}       
         '''.format(self.name))
#child class
class BchildClass:
    def __init__(self, course):
        self.course = course
    def courseOutput(self):
        print('''
        -------------Child class------------
        Course name:{}            
        ''',format(self.course))


#call the function
name = input('Enter your name:')
course = input()          
# now create object
parentObj = Aclassparent(name)
parentObj.userNameOutput()