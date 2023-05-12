"""                                    
Step 1 table.
Is it summer?         Temperature               Are the squirrels playing?
true                  below 60                            No       
true                  between 60 and 100                  Yes        
true                  above 100                           No                        
false                 below 60                            No           
false                 between 60 and 90                   Yes                   
false                 above 90                            No        

"""

def squirrel_play(summer, temp):
    """ Return True if the temp is between 60 and 90 or if its between 60 and 
    100 in summer.

    squirrel_play(True, 50)
    False
    squirrel_play(True, 70)
    True
    squirrel_play(True, 150)
    False
    squirrel_play(False, 50)
    False
    squirrel_play(False, 70)
    True
    squirrel_play(False, 150)
    False
    """
    if summer == True and temp in range(60,101):
        return True
    elif summer == False and temp in range(60, 91):
        return True
    else:
        return False    



   
print(squirrel_play(True, 50))
print(squirrel_play(True, 70))
print(squirrel_play(True, 150))
print(squirrel_play(False, 50))       
print(squirrel_play(False, 70))
print(squirrel_play(False, 150))
