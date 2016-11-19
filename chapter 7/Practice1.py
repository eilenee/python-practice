item_price = float(raw_input ('enter the price of the item: '))
if item_price <= 10.0:
    discount = item_price * 0.10
else:
    discount = item_price * 0.20
final_price = item_price - discount
print 'You got ', discount, 'off, so your final price was', final_price
