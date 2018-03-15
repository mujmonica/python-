ingredient=["pepperoni","sausage","cheese","peppers"]
client_newingre=[]
client_ingre1=raw_input("please give me a topping")
client_ingre1=client_ingre1.strip()
client_ingre1=client_ingre1.lower()

if client_ingre1 in ingredient:
    print "we have "+client_ingre1
    client_newingre.append(client_ingre1)
else:
    print "we don't have "+client_ingre1


client_ingre2=raw_input("please give me one more topping")
client_ingre2=client_ingre2.strip()
client_ingre2=client_ingre2.lower()


if client_ingre2 in ingredient:
    print "we have "+client_ingre2
    client_newingre.append(client_ingre2)
else:
    print "we don't have "+client_ingre2
print "here are your toppings:"
print client_newingre
