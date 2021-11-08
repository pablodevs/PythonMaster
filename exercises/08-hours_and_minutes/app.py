#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  hours = secs//3600
  minutes = secs//60
  return hours, minutes




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(100000))