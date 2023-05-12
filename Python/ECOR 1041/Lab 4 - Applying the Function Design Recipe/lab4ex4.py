import math

def height(length : float, angle : float):
 """
 Return the height reached by the ladder.
 
 height( 10, 15)
 2.588190451
 height( 5, 60)
 4.330127019
 height( 6.5, 30)
 3.25
 """
 return math.sin( math.radians(angle) ) * length


a=height( 10, 15)
print(a)

a=height( 5, 60)
print(a)

a=height( 6.5, 30)
print(a)



