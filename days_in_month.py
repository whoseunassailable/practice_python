def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = []
  trueOrFalse = is_leap(year)
  if trueOrFalse:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

