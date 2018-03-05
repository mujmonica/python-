def get_specials(day,time):
    monday={"b":"monday brea","l":"monday lunch","d":"monday dinner"}
    tuesday={"b":"tuesday brea","l":"tuesday lunch","d":"tuesday dinner"}
    weeks={"m":"monday","t":"tuesday"}
   
    
    
    return locals()[weeks[day]][time]


    

def get_day():
    day=raw_input("day: input m or t")
    return day


def get_time():
    time=raw_input("time: input b/l/d")
    return time



def main():
    
    print "this will help you"
    while True:

        day=get_day()
        time=get_time()
        special=get_specials(day,time)
        
        print special
        another=raw_input("q for quit")
        if another=="q":
            break

if __name__=="__main__":
    main()
    
