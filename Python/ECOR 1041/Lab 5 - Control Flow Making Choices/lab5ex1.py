def tip(cost: float, rating: int):
 """ Return based on the level of rating,a percentage of the cost of the 
 meal.
 
 >>>tip(10, 2)
 1.5
 >>>tip(100, 3)
 20
 >>>tip(50, 1 )
 2.5
 """
 if rating == 1:
  tip = cost * 0.05
 elif rating == 2:
  tip = cost * 0.15
 elif rating == 3:
  tip = cost * .2
 else:
  tip = "The value for satisfaction is unacceptable"
 return tip



print(tip(10, 2))

print(tip(100, 3))

print(tip(50, 1 ))

