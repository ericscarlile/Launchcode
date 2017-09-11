begin_vacation = int(input("What day does the vacation start?"))
num_days_of_vacation = int(input("How many days long is your vacation?"))

return_day = ((begin_vacation + num_days_of_vacation) % 7)
print(return_day)
