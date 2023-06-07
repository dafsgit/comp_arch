import time
import datetime
# GPIO imports
import RPi.GPIO as GPIO
# Sensor imports
import dht11
from gpiozero import DistanceSensor
# OLED imports
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
# Firebase imports
import pyrebase
# Serial imports
import serial
# GUI imports
import os
from PyQt5 import QtGui, QtCore
from gui import *

# Firebase initialization
config = {
	"apiKey": "AIzaSyA7hUf4r8MVN-JpKFwJIT3Da5rLXw7g-Sk",
	"authDomain": "pf-comp-arch.firebaseapp.com",
	"databaseURL": "https://pf-comp-arch-default-rtdb.firebaseio.com",
	"projectId": "pf-comp-arch",
	"storageBucket": "pf-comp-arch.appspot.com",
	"messagingSenderId": "716244420709",
	"appId": "1:716244420709:web:ead314f7302ab460419e8c",
	"measurementId": "G-BEMGMDFML4"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
email = "a01732610@tec.mx"
password = "12345678"
try:
	signin = auth.sign_in_with_email_and_password(email, password)
	print("You're in")
except:
	print("Invalid credentials")
db = firebase.database()

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

th = 14
thInstance = dht11.DHT11(th)
t = 0
h = 0

lPin = 15
GPIO.setup(lPin, GPIO.IN)

# https://gpiozero.readthedocs.io/en/stable/api_input.html
echo = 23
trigger = 24
dInstance = DistanceSensor(echo, trigger)

fPin = 18
GPIO.setup(fPin, GPIO.IN)

# OLED setup
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
font = ImageFont.load_default()

# Serial setup
s = serial.Serial('/dev/ttyACM0', 9600)


class Ui_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def sensorLoop(self):
		# Read temperature and humidity
		global t, h, thValues
		thValues = thInstance.read()
		if thValues.is_valid():
			t = thValues.temperature
			h = thValues.humidity
			
		# Read light
		global lPin
		if GPIO.input(lPin) == 0:
			lVal = True
			lStr = 'ON'
		else:
			lVal = False
			lStr = 'OFF'
		
		# Read distance
		global dInstance
		d = float(format(dInstance.distance*100, '.2f'))

		# Read flame
		global fPin
		if GPIO.input(fPin) == 0:
			fVal = True
			fStr = 'ON'
		else:
			fVal = False
			fStr = 'OFF'
		
		# Show sensor values - OLED
		image = Image.new('1', (width, height))
		draw = ImageDraw.Draw(image)
		draw.text((10, 4), 'Temp (°C):', font=font, fill=255)
		draw.text((88, 4), f'{t}', font=font, fill=255)
		draw.text((10, 16), 'Hum (%):', font=font, fill=255)
		draw.text((88, 16), f'{h}', font=font, fill=255)
		draw.text((10, 28), 'Light:', font=font, fill=255)
		draw.text((88, 28), lStr, font=font, fill=255)
		draw.text((10, 40), 'Dist (cm):', font=font, fill=255)
		draw.text((88, 40), f'{d}', font=font, fill=255)
		draw.text((10, 52), 'Presence:', font=font, fill=255)
		draw.text((88, 52), fStr, font=font, fill=255)
		disp.image(image)
		disp.show()
		
		# Show sensor values - LED matrix
		command1 = 'control!write!T' + str(int(t)) + ' H' + str(int(h)) + ' L' + lStr + ' D' + str(int(d)) + ' P' + fStr + '*'
		command2 = 'control!show!'
		s.write(command1.encode())
		s.write(command2.encode())

		# Show sensor values - GUI
		window.lcd_tmp.display(t)
		window.pb_hmd.setValue(int(h))
		window.cb_lgt.setChecked(lVal)
		window.lcd_dst.display(d)
		window.cb_flm.setChecked(fVal)
		
		# Update RT database - Firebase
		dtTemp = {"Temperatura": f"{t}"}
		db.child("Sensores").update(dtTemp)
		dtHumi = {"Humedad": f"{h}"}
		db.child("Sensores").update(dtHumi)
		dtLght = {"Luz": lStr}
		db.child("Sensores").update(dtLght)
		dtDist = {"Distancia": f"{d}"}
		db.child("Sensores").update(dtDist)
		dtFlme = {"Presencia": fStr}
		db.child("Sensores").update(dtFlme)
		
		timeNow = datetime.datetime.now()
		window.lbl_time.setText("Última actualización: " + str(timeNow))
		print("Última actualización: " + str(timeNow))
	
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
	
		timer = QtCore.QTimer(self)
		timer.timeout.connect(self.sensorLoop)
		timer.start(5000)


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = Ui_MainWindow()
	window.show()
	app.exec_()
