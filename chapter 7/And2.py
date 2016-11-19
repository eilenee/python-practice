age = float(raw_input("Enter your age: "))
grade = int(raw_input("Enter your grade: "))
color = raw_input("Enter your favorite color: ")
if age >= 8 and grade >= 3 and color == "green":
    print "You are allowed to play this game."
else:
    print "Sorry, you can't play the game."
