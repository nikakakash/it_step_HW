class shoppingCart:
    def __init__(self):
        self.items = []

    def addItem(self, name, qty):
       temp=[]
       temp.append(name)
       temp.append(qty)
       item1=tuple(temp)
       self.items.append(item1)

    def current_items(self):
        return self.items

    def remove_item(self, name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
        return self.items
    def total(self):
        add=0
        for item in self.items:

            add = add+item[1]
        print(f"total:{add}")

cart = shoppingCart()
cart.addItem("zeti",2)
cart.addItem("karaqi",3)
cart.addItem("wyali",4)
cart.addItem("puri",6)
print(cart.current_items())
cart.total()
cart.remove_item("wyali")
print(cart.current_items())
cart.total()
