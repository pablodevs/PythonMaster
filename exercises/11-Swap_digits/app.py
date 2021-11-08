#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  num = str(num)
  return ''.join([num[1],num[0]])
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(96))

