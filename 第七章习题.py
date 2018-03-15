print "welcome"
value=raw_input("enter the value")

num=0.0

while True:
    if value.isdigit():
        num=num+float(value)
        value=raw_input("enter the value")
    elif value=="q":
        print "total:{}".format(num)        
        break
    else:
        print "sorry,{}is not valid,try again".format(value)
        value=raw_input("enter the value")
         
