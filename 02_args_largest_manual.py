# Create a function using *args that returns the largest supplied number.
def largest_nos(*args):
    if not args:
        return None  
    largest = args[0]
    for i in args[1:]:
        if i > largest:
            largest = i
    return largest

largest_nos(1,2,4,9,11)

# first if condition is give when list,tuple would be empty the print none and then run loop from 1 to last because 0 considered as largest

