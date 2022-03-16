# ####################################################

# :graduation: ALGO CHALLENGE DAY #13 @everyone 

# 👇🏻 
# #Count the divisors of a number

# Count the number of divisors of a positive integer n.

# Random tests go up ton = 500000.

# Examples (input --> output)
# 4 --> 3 (1, 2, 4)
# 5 --> 2 (1, 5)
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)

def divisors(n):
    divs = []
    if n % 2 == 1:
        for i in range(1,n+1,2):
            if n%i == 0: divs.append(i)
    else:
        for i in range(1,n+1):
            if n%i == 0: divs.append(i)
    output = f"{str(n)} --> {str(len(divs))} ({', '.join(str(num) for num in divs)})"
    return output
print(divisors(499999))
print(divisors(500000))


