X=int(input("X:"))
Y=int(input("Y:"))

list = []
for i in range(X):
    inner_list = []
    for j in range(Y):
        inner_list.append(i*j)
    list.append(inner_list)

print("\nList:",list)