import easygui


easygui.msgbox ('This program converts Fahrenheit to Celsius')
temperature = easygui.enterbox('Type in a temperature in Fahrenheit:')
Fahr = float(temperature)
Cel = (Fahr - 32) * 5.0 / 9
easygui.msgbox('That is ' + str(Cel) + ' degrees Celsius.')
