'''
Welcome to the Loop Hole!
Today's Manager's Special is:
Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries
How many would you like?
>>> 3.33333
How much would you like to pay per donut (suggested price is $4.35 each)?
>>> 2.5
Ok, let me prepare that for you....
After tax, your total is: $8.74999125
Thank you for snacking! Loop back around here soon!
'''
print("Welcome to the Loop Hole!")
print("Today's Manager's Special is:")
print("Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely "
      "of Capn' Crunch Oops! All Berries")

tax = 1.05
num_donuts = float(input("How many would you like?"))
price_paid = float(input("How much would you like to pay? (Suggested $2)"))

total_price = num_donuts * price_paid * tax
print(total_price)
