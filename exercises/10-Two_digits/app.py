#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  digit = str(digit)
  return int(digit[0]), int(digit[1])
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
