data = []
check = True
msg = "Enter a correct input:\n"
while check:
    data = [el for el in input(msg).strip().split(',')]
    check_list = [(len(n)==4 and list(set(list(n))) in [['0','1'],['0'],['1'],['1','0']]) for n in data]
    check = not all(check_list)
    msg = "ERROR: Try again:\n"
    
print(','.join([c for c in data if int(c)%5==0]))

