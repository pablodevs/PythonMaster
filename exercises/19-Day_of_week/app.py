# Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  return (3+k)%7



# Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(140))
print(day_of_week(30))
print(day_of_week(31))
print(day_of_week(365))
print(day_of_week(0))
# 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday
# January 1 was Thursday