def accumulated_amount(principal, rate, n, time):
    return principal * ( 1 + rate / n ) ** (n * time)

print(accumulated_amount(1500, 0.05, 2, 4))
print(accumulated_amount(1500, 0.05, 2, 0))