



class ShoppingCart:
    def __init__(self):
        self.items=[]

    def addItem(self,name,price,quantity):
        self.items.append((name,price,quantity))
        print(f'{name} added to cart')


    def deleteItem(self,name):
        for items in self.items:
            if items[0]==name:
                self.items.remove(items)
        print(f'{name} removed from cart')

    def total(self):
        total=[]
        for items in self.items:

            subTotal=items[1]*items[2]
            total.append(subTotal)
        print(f'Your total is {sum(total)}')


cart=ShoppingCart()
cart.addItem("apple",2,5)
cart.addItem("banana",4,6)


cart.total()

cart.addItem("puri",1,1.5)
cart.total()






