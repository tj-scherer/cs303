import configparser
import numpy as np

def al2num(al):
	ret = []
	for i in range(len(al)):
		ret.append(ord(al[i]) - ord('a'))
	return ret

def num2al(num):
	ret = ''
	for i in range(len(num)):
		ret += chr(num[i] + ord('a'))
	return ret

def encrypt(K, data):
	ret = ''
	for i in range(int(len(data)/3)):
		P = al2num(data[3*i:3*i+3])
		print('P:    ' + str(P))

		C = np.matmul(K, P)
		print('C:    ' + str(C.tolist()[0]))

		for i in range(len(C)):
			C[i] = C % 26
		print('C%26: ' + str(C.tolist()[0]))

		ret += num2al(C.tolist()[0])
	return ret

def decrypt(K_inv, data):
	ret = ''
	for i in range(int(len(data)/3)):
		C = al2num(data[3*i:3*i+3])
		print('C:    ' + str(C))

		P = np.matmul(K_inv, C)
		print('P:    ' + str(P.tolist()[0]))

		for i in range(len(P)):
			P[i] = P % 26
		print('P%26: ' + str(P.tolist()[0]))
		
		ret += num2al(P.tolist()[0])
	return ret

print()
print('# TJ Scherer')
print('# CS303')
print('# HW 1')
print()

config = configparser.ConfigParser()
config.read('config.ini')
config = config['user']

k = np.matrix(config['k'])
k_inv = np.matrix(config['k^-1'])
data = ''

while(len(data) == 0 or len(data) % 3 != 0 or not data.isalnum()):
	data = input('Please enter the string: ').strip()
print()

print('Data to encrypt: ' + data)
print()

print('K =')
print(k)
print()

print('K^-1 =')
print(k_inv)
print()

data_enc = encrypt(k, data)
print('Encrypted: ' + str(data_enc))
print()

data_dec = decrypt(k_inv, data_enc)
print('Decrypted: ' + str(data_dec))
print()

print('Done')