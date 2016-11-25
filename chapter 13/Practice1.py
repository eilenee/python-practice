# 7개의 인자를 받는 함수를 정의
def printAddr(name, num, street, city, prov, pcode, country):
    print name
    print num,
    print street
    print city,
    if prov !="":
        print ", "+prov
    else:
        print ""
    print pcode
    print country
    print

#함수를 호출하고 7개의 인자를 전달
printAddr("Sam", "45", "Main St.", "Ottawa", "ON", "K2M 2E9", "Canada")
printAddr("Jian", "64", "2nd Ave.", "Hong Kong", "", "235643", "China")
