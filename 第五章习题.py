name=raw_input("give me your name,please[name]")
quantity=raw_input("how many widgets are you buying?[#]")
quantity=float(quantity)

price=raw_input("how much do they cost,per item[#.##]")
price=float(price)


total=price*quantity

print"your total is ${}".format(total)
print"thanks for shopping with us today {}".format(name)
