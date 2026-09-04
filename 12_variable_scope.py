# Demonstrate local and global variable scope using a small program.
X = 100  # global variable accessible anyhwhere in file 

def explain_variable():
    y = 20  # local variable accesible inside function
    print('local variable:',y)
    print('global variable:',X)

explain_variable()