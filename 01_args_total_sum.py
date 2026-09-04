# Create a function using *args that accepts any number of values and returns their total.
def total_sum(*args):
    total = sum(args)
    return total

total_sum(1,2,3,4,5,6,7)

# inside function args is packed into the single tuple of all passed value.do sum and return total