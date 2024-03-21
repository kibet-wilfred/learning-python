class product_attributes:
    product_name= ""
    size= 0
    colour= ""
    price= 0

    def __init__(self, product_name, size, colour, price):
        self.product_name = product_name
        self.size = size
        self.colour = colour
        self.price = price
        print("Product attributes created")


    def describe_products(self):
        print("product:" ,self.product_name,"Colour:",self.colour, "size:",self.size,"price:",self.price)

product = product_attributes(product_name="shirt",size=10,colour="blue",price=150)
product.describe_products()

