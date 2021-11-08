LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
def islower(c):
    if c in LETTERS: return True
    else: return False

def isupper(c):
    if c not in LETTERS and islower(c.lower()): return True
    else: return False


d={"upper":0, "lower":0}
data = input()

for c in data:
    if islower(c): d["lower"]+=1
    elif isupper(c): d["upper"]+=1

print(f"UPPER CASE {d['upper']} LOWER CASE {d['lower']}")