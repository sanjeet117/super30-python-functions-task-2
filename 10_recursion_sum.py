'''  
Write a recursive function to calculate

1 + 2 + 3 + ... + n
'''
def add(n):
    if n <= 0:
        return 0
    return n + add(n-1)

# here we used recursive function add with base n = 0

add(7)