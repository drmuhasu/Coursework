def blackjack(a: int, b: int) -> int:
    """Return the value that is closest to 21.
    
    blackjack(21, 21)
    21
    blackjack(34, 22)
    0
    blackjack(19, 20)
    20
    blackjack(19, 21)
    21
    blackjack(23, 17)
    17
    """
    
    if not (0< a <22):
        a = 0
    if not (0< b <22):
        b = 0
    if (a>b):
      return a
    else: 
      return b    
  
  
  
print(blackjack(21, 21))
print(blackjack(34, 22))
print(blackjack(19, 20))
print(blackjack(19, 21))
print(blackjack(17, 23))
