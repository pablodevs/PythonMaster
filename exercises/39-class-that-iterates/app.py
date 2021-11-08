# input: 100 >>> 0,7,14,21,28,35,42,49,56,63,70,77,84,91,98

class generator():
    """Docstring"""

    def get(value):
        for i in range(value):
            if i%7==0:
                yield i

myonetimeiterableouhyeah = generator.get(100)
for y in myonetimeiterableouhyeah:
    print(y)
    
print("-------- and again bitch! --------")

for y in myonetimeiterableouhyeah:
    print(y)

print("ok no... D:")
