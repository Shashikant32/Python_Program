def is_leap_year(year):
    # Check if the year is divisible by 4 and not divisible by 100 or divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1  # Leap year
    else:
        return 0  # Not a leap year

# Input year from the user
year = int(input())

# Output 1 if it's a leap year, otherwise output 0
print(is_leap_year(year))
