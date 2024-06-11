import datetime
current_date = datetime.date.today()
print("Current date:", current_date)
day_of_week = current_date.weekday()
print(day_of_week)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Today is", weekdays[day_of_week])