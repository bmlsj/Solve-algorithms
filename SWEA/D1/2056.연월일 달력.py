
t = int(input())

for i in range(1, t+1):

    s = input()
    year, month, day = s[:4], s[4:6], s[6:]
    one = ['01', '03', '05', '07', '08', '10', '12']
    zero = ['04', '06', '09', '11']
    result = 0

    if int(month) < 1 or int(month) > 12:
        result = -1

    if month == '02':
        if int(day) < 1 or int(day) > 28:
            result = -1

    elif month in one:
        if int(day) < 1 or int(day) > 31:
            result = -1

    elif month in zero:
        if int(day) < 1 or int(day) > 30:
            result = -1

    if result == -1:
        print(f"#{i} -1")
    else:
        print(f"#{i} {year}/{month}/{day}")
