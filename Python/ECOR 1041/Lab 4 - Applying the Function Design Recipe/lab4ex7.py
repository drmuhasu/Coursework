def replicate(s) -> str:
    '''returns a new string that contains one or more copies of the
    argument. The number of copies is equal to the number of characters in the 
    original string.
    
    >>>replicate('a')
    a
    
    >>>replicate('abc')
    abcabcabc
    
    >>>replicate(xy)
    xyxy
    '''
    return s * len(s)


print(replicate('a'))
print(replicate('abc'))
print(replicate('xy'))