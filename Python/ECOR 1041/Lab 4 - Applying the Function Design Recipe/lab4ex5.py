def repeat(s: str, n: int) -> str:
 """ Return s repeated n times; if n is negative, return the
 empty string.
 
 >>> repeat('yes', 4)
 'yesyesyesyes'
 
 >>> repeat('no', 0)
 ''
 
 >>> repeat('no', -2)
 ''
 
 >>> repeat('yesnomaybe', 3)
 'yesnomaybeyesnomaybeyesnomaybe'
 """
 return s * n
 
a=repeat('yes', 4)
print(a)

a=repeat('no', 0)
print(a)

a=repeat('no', -2)
print(a)

a=repeat('yesnomaybe', 3)
print(a)
