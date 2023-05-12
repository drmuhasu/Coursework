import math
def area_of_disk(radius: float):
 return math.pi * radius ** 2

def distance(x1 : float , y1 : float , x2 : float , y2 : float ):
 return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 



def area_of_circle(xc : float, yc : float, xp : float, yp : float):
 """
 Return the area of a circle using the funstions previously defined.
 
 area_of_circle( 1 , 2 , 1 , 4)
 12.56637061
 
 area_of_circle( 5.6 , 3.4 , 5 , 6.3 ) 
 27.55176757
 
 area_of_circle( 1 , -0.5 , -7 , 4 )
 264.6791811
 
 """
 return area_of_disk(distance(xc, yc, xp, yp))




a =  area_of_circle( 1 , 2 , 1 , 4)
print(a)
a =  area_of_circle( 5.6 , 3.4 , 5 , 6.3 ) 
print(a)
a =  area_of_circle( 1 , -0.5 , -7 , 4 )
print(a)