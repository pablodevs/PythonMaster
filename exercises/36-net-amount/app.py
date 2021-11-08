data = input().strip().split()
operations = [(data[i],int(data[i+1])) for i in range(0,len(data),2)]
money = 0
for op,value in operations:
    if op == 'D': money+=value
    elif op == 'W': money-=value
print(money)