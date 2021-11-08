def f(n,times):
    c = str(n)
    result = 0
    for i in range(times):
        result+=int(c*(i+1))
    return result

print(f(9,4))