def assistance(income : int, children : int):
 """ Return the assistance that is granted to families based on their income and 
 the number of children 
 >>>assistance(35000, 5)
 7500
 >>>assistance(22000, 1)
 No assistance
 >>>assistance(12000, 2)
 4000
 """
 if 30000 < income < 40000:
  if children >= 3: 
   return 1500 * children
  else: 
   return "No assistance"
 if 20000 < income < 30000:
  if children >= 2: 
   return 1000 * children
  else: 
   return "No assistance"
 if income < 20000:
   return 2000 * children
  
  
print(assistance(35000, 5))
 
print(assistance(22000, 1))

print(assistance(12000, 2))