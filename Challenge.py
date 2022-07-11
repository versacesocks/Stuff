name = input("Please, tell me your name: ")
sales = input("Please, input your total month sales: ")

sales = int(sales)

commission = sales * 13/100

commission = round(commission, 2)

print(f"Hello {name}, your commissions this month are ${commission}")