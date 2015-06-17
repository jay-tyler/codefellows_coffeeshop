# codefellows_coffeeshop
##Overview

In this particular example, there are three basic container types:
Item 
Order
Shift

An Item is a thing on a menu with a business cost and a retail price.
An Order consists of one or more item; may also track the customer name, and tracks 
the order time.
A Shift consists of one or more Orders; also tracks the employee name, and the start/end 
times for the shift.

You'll notice that there's a little bit of try/except madness going on in code; this is
mostly to accomodate some more intuitive commands to allow manipulation of Orders and Shifts.
I've never tried this before, but I'm learning that you have to cover many cases to get it to work.

##Tutorial
First making two menu items that every coffee shop has
```
>>>cookie = Item("cookie", 2, 1)
>>>drip = Item("drip coffee", 2, 0.5)
```

We could make an Order by instantiating it with a list of these:
```
>>>order_a = Order([cookie, drip])
>>>order_a
Order([Item('cookie', 2, 1), Item('drip coffee', 2, 0.5)], None)
```

Another way to make a similar order is to add two items together:
```
>>>order_b = cookie + drip
>>>order_b
Order([Item('cookie', 2, 1), Item('drip coffee', 2, 0.5)], None)
```

We can transfer items from one Order to another, for instance:
```
>>>order_a + order_b
>>>order_a
Order([Item('cookie', 2, 1), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1), Item('drip coffee', 2, 0.5)], None)
>>>order_b
Order([Item('NULL_ITEM', 0, 0)], None)
```

Adding an order to itself doubles its size:
```
>>>order_a + order_a
>>>order_a
Order([Item('cookie', 2, 1), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1), Item('drip coffee', 2, 0.5)], None)
```

We can also update an Order by adding an item to it.
```
>>>order_d = drip + drip
>>>order_d + cookie
>>>order_d
Order([Item('drip coffee', 2, 0.5), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1)], None)
```

Finally we have the Shift to contain the orders
```
>>>jasons_shift = Shift("Jason")
```

We can add an Order to the Shift
```
>>>jasons_shift.add_order(order_d)
>>>jasons_shift.orders
[Order([Item('drip coffee', 2, 0.5), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1)], None)]
```

Or we can add a list of Orders using the same function add_order()
```
>>>order_a = drip + drip
>>>order_b = cookie + cookie
>>>jasons_shift.add_order([order_a, order_b])
>>>jasons_shift.orders
[Order([Item('drip coffee', 2, 0.5), Item('drip coffee', 2, 0.5), Item('cookie', 2, 1)], None),
 Order([Item('drip coffee', 2, 0.5), Item('drip coffee', 2, 0.5)], None),
 Order([Item('cookie', 2, 1), Item('cookie', 2, 1)], None)]
```

We can get total sales and total business cost from the orders in the shift
```
>>>jasons_shift.grossprice
14
>>>jasons_shift.grosscost
5.0
```

This code hasn't been extensively tested yet. It will work for all the examples
above, but I think I have created opportunities for unintended use cases where 
it might break.

There's plenty more that I could want to implement too; but alas, no time 
to do it now.
