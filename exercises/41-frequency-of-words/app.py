input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.".strip().split()
expected_output = "2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1"

dic = {}
for item in input:
    dic[item] = str(input.count(item))

output = ''
for key,value in sorted(dic.items()):
    output += f"{key}:{value} "

print(output.strip())
assert output.strip() == "2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1"

# print(dir(dic))