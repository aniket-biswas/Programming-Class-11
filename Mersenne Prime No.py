p=int(input("Enter P:"))
def lucas_lehmer(p):
    M = 2 ** p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0