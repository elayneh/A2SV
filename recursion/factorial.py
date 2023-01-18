def factorial(n):
    # Terminating base case
    if n == 0:
        return 1
    # Recursive base case
    return n * factorial(n - 1)
def iteration(n):
    if n <= 0:
        return
    i = 1
    for i in range(n - 1, 0, -1):
        n = n * i
    return n

if __name__ == "__main__":
    n = int(input("Please inter the number that U wanna to find the factorial: \n"))
    # print(factorial(n))
    print(iteration(n))
