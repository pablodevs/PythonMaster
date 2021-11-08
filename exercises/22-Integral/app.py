def f(n):
    dick = {}
    for i in range(1,n+1):
        dick[i] = i*i
    return dick

print(f(int(input())))