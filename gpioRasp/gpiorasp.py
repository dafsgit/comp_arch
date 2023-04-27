import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pines para display
a = 14
b = 15
c = 18
d = 23
e = 24
f = 25
g = 8

# pin para sentido
s = 7

# modo de pines
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(s, GPIO.IN)

i = 0
while True:
	if i == 0:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,0)
	elif i == 1:
		GPIO.output(a,0)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,0)
		GPIO.output(e,0)
		GPIO.output(f,0)
		GPIO.output(g,0)
	elif i == 2:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,0)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,0)
		GPIO.output(g,1)
	elif i == 3:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,0)
		GPIO.output(f,0)
		GPIO.output(g,1)
	elif i == 4:
		GPIO.output(a,0)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,0)
		GPIO.output(e,0)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 5:
		GPIO.output(a,1)
		GPIO.output(b,0)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,0)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 6:
		GPIO.output(a,1)
		GPIO.output(b,0)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 7:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,0)
		GPIO.output(e,0)
		GPIO.output(f,0)
		GPIO.output(g,0)
	elif i == 8:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 9:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,0)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 10:
		GPIO.output(a,1)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,0)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 11:
		GPIO.output(a,0)
		GPIO.output(b,0)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 12:
		GPIO.output(a,0)
		GPIO.output(b,0)
		GPIO.output(c,0)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,0)
		GPIO.output(g,1)
	elif i == 13:
		GPIO.output(a,0)
		GPIO.output(b,1)
		GPIO.output(c,1)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,0)
		GPIO.output(g,1)
	elif i == 14:
		GPIO.output(a,1)
		GPIO.output(b,0)
		GPIO.output(c,0)
		GPIO.output(d,1)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	elif i == 15:
		GPIO.output(a,1)
		GPIO.output(b,0)
		GPIO.output(c,0)
		GPIO.output(d,0)
		GPIO.output(e,1)
		GPIO.output(f,1)
		GPIO.output(g,1)
	
	sentido = GPIO.input(s)
	if sentido == 0:
		# cuenta ascendente
		if i == 15:
			i = 0
		else:
			i = i + 1
	else:
		# cuenta descendente
		if i == 0:
			i = 15
		else:
			i = i - 1
	
	time.sleep(1)
