e = int(input('e: '))
Fn = int(input('F(n): '))

d = 0
mod = (d * e) % Fn

while mod != 1:
	d = d + 1
	mod = (d * e) % Fn
print('d: ' + str(d))