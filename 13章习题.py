from random import random
frequency={0:0,1:0}
for i in range(1,10000):
    if random()==0:
        frequency[0]=frequency[0]+1
    elif random()==1:
        frequency[1]=frequency[1]+1


print frequency

        
