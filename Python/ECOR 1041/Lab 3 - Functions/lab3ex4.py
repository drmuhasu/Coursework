import math
def area_of_cone(height, radius):
    return math.pi * radius * math.sqrt((radius**2) + (height**2))

print(area_of_cone(2.5, 5))
print(area_of_cone(3, 12))   
    
    
    