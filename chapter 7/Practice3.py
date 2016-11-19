tank_size = int(raw_input('How big is your tank (liters)? '))
full = int(raw_input ('How full is your tank (eg. 50 for half full)? '))
mileage = int(raw_input ('What is your gas mileage (km per liter)? '))
range = tank_size * (full / 100.0) * mileage
print 'You cna go another', range, 'km.'
print 'The next gas station is 200km away.'
if range <= 200:
    print 'GET GAS NOW!'
else:
    print 'You can wait for the next station.'
