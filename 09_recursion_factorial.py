# Write a recursive function to calculate factorial.
def calculate_fact(n):
    if n < 0:
        return 'value error' 
    if n == 0:
        return 1
    return n * calculate_fact(n-1)

calculate_fact(5)
'''  
The function call itself is recursive function here calculate_fact(n) calling itself in return 
'''