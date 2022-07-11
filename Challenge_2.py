name = input("What is your name? ")
sale = input("What is your sale this time? ")

sale = int(sale)

commission = round(sale * 13/100, 2)
print(f"Hello {name}, \nYour total commission is ${commission}.")

