import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanila')
easygui.msgbox ("You entered " + flavor)
