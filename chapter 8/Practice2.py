number = int(raw_input('Which table would you like? '))
print 'Here is your table:'
i = 1
while i <= 10:
    print number, 'times', i, '=', number * i
    i = i + 1
