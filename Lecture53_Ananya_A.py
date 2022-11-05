price = int(input("Price : "))
def vatCalculate(price):
    result = int(price+(price*7/100))
    return result
print("Result :",vatCalculate(price))