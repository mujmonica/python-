from random import randint
num=randint(1,10)
print "welcome,i have my number"
while True:
    a=raw_input("what is your guess?")
    a=int(a)
    if a>num:
        print"too high,again"
    elif a<num:
        print "too low,again"
    else:
        print"got it"
        break

    
        
        

