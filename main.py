actual_cost = float(input("Plese enter product price:"))
sale_amount = float(input("Plese enter amount of sales:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
    
else:
        print("NO PROFIT!!!!!")