import calendar
from datetime import datetime

def get_month_last_date(today):
    """
    Returns last date of the month in given date
    1. `calendar.monthrange(year, month)` returns a tuple `(first_weekday, number_of_days)`. The second value is the last day of the month.
    2. Use `datetime` to construct the last date of the current month.

    ### Example Output:
    If today is `March 25, 2025`, the output will be:
    ```
    Last date of the current month: 2025-03-31
    ```"""
    last_day = calendar.monthrange(today.year, today.month)[1]

    # Construct the last date of the current month
    last_date = datetime(today.year, today.month, last_day)

    return last_date

def get_next_month_terminal_dates(today):
    """
    Returns the first and last date of the next month from the given date
    1. Get the next month's number by adding 1 to the current month's number.
    2. If the next month is January, increment the year by 1.
    3. Get the last date of the next month.
    4. Construct the first date of the next month."
    """
    # Get the next month's number
    next_month = today.month + 1

    # If the next month is January, increment the year by 1
    year = today.year
    if next_month == 13:
        next_month = 1
        year += 1

    # Get the last date of the next month
    last_day = calendar.monthrange(year, next_month)[1]

    # Construct the first date of the next month
    first_date = datetime(year, next_month, 1)
    last_date = datetime(year, next_month, last_day)

    return first_date, last_date