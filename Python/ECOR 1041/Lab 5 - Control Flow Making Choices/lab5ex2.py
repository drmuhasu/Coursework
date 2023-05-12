def coupon(spent : float):
 """ Return a coupon which is a percentage to the amount spent.
 >>>coupon(40)
 8%
 >>>coupon(200)
 12%
 >>>coupon(-10)
 no coupon
 """
 if spent < 10:
  coupon = "No coupon"
 elif spent < 60:
  coupon = "8%"
 elif spent < 150:
  coupon = "10%"
 elif spent < 210:
  coupon = "12%"
 elif spent > 211:
  coupon = "14%"
 return coupon



print(coupon(40))

print(coupon(200))

print(coupon(-10))