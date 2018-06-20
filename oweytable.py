import sqlite
users = sqlite.connect('whatever.db') 

class oweytable():
    
    def __init__(self, users):
        //initialise the matrix based on the users, set all values to 0
        //owings
        
    set_owing(userAid, userBid, amount):
        //owings(userAid, userBid) += amount
        //owings(userAid, userBid) += -amount
        
    read(personAid):
        //personAid = whatever
        //for line in owings:
        //  personAOwes.add(line(personAid))
        //return personAOwes
    
    read(personAid, personBid):
        //return owings(personAid, personBid)
