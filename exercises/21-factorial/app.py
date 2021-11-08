# Your code here
def compute_factorial (n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(compute_factorial(8))
print(compute_factorial(1))
print(compute_factorial(0))