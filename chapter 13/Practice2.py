def addUpChange(coins500, coins100, coins50, coins10):
    total = 500 * coins500 + 100 * coins100 + 50 * coins50 + 10 * coins10
    return total

coins500 = int(raw_input("How many 500-won coins?: "))
coins100 = int(raw_input("How many 100-won coins?: "))
coins50 = int(raw_input("How many 50-won coins?: "))
coins10 = int(raw_input("How many 10-won coins?: "))


total = addUpChange(coins500, coins100, coins50, coins10)

print "You have a total of: ", total
