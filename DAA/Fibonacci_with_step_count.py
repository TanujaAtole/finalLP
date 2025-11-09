# Recursive Fibonacci with step count
steps_recursive = 0

def fibonacci_recursive(n):
    """
    Recursive function to find nth Fibonacci number.
    Each function call is counted as one step.
    """
    global steps_recursive
    steps_recursive += 1  # Count each call as one step

    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Iterative Fibonacci with step count
def fibonacci_iterative(n):
    """
    Iterative function to find nth Fibonacci number.
    Each loop iteration is counted as one step.
    """
    steps_iter = 0

    if n <= 1:
        return n, 1  # Base case: 1 step for checking

    a, b = 0, 1
    for i in range(2, n + 1):
        steps_iter += 1  # One step per loop
        a, b = b, a + b
    return b, steps_iter


# MAIN PROGRAM
if __name__ == "__main__":
    n = int(input("Enter the number n to find nth Fibonacci number: "))

    # Recursive version
    steps_recursive = 0
    fib_r = fibonacci_recursive(n)
    print(f"\nRecursive Fibonacci({n}) = {fib_r}")
    print("Step count (recursive):", steps_recursive)

    # Iterative version
    fib_i, steps_iter = fibonacci_iterative(n)
    print(f"\nIterative Fibonacci({n}) = {fib_i}")
    print("Step count (iterative):", steps_iter)

    ''' Enter the number n to find nth Fibonacci number: 5

Recursive Fibonacci(5) = 5
Step count (recursive): 15

Iterative Fibonacci(5) = 5
Step count (iterative): 4
    '''
