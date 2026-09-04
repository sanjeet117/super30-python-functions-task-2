'''
Create a function that accepts another function as an argument.

Example idea

calculate(add, 10, 20)

calculate(multiply, 10, 20)
'''
def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def calculate(func,a,b):
    return func(a,b)

print(calculate(add,10,20))
print(calculate(multiply,10,20))
    


'''Higher-Order Function: calculate() takes another function as an argument and executes it dynamically.

No Parentheses on Pass: Pass function names without () (e.g., add, not add()) so they run inside calculate(), not before.

Flexibility with *args: Using *args allows calculate() to handle any function regardless of how many numbers it accepts.'''