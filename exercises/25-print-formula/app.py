import math

C = 50
H = 30

def calc(n):
    return math.sqrt((2*C*n)/H)

D = input("Values separated by coma please...")
D = D.strip().split(",")
D = [round(calc(int(e))) for e in D]
print(D)