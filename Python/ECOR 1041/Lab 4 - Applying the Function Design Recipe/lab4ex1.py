import math
def area_of_disk(radius: float):
 '''
 Return the area_of_disk using an equation that has the radius as a variable.
 
 area_of_disk(4)
 50.26548246
 
 area_of_disk(2)
 12.56637061
 
 area_of_disk(1.5)
 7.068583471
 '''
 return math.pi * radius ** 2


a = area_of_disk(4)
print(a)
a = area_of_disk(2)
print(a)
a = area_of_disk(1.5)
print(a)

