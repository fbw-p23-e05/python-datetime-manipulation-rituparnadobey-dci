### Task 1

# Using the variable called `current_datetime`, subtract 15 days from the current time.

# Hint: use `.strftime()` method to reformat the time

# - If today is 8/07/2021, your result should look like this:

# ```
# 2021-06-23


import datetime as dt
from datetime import timedelta


current_datetime = dt.date.today()

result = current_datetime - timedelta(days=15)

formatted_date = result.strftime("%Y-%m-%d")

print(formatted_date)