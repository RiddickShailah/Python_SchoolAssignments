wage = input('Please enter your hourly wage: ' )
wage = int(wage)

hour = input('Please enter then number of hours worked per week: ' )
hour = int(hour)

week = input('Please enter your number of hours worked this year: ' )
week= int(week)

# Calculation
week_salary = wage * hour
salary= week_salary * week
print('Your salary so far this year is $', salary, "!")