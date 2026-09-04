# Write a recursive function to generate the Fibonacci sequence or calculate the nth Fibonacci number.
def fibo_series(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1] 
    seq = fibo_series(n-1)
    seq.append(seq[-1] + seq[-2])
    return seq

print(fibo_series(9))

'''  
Base Case (n == 2): Directly returns the starter list [0, 1] without making further recursive calls.

Recursive Step (n > 2): Calls fibo_series(n - 1) to fetch the existing sequence.

Append Next Term: Uses negative indexing (seq[-1] + seq[-2]) to sum the last two elements of that
sequence and appends the result to the list.
'''

    