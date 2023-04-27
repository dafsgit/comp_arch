import serial

s = serial.Serial('/dev/ttyACM0', 9600)
#print(s.name)

while True:
	ln = s.readline().decode()
	print(ln, end='', flush=True)
	
