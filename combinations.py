# Recreating n choose k in Python to use in a flask application
  
# greatest common divisor
def gcd(a, b):
    gcdval = 0

    i = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcdval = i
        i += 1

    return gcdval

def nChooseK(n, k):
    total = 1
    currentn = n - k + 1
    currentk = 1

    # for currentk in range(1, k):
    while currentk <= k:
        gcdval = gcd(currentn, currentk)
        total = (total / (currentk / gcdval)) * (currentn / gcdval)
        currentn += 1
        currentk += 1
    
    return total

# if __name__ == "__main__":

#     n = 52
#     k = 5

#     if n < k:
#         print("n must be greater than k")
#     else:  
#         combinations = nChooseK(n, k)
#         print("Combinations: " + str(combinations))