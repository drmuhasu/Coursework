"""                                    
Step 1 table.
Is it the weekend?    Number of pastries         Is the party successful?
true                  below 40                           No       
true                  between 40 and 60                  Yes        
true                  above 60                           Yes                        
false                 below 40                           No           
false                 between 40 and 60                  Yes
false                 above 60                           No        

"""


def bakers_party(weekend : bool, pastry : int):
    """ Return whether the baker's party will be successful, if there are 40 to
    60 pastries on a weekday it will be successful and if not weekend it needs 
    more that 60 to be successful.
    
    bakers_party(True,25)
    No
    bakers_party(True,53)
    Yes
    bakers_party(True,79)
    Yes
    bakers_party(False,20)
    No
    bakers_party(False,60)
    Yes
    bakers_party(False,90)
    No
    """
    if weekend == False and pastry in range(40, 61):
        return True
    elif weekend == False and pastry > 60 : 
        return False    
    elif weekend == False and pastry < 40:
        return False    
    elif weekend == True and pastry > 40:
        return True     
    elif weekend == True and pastry < 40:
        return False
    else:
        return "Invalid values"
    
print(bakers_party(True,25))
print(bakers_party(True,53))
print(bakers_party(True,79))
print(bakers_party(False,20))
print(bakers_party(False,60))
print(bakers_party(False,90))
    
    
    
