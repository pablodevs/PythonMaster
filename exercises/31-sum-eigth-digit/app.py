list = [n for n in range(1000,3001)if all([int(x)%2!=0 for x in list(str(n))])]
for e in list:
    assert e%2!=0