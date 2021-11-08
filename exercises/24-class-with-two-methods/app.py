class HandleInputs:
    """Docstring"""
    def __init__(self):
        '''Initial values'''
        self.value = None
    
    def __str__(self):
        return "value: {}".format(self.value)
    
    def getString(self):
        self.value = input("Introduce a new value:")
    
    def printString(self):
        print(self.value.upper())


new_value = HandleInputs()
assert new_value.value == None
new_value.getString()
new_value.printString()
print(new_value)