number = int(raw_input('Which table would you like? '))
print 'Here is your table:'
for i in range(1, 11):
    print number, 'x', i, '=', number * i
