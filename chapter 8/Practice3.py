number = int(raw_input('Which table would you like? '))
limit = int(raw_input('How high would you like it to go? '))
print 'Here is your table:'
for i in range(1, limit+1):
    print number, 'times', i, '=', number * 1
