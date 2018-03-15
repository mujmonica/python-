
class InventoryItem(object):
    def __init__(self,title,description,price,store_id):
        self.title=title
        self.description=description
        self.price=price
        self.store_id=store_id

    def __str__(self):
        return self.title
    
    def change_description(self,description=""):
        if not description:
            description=raw_input("input descriptiong:")
        self.description=description
    def change_price(self,price=-1):
        while price<0:
            price=raw_input("input price:")
            try:
                price=float(price)
                break
            except:
                print "sorry"
        self.price=price

class Software(InventoryItem):
    def __init__(self,title,description,price,store_id,operating_sys,esrb_ranking):
        super(Software,self).__init__(title=title,description=description,price=price,store_id=store_id)
        self.operating_sys=operating_sys
        self.esrb_ranking=esrb_ranking
        
        
    def __str__(self):
        soft_line="{title}used for {operating_sys}".format(title=self.title,operating_sys=self.operating_sys)
        return soft_line
    def __eq__(self,other):
        if self.title==other.title and self.operating_sys==other.operating_sys:
            return True
        else:
            return False
        
        
    


    

    
        
        
        
    
