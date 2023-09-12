# ### Task 2

# Using the variable called `current_datetime`, add 7 days to your current day.

# - Your result should look like this, if today is 8/07/2021:

# ```
# 2021-07-15
# ```

import datetime as dt
from datetime import timedelta


current_date = dt.date.today()

result_date = current_date + timedelta(days=7)

date_format = result_date.strftime("%Y-%m-%d")

print(date_format)


