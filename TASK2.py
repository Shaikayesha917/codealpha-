stock_prices={"AAPL": 180,"TSLA": 250,"GOOGL": 140,"AMZN": 130}
user_stock={}
while True:
    stock=input("enter stock name or enter done to exit").upper()
    if stock=="DONE":
        break
    if stock in stock_prices:
        q = input(f"Enter quantity for {stock}: ")
        if q.isdigit():
            quantity=int(q)
            if stock in user_stock:
                user_stock[stock] += quantity
            else:
                user_stock[stock] = quantity
        else:
            print("enter a number")
    else:
        print("stock not found")
print(user_stock)
total_investment=0
for i in user_stock:
    price=stock_prices[i]
    quantity=user_stock[i]
    value=price*quantity
    total_investment+=value
    print( str(quantity) + " shares × " + str(price) + " = " + str(value))
print("\nTotal Investment Value: " + str(total_investment))
#saving in file
try:
    with open("stock_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock in user_stock:
            price = stock_prices[stock]
            quantity = user_stock[stock]
            value = price * quantity
            file.write( str(quantity) + " shares × " + str(price) + " = " + str(value) + "\n")
        file.write("\nTotal Investment Value: " + str(total_investment) + "\n")
    print("Summary saved to 'stock_summary.txt'")
except:
    print("No valid stock entries found. File not saved.")


'''try:
    with open("stock_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary \n")
        for stock in user_stock:
            price = stock_prices[stock]
            quantity = user_stock[stock]
            value = price * quantity
            file.write(stock + ": " + str(quantity) + " shares × ₹" + str(price) + " = ₹" + str(value) + "\n")
        file.write("\nTotal Investment Value: ₹" + str(total_investment) + "\n")
    print("✅ Summary saved to 'stock_summary.txt'")
except:
    print("❌ Error saving file.")'''


