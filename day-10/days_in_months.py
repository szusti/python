def is_leap(year):
    if year % 4:
        if year % 100 == 0:
            if year % 400 ==0:
                print("Leap year")
                return True
            else:
                print("Not leap year")
                return False
        else:
            print("Leap year")
            return True
    else:
        print("Not leat year")
        return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31] # list for non leap year
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)