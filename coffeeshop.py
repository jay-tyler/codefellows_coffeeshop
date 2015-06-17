'''
See README for a full tutorial/overview of this file.

An object-oriented model of a coffee shop in response to a codefellows code challenge.

In this particular example, there are three basic container types:
Item 
Order
Shift

An Item is a thing on a menu with a business cost and a retail price.
An Order consists of one or more item; may also track the customer name, and tracks 
the order time.
A Shift consists of one or more Orders; also tracks the employee name, and the start/end 
times for the shift.
'''


import datetime


class Item:
    """Item is a menu item with a name, retail price, and cost."""

    def __init__(self, name, price, cost):
        self.name = name
        self.price = price #This is the retail price the customer pays
        self.cost = cost #This is the cost of producing the item the business pays

    def __add__(self, other):
        '''Adding an Item to an Item creates an Order; Adding an Item to an Order
        should update that Order.'''
        try: 
            '''First trying a binary combination of two Items; will Fail if the objects
            don't have the price and cost attibutes'''
            out = Order([self, other])
        except AttributeError as e:
            '''Try to see if other is an Order object
            If it is, we will modify the Irder to include the Item'''
            try:
                other.additem(self)
                out = other
            except AttributeError as e:
                print("Usage: Can create an order by adding Item to Item, or update an Order by adding Item to Order")
                raise e
            
        return out

    def __repr__(self):
        return 'Item(%r, %r, %r)' % (self.name, self.price, self.cost)

    def __str__(self):
        return "A %s retailing at %f with a %f fixed cost."


class Order:
    """Order consists of menu Items, an optional customer id, and a timestamp"""

    def __init__(self, items, id=None):
        self.items = items
        self.id = id
        self.timestamp = datetime.datetime.now()
        
        self.check_order() #check order will attempt to calculate totals

    def __repr__(self):
        return 'Order(%r, %r)' % (self.items, self.id)

    def __str__(self):
        itemstr = ', '.join(self.items)
        return "An order for %s consisting of %s items." % (self.name, self.items)

    def __add__(self, other):
        #Try first concatenating orders together
        try:
            self.items.extend(other.items)
            self.check_order() #update totals
            if id(other) != id(self): #"delete" second order by nullifying existing items
                other.delete_order()
        except AttributeError: #See if object is an Item; update order
            try:
                self.additem(other)
                self.check_order()
            except AttributeError: #Case of unknown object being added
                raise
    
    def additem(self, new_item):
        self.items.append(new_item)
        self.check_order()

    def check_order(self):
        #Here we make the Order quack.
        try:
            self.totalprice = self.getprice()
            self.totalcost = self.getcost()
        except (AttributeError, TypeError) as e:
            #print("Usage: The first argument is a list of Menu Items")
            raise

    #Remove all items from an order
    def delete_order(self):
        self.items = [NULL_ITEM]
        self.check_order() #Use to get self.totalcost, self.totalprice to zero

    def getprice(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def getcost(self):
        total = 0
        for item in self.items:
            total += item.cost
        return total


class Shift:
    """Shift consists of Orders and takes an employee name and optional
       orders, start-time, and end-time. Start-time is assumed to be time
       of instantiation if not otherwise provided.""" 

    def __init__(self, employee, orders=None, start=None, end=None):
        self.employee = employee
        if not start:
            self.start = datetime.datetime.now()
        self.end = end
        self.orders = orders

        self.check_shift()

    def end_shift(self):
        self.end = datetime.datetime.now()

    def add_order(self, order):
    #add_order will take a singular order or a list of orders
        if not self.orders:
            self.orders = [order]
        else:
            try:
                self.orders.extend(order)
            except TypeError: #for single order
                #try:
                self.orders.append(order)
        try:
            self.check_shift() #Test to see if Orders quack
        except AttributeError: #Case of unknown item being added
            raise
                
    def check_shift(self):
    #Calculate total price and cost over all orders
        if self.orders: #Checking that at least one order has been assigned to the shift
            grossprice = 0
            grosscost = 0
            for order in self.orders:
                grossprice += order.totalprice
                grosscost += order.totalcost
            self.grossprice = grossprice
            self.grosscost = grosscost
        else:
            self.grossprice = 0
            self.grosscost = 0
 

#Defining some object oriented constants for modifying records
NULL_ITEM = Item("NULL_ITEM", 0, 0)
NULL_ORDER = Order([NULL_ITEM], None)


    
