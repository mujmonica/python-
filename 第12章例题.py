
class InventoryItem(object):
    def __init__(self,title,description,price,store_id):
        self.tile=title
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

class Book(InventoryItem):
    def __init__(self,title,description,price,format,author,store_id):
        super(Book,self).__init__(title=title,description=description,
                                  price=price,store_id=store_id)
        self.format=format
        self.author=author
        
    def __str__(self):
        book_line="{title}by{author}".format(title=self.title,author=self.author)
        return book_line

    

    
        
        
        
    
