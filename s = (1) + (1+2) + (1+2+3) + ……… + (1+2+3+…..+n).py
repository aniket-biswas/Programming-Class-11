n =int(input("Enter N:"))
def sumOfSeries(n):
    return sum([i * (i + 1) / 2 for i in range(1, n + 1)])
print(sumOfSeries(n))

