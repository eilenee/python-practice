Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> friends = []
>>> friends.append('David')
>>> friends.append('Mary')
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> print letters[0]
a
>>> print letters[3]
d
>>> print letters[1:4]
['b', 'c', 'd']
>>> print letters[1:2]
['b']
>>> print type(letters[1])
<type 'str'>
>>> print type(letters[1:2])
<type 'list'>
>>> print letter[:2]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print letter[:2]
NameError: name 'letter' is not defined
>>> print letters[:2]
['a', 'b']
>>> print letters[2:]
['c', 'd', 'e']
>>> print letters[:]
['a', 'b', 'c', 'd', 'e']
>>> 
>>> print letters
['a', 'b', 'c', 'd', 'e']
>>> letters[2] = 'z'
>>> print letters
['a', 'b', 'z', 'd', 'e']
>>> letters[2] = 'c'
>>> print letters
['a', 'b', 'c', 'd', 'e']
>>> 
>>> letters.append('n')
>>> print letters
['a', 'b', 'c', 'd', 'e', 'n']
>>> letters.append('g')
>>> print letters
['a', 'b', 'c', 'd', 'e', 'n', 'g']
>>> 
>>> letters.extend(['p', 'q', 'r'])
>>> print letters
['a', 'b', 'c', 'd', 'e', 'n', 'g', 'p', 'q', 'r']
>>> letters.insert(2. 'z')
SyntaxError: invalid syntax
>>> letters.insert(2, 'z')
>>> print letters
['a', 'b', 'z', 'c', 'd', 'e', 'n', 'g', 'p', 'q', 'r']
>>> 
>>> letters = ['a','b','c','d','e']
>>> letters.extend(['f', 'g', 'h'])
>>> print letters
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> letters.append(['f', 'g', 'h'])
>>> print letters
['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h']]
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> letters.remove('c')
>>> print letters
['a', 'b', 'd', 'e']
>>> letters.remove('f')

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    letters.remove('f')
ValueError: list.remove(x): x not in list
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> lastLetter = letters.pop()
>>> print letters
['a', 'b', 'c', 'd']
>>> print lastLetter
e
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> del letters[3]
>>> print letters
['a', 'b', 'c', 'e']
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> second = letters.pop(1)
>>> print second
b
>>> print letters
['a', 'c', 'd', 'e']
>>> 
>>> if 'a' in letters:
	print "found 'a' in letters"
else:
    print "didn't find 'a' in letters"

found 'a' in letters
>>> 'a' in letters
True
>>> 's' in letters
False
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> print letters.index('d')
3
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> for letter in letters:
	print letter

a
b
c
d
e
>>> 
>>> letters = ['d', 'a', 'e', 'c', 'b']
>>> print letters
['d', 'a', 'e', 'c', 'b']
>>> letters.sort()
>>> print letters
['a', 'b', 'c', 'd', 'e']
>>> 
>>> letters = ['d', 'a', 'e', 'c', 'b']
>>> letters.sort()
>>> print letters
['a', 'b', 'c', 'd', 'e']
>>> letters.reverse()
>>> print letters
['e', 'd', 'c', 'b', 'a']
>>> 
>>> letters = ['d', 'a', 'e', 'c', 'b']
>>> letters.sort (reverse = True)
>>> print letters
['e', 'd', 'c', 'b', 'a']
>>> 
>>> originial_list = ['Tom', 'James', 'Sarah', 'Fred']
>>> new_list = original_list[:]

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    new_list = original_list[:]
NameError: name 'original_list' is not defined
>>> new_list = original_list[:]

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    new_list = original_list[:]
NameError: name 'original_list' is not defined
>>> original_list[:] = new_list

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    original_list[:] = new_list
NameError: name 'new_list' is not defined
>>> original_list = ['Tom', 'James', 'Sarah', 'Fred']
>>> new_list = original_list[:]
>>> new_list.sort()
>>> print original_list
['Tom', 'James', 'Sarah', 'Fred']
>>> print new_list
['Fred', 'James', 'Sarah', 'Tom']
>>> 
>>> original = [5, 2, 3, 1, 4]
>>> newer = sorted(original)
>>> print original
[5, 2, 3, 1, 4]
>>> print newer
[1, 2, 3, 4, 5]
>>> 
>>> my_tuple = ("red", "green", "blue")
>>> 
>>> joeMarks = [55, 63, 77, 81]
>>> tomMarks = [65, 61, 67, 72]
>>> bethMarks = [97, 95, 92, 88]
>>> classMarks = [joeMarks, tomMarks, bethMarks]
>>> print classMarks
[[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]
>>> 
>>> classMarks = [ [55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88] ]
>>> print classMarks
[[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]
>>> 
>>> for studentMarks in classMarks:
	print sudentMarks

	

Traceback (most recent call last):
  File "<pyshell#119>", line 2, in <module>
    print sudentMarks
NameError: name 'sudentMarks' is not defined
>>> print classMarks[0]
[55, 63, 77, 81]
>>> print classMarks[0][2]
77
>>> 
>>> phoneNumbers = {}
>>> phoneNumbers["John"] = "555-1234"
>>> print phoneNumbers
{'John': '555-1234'}
>>> phoneNumbers["Mary"] = "555-6789"
>>> phoneNumbers["Bob"] = "444-4321"
>>> phoneNumbers["Jenny"] = "867-5309"
>>> print phoneNumbers
{'Bob': '444-4321', 'John': '555-1234', 'Mary': '555-6789', 'Jenny': '867-5309'}
>>> print phoneNumbers["Mary"]
555-6789
>>> 
>>> phoneNumbers.keys()
['Bob', 'John', 'Mary', 'Jenny']
>>> phoneNumbers.values()
['444-4321', '555-1234', '555-6789', '867-5309']
>>> for key in sorted(phoneNumbers.keys()):
	print key, phoneNumbers[key]

	
Bob 444-4321
Jenny 867-5309
John 555-1234
Mary 555-6789
>>> for value in sorted(phoneNumbers.values()):
	for key in phoneNumbers.keys():
		if phoneNumbers[key] == value:
		   print key, phoneNumbers[key]

		   
Bob 444-4321
John 555-1234
Mary 555-6789
Jenny 867-5309
>>> 
>>> del phoneNumbers["John"]
>>> print phoneNumbers
{'Bob': '444-4321', 'Mary': '555-6789', 'Jenny': '867-5309'}
>>> phoneNumbers.clear()
>>> print phoneNumbers
{}
>>> phoneNumbers = {'Bob': '444-4321', 'John': '555-1234', 'Mary': '555-6789', 'Jenny': '867-5309'}
>>> "Bob" in phoneNumbers
True
>>> "Barb" in phoneNumbers
False
>>> 
