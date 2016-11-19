gender = raw_input("Are you male or female? ('m' or 'f') ")
if gender == 'f':
    age = int(raw_input('What is your age? '))
    if age >= 10 and age <= 12:
        print 'You can play on the team'
    else:
        print 'You are not the right age.'
else:
    print 'Only girls are allowed on this team.'
