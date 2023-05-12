import math
def distance(x1 : float , y1 : float , x2 : float , y2 : float ):
 """
 Return the distance between the points with coordinates (x1, y1) and (x2, y2).
 
 distance( 1 , 1 , 2 , 2 )
 1.414213562
 
 distance( 5.6 , 3.4 , 5 , 3 )
 0.7211102551
 
 distance( 3 , -1.5 , -2 , 4 )
 7.433034374
 
 """
 return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 





a = distance( 1 , 1 , 2 , 2 )
print(a)
a = distance( 5.6 , 3.4 , 5 , 3 )
print(a)
a = distance( 3 , -1.5 , -2 , 4 )
print(a)