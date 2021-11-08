#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math

def century(year):
  if (len(str(year)) in [1,2] or year == 100) and year > 0: return 1
  return (year - 1) // 100 + 1

#Invoke the function with any given year. 
print(century(1900))