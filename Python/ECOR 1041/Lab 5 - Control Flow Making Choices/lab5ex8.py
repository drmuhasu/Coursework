
def multiplyList(a : int, b : int, c : int):
    """Return the product of the integers a, b, and c unless a number is 
    repeated in which case the number will be discarded.
    
    multiplyList(1,2,3)
    6
    multiplyList(2,2,3)
    3
    multiplyList(1,2,2)
    1
    multiplyList(3,2,3)
    2
    multiplyList(3,3,3)
    Invalid integers.
    """
    if a != b !=c:
        return a * b * c
    elif a == b == c :
        return "Equal integers"
    elif b == c :
        return a
    elif a == b :
        return c
    elif a == c :
        return b
    else:
        return False
    

print(multiplyList(1,2,3))
print(multiplyList(2,2,3))
print(multiplyList(1,2,2))
print(multiplyList(1,2,1))
print(multiplyList(3,3,3))   
    
    
