lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_chars = ['$','#','@']

def criteria(password):
    check = {'lower': False,'upper': False,'number': False,'special': False,'length': False,}
    if len(password) not in range(6,13): return False
    else:
        check['length'] = True
        for c in password:
            if c in lower_letters: check['lower'] = True
            if c in upper_letters: check['upper'] = True
            if c in numbers: check['number'] = True
            if c in special_chars: check['special'] = True
    return all(check.values())

pssws = ['ABd1234@1','aF1#','2w3E*','2We3345', '2w3*', 'aaaaaaaaaaaa']
print(','.join(list(filter(criteria, pssws))))
