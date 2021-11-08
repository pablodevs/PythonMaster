#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  str_num = str(num)
  return int(str_num[str_num.index('.') + 1])


#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))