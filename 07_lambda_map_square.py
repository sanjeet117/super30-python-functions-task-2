'''
Use lambda with map() to square

[1, 2, 3, 4, 5, 6]
''' 
numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x**2,numbers))
print(squared)

'''
lambda x: x**2 defines an anonymous function that takes an element x and returns its square.

map(...) applies that lambda to every item in numbers.

list(...) converts the resulting map iterator into a standard Python list.
'''

