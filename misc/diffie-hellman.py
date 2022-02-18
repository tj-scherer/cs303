# https://www.mtholyoke.edu/courses/quenell/s2003/ma139/js/powermod.html

q = int(input('q: '))
a = int(input('a: '))
YA = int(input('public YA: '))
YB = int(input('public YB: '))

powers = []

XA = 0
while YA not in powers:
	powers.append(a ** XA % q)
	XA = XA + 1
XA = XA - 1

print('XA: ' + str(XA))

powers = []

XB = 0
while YB not in powers:
	powers.append(a ** XB % q)
	XB = XB + 1
XB = XB - 1

print('XB: ' + str(XB))