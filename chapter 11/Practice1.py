import time
start = int(raw_input("Countdown timer: How many seconds? ", ))
for i in range (start, 0, -1):
    print i
    time.sleep(1)
print "BLAST OFF!"
