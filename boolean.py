'''
Boolean values:
1. boolean values always return True orFlase
2. Boolean mathod is bool()

Which condition Boolean values retrun flase 
bool(False)
bool(None)
bool(0)
bool([])
bool(())
bool({})
1.Null()
2.Empty()
'''
print('\n', bool(1))
print('\n', bool())
print('\n', bool([]))

#Example with condition
name= input("Enter your name: ")
#int('\Check name: ',bool(name))

if bool(name)== False:
   print('You must give your name.')
else:
    print('\nName: ',name)   