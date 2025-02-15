"""
Exercise: 
A leap year is a calendar year that contains an additional leap day.
The extra day (29th Feb) occurs in every year that is a multiple of 4, except for years that are multiples of
of 100, unless they are also divisible by 400.
date: Feb/2025; Exercise openHPI python course
"""

year = 2025 #Change the year to repeat the check

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is no leap year.")
