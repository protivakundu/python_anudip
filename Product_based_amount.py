def toys_based_chareges(toy_code,order_amount):
    if toy_code==1:
        if order_amount>1000:
            result=(10/100)*order_amount
            print("The amount is:",result)
        else:
            print("There is no discount")
    elif toy_code==2:
        if order_amount>100:
            result=(5/100)*order_amount
            print("The amount is:",result)
        else:
            print("There is no discount")
    elif toy_code==3:
        if order_amount>500:
            result=(10/100)*order_amount
            print("The amount is:",result)
        else:
            print("There is no discount")
    else:
        print("There is invalid toys")

print("1.Battery_based_toy")
print("2.Key_based_toy")
print("3.Electrical_based_toy")
product_code=int(input("Enter the product code:"))
order=int(input("Enter the ammount:"))
toys_based_chareges(product_code,order)
