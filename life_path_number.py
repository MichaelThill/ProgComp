def calc_total(x):
    total = str(x)
    div_by_11 = False
    if int(total) % 11 == 0 and len(total) < 4:
        div_by_11 = True
    while len(total) > 1 and div_by_11 == False:
          temp_total = 0
          for i in total:
                temp_total = temp_total + int(i)
          if temp_total % 11 == 0:
              div_by_11 = True
          total = str(temp_total)
    return(total)


#reads the data into the program and store in list
count = int(input("How many dates: "))
dates_list = []
for i in range(count):
    dates_list.append(input("Input date: "))
     

for i in dates_list:
    day = i[0:2]
    month = i[3:5]
    year = i[6:10]

    day_digit_total = calc_total(day)
    month_digit_total = calc_total(month)
    year_digit_total = calc_total(year)

    sum_of_whole = int(day_digit_total) + int(month_digit_total) + int(year_digit_total)

    if sum_of_whole % 11 == 0:
        print(sum_of_whole, i)
    else:
        print(calc_total(sum_of_whole), i)
