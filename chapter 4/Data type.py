Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 24
>>> b = float(a)
>>> a
24
>>> b
24.0
>>> c = 38.0
>>> d = int(c)
>>> c
38.0
>>> d
38
>>> 
>>> 0.1 + 0.2
0.30000000000000004
>>> print 0.1 + 0.2
0.3
>>> 
>>> e = 54.99
>>> f = int(e)
>>> print e
54.99
>>> print f
54
>>> 
>>> a = '76.3'
>>> b = float(a)
>>> a
'76.3'
>>> b
76.3
>>> 
>>> a = '44.2'
>>> b = 44.2
>>> type(a)
<type 'str'>
>>> type(b)
<type 'float'>
>>> 
>>> print float('fred')

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print float('fred')
ValueError: could not convert string to float: fred
>>> 
>>> fahr = 75
>>> cel = float(5) / 9 * (fahr -32)
>>> print cel
23.8888888889
>>> 
