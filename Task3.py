# Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

# Steps:

# Start by creating a datetime of the current date, January 1st, 2020: current_date = datetime(year=2020, month=1, day=1)

# Do your calculations to add 25 days to current_date. Create a string and print it out. Your result should look like this:

# Hello Friedrich, your rent of 300 € is due on 26 January, 2020.


import datetime as dt
from datetime import timedelta

current_date = dt.date(year=2020, month=1, day=1)

notification_date = current_date + timedelta(days=25)

print("Current_date:",current_date)
print("Notification_date:",notification_date)
print("Notification: Hello Friedrich, your rent of 300 € is due on 26 January, 2020.")