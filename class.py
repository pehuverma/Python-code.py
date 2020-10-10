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

# make a class
class Album:
    #pass
    singer ='Arjit'
    songName='I love my india'
#after creating class you will usethe class by object
# how create object
albumObject = Album() 
#print('\n albumObject.singer:',albumObject.singer)  

#creating constructor
def __init__(self,singer,songName):
    #self is current instance and we are creating 2 insttance for singer
    #and song name
    self.s = singer
    self.sn = songName
def albumdetail(self):
    print('''
    ---------------------------------
    Our album name 
    ----------------------------------
    Singer Name : {}
    Song Name : {}
    ''',format(self.s,self.sn))


def oldsongAlbum(self):
    print(''''
    =======================
    old album name
    =======================
    singer name :{}
    song name :{}
    ''',format(self.s,self.sn))