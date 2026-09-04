## Detailed Logic & Approaches

1. Arbitrary Arguments (`*args`)
Total Sum (`01_args_total_sum.py`):** `*args` bundles incoming positional arguments into a single tuple. Passing this tuple to `sum(args)` calculates and returns the cumulative total.
Manual Largest (`02_args_largest_manual.py`):** Checks if `args` is empty to safely return `None`. Sets `largest = args[0]` and iterates through `args[1:]`, updating `largest` whenever a greater element is encountered.
*Built-in Largest (`03_args_largest_builtin.py`):** Utilizes `max(args, default=None)` to extract the maximum element while preventing runtime errors if no arguments are provided.

 2. Keyword Arguments (`**kwargs`)
User Profile Generator (`04_kwargs_user_profile.py`):** `**kwargs` packs keyword arguments into a standard dictionary. `.items()` is used to loop through every dynamic key-value pair and display user profile details.

3. Higher-Order Functions (`05_higher_order_calculate.py`)
Dynamic Callback Execution:** Functions are first-class objects in Python. The `calculate(func, a, b)` function receives function references (`add` or `multiply`) without parentheses and invokes `func(a, b)` dynamically at runtime.

 4. Lambda Expressions, `map()`, and `filter()`
Square via Lambda (`06_lambda_square.py`):** Defines a one-line anonymous function `lambda x: x**2` that evaluates and returns the square of the input without requiring `def` or `return` keywords.
Transform via `map()` (`07_lambda_map_square.py`):** `map()` lazily applies the squaring lambda to each item in the list; `list()` materializes the transformed values.
Filter via `filter()` (`08_lambda_filter_even.py`):** `filter()` evaluates the predicate `lambda x: x % 2 == 0` for each item, retaining only numbers that produce a remainder of 0.
5. Recursion

Factorial (`09_recursion_factorial.py`):** Base condition stops recursion at `n == 0` (returns 1) and handles negative inputs. The recursive step computes `n * calculate_fact(n - 1)`.
Sum of Sequence (`10_recursion_sum.py`):** Base condition returns `0` when `n <= 0`. The recursive step breaks the summation into `n + add(n - 1)`.
Fibonacci Generator (`11_recursion_fibonacci.py`):** Base cases handle starting lists (`n=1 -> [0]`, `n=2 -> [0, 1]`). The recursive step calls `fibo_series(n - 1)` and appends the sum of the last two elements using negative indexing (`seq[-1] + seq[-2]`).

 6. Variable Scope (`12_variable_scope.py`)
LEGB Hierarchy:** Demonstrates that variables initialized outside functions reside in the module's global scope, while variables declared inside a function body remain in the local scope and cannot be accessed outside.

 7. Modular Design (`13_mini_calculator.py`)
Separation of Concerns:** Distinct mathematical functions (`add`, `subtract`, `multiply`, `divide`) are isolated from CLI interaction.
Defensive Programming:** `divide()` explicitly validates `b == 0` to prevent `ZeroDivisionError`.
Control Loop:** A `while True` loop inside `main()` manages user input validation and execution flow until option 5 triggers `break`.
