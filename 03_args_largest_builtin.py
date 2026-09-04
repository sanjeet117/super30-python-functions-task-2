
# Create a function using *args that returns the largest supplied number.
def large_nos(*args):
    largest = max(args,default = None)
    return largest

large_nos(2,3,5,7)

# if tuple would be empty it will print largest = none 