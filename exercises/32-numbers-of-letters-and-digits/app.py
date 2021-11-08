def isdigit(c):
    if c in ['0','1','2','3','4','5','6','7','8','9']: return True
    else: return False
def isalpha(c):
    if c.lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']: return True
    else: return False

d={"digits":0, "chars":0}
data = input()

for c in data:
    if isdigit(c): d["digits"]+=1
    elif isalpha(c): d["chars"]+=1

print(f"LETTERS {d['chars']} DIGITS {d['digits']}")