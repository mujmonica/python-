def main():
    
    print "welcome"
    name=raw_input("give me name,q to quit")
    
    while True:
 
       
        if name=="q":
            print"bye"
            break
        elif inclass(name):
            print "in the class"
            name=raw_input("give me name,q to quit")
            
        else:
            print"not in the class"
            name=raw_input("give me name,q to quit")

            

def inclass(stu_name):
    classmate=["monica","tom","chuan","qinshou"]
    
    
    
    if stu_name in classmate:
        return True
    else:
        return False



if __name__=="__main__":
    main()
    


    
    

            
 
            
            
        
    
    
