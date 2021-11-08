input = [x.split(',') for x in input().strip().split(' ')]
list = []

for name,age,height in input:
    list.append({'name':name,'age':int(age),'height':int(height)})

list = sorted(list, key = lambda n: (n['name'], n['age'], n['height']))

list = [(n['name'], str(n['age']), str(n['height'])) for n in list]
print(list)

assert list == [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

