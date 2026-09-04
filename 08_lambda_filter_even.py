# Use lambda with filter() to extract even numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_num = list(filter(lambda x: x % 2 == 0,numbers))
print(even_num)

''' 
lambda x: x % 2 == 0 returns True when x is divisible by 2, and False otherwise.

filter(...) keeps only the items from numbers where the lambda returns True.

list(...) converts the filter iterator into a list.
'''

