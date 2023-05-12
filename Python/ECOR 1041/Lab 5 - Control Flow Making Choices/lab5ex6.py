"""                                    
Step 1 table.
A                     B                                   Returned Value 
42                    0                                   42       
0                     42                                  42         
42                    42                                  84                         
21                    21                                  42            
21                    20                                  41                    
"""

def great_42(a: int, b: int) -> int:
    """ Return True if either value is 42, or if their sum or difference is 42.
    great_42(42, 0)
    True
    great_42(0, 42)
    True
    great_42(42, 42)
    True
    great_42(21, 21)
    False
    great_42(21, 20)
    False
    """
    if abs(a) + abs(b) == 42 :
        return True
    elif a == 0 and b == 42:
        return True
    elif a == 42 and b == 0:
        return True
    else:
        return False

print(great_42(42, 0))
    
print(great_42(0, 42))
    
print(great_42(42, 42))
    
print(great_42(21, 21))
   
print(great_42(21, 20))