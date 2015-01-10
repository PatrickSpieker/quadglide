#QuadGlide Software v0.1.0
import random

#import serial communication module for use with Xbee Radios
#import serial

#import HID conponents
import pygame

#starting pygame and pygame.joystick
pygame.init()
pygame.joystick.init()
device = pygame.joystick.Joystick(0)
device.init()




#import GUI base, tkinter
from tkinter import *

#import time for sleep functions
from time import sleep

class ControlWindow(Frame):
	"""The GUI window for controlling a quadcopter"""
	def __init__(self, master, device):
		"""Setup the Frame"""
		super(ControlWindow, self).__init__(master)
		self.grid()
		self.setupWidgets()
		self.device = device
		self.update_stick1_x()
		self.update_stick1_y()
		self.update_stick2_x()
		self.update_stick2_y()
	def setupWidgets(self):
        	"""Setup widgets for use in GUI"""

        	#setup stablization button
        	self.button1_txt = "Stablize"
        	self.button1 = Button(self, text = self.button1_txt)
        	self.button1["command"] = None
        	self.button1.grid(row = 1, column = 0, sticky = W)

        	#setup cut power button
        	self.button2_txt = "Kill Power"
        	self.button2 = Button(self, text = self.button2_txt)
        	self.button2["command"] = None
        	self.button2.grid(row = 2, column = 0, sticky = W)

        	#setup safe descent button
        	self.button3_txt = "Safe Descent"
        	self.button3 = Button(self, text = self.button3_txt)
        	self.button3["command"] = None
        	self.button3.grid(row = 3, column = 0, sticky = W)

        #setup placeholder buttons
        	self.button4_txt = "Button 4"
        	self.button4 = Button(self, text = self.button4_txt)
        	self.button4["command"] = None
        	self.button4.grid(row = 4, column = 0, sticky = W)

        	self.button5_txt = "Button 5"
        	self.button5 = Button(self, text = self.button5_txt)
        	self.button5["command"] = None
        	self.button5.grid(row = 5, column = 0, sticky = W)

        	self.button6_txt = "Button 6"
        	self.button6 = Button(self, text = self.button6_txt)
        	self.button6["command"] = None
        	self.button6.grid(row = 6, column = 0, sticky = W)

        	self.button7_txt = "Button 7"
        	self.button7 = Button(self, text = self.button7_txt)
        	self.button7["command"] = None
        	self.button7.grid(row = 7, column = 0, sticky = W)

        	self.button8_txt = "Button 8"
        	self.button8 = Button(self, text = self.button8_txt)
        	self.button8["command"] = None
        	self.button8.grid(row = 8, column = 0, sticky = W)

        	#setup quadcopter telemetry interface
        	self.telemetry_lbl_txt = "Quadcopter Telemetry Readings"
        	self.telemetry_lbl = Label(self, text = self.telemetry_lbl_txt)
        	self.telemetry_lbl.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        #Data read from quadcopter sensors will go here

        #Gyro, accelerometer data, maybe barometer? airspeed?

        #There will be functions which reach out via serial to
        #Xbee to bring in this data

        #In addition, this data will be written to a log file
        #along with the corosponding data from the USB Controller
        #Maybe in a table/chart? CSV file? How often to record these?
        #Every refresh (150ms at current speed), or once a second?


        #setup gap column in between telemetry and USB interface
        	self.gapCol_txt = "\t\t\t"
        	self.gapCol_lbl = Label(self, text = self.gapCol_txt)
        	self.gapCol_lbl.grid(row = 0, column = 3, rowspan = 10)

        #setup USB controller data interface
        	self.usb_lbl_txt = "USB Controller Data Readings"
        	self.usb_lbl = Label(self, text = self.usb_lbl_txt)
        	self.usb_lbl.grid(row = 0, column = 4, columnspan = 2, sticky = E)


        #setup USB controller's first stick with x and y labels and string variables
        	self.stick1_x_txt = "Stick 1's X value:"
        	self.stick1_x_lbl = Label(self, text = self.stick1_x_txt)
        	self.stick1_x_lbl.grid(row = 1, column = 4, sticky = W)

        	self.stick1_x = StringVar()
        	self.stick1_xVar = Label(self, textvariable = self.stick1_x)
        	self.stick1_xVar.grid(row = 1, column = 5, sticky = W)

        	self.stick1_y_txt = "Stick 1's Y Value:"
        	self.stick1_y_lbl = Label(self, text = self.stick1_y_txt)
        	self.stick1_y_lbl.grid(row = 2, column = 4, sticky = W)

        	self.stick1_y = StringVar()
        	self.stick1_yVar = Label(self, textvariable = self.stick1_y)
        	self.stick1_yVar.grid(row = 2, column = 5, sticky = W)

        #setup USB controller's second stick with x and y labels and string variables
        	self.stick2_x_txt = "Stick 2's X value:"
        	self.stick2_x_lbl = Label(self, text = self.stick2_x_txt)
        	self.stick2_x_lbl.grid(row = 3, column = 4, sticky = W)

        	self.stick2_x = StringVar()
        	self.stick2_xVar = Label(self, textvariable = self.stick2_x)
        	self.stick2_xVar.grid(row = 3, column = 5, sticky = W)

        	self.stick2_y_txt = "Stick 2's Y Value:"
        	self.stick2_y_lbl = Label(self, text = self.stick2_y_txt)
        	self.stick2_y_lbl.grid(row = 4, column = 4, sticky = W)

        	self.stick2_y = StringVar()
        	self.stick2_yVar = Label(self, textvariable = self.stick2_y)
        	self.stick2_yVar.grid(row = 4, column = 5, sticky = W)

        #setup boolean quadcopter connection box
        	self.BoolConnect_txt = "Connected: "
        	self.BoolConnect_lbl = Label(self, text = self.BoolConnect_txt)
        	self.BoolConnect_lbl.grid(row = 1, column = 1, sticky = W)

        	self.BoolConnect = StringVar()
        	self.BoolConnectVar = Label(self, textvariable = self.BoolConnect)
        	self.BoolConnectVar.grid(row = 1, column = 2, sticky = W)


	def update_stick1_x(self):
        	self.stick1_x.set(self.device.get_stick1()[0])
        	self.stick1_xVar.after(100, self.update_stick1_x)

	def update_stick1_y(self):
		self.stick1_y.set(self.device.get_stick1()[1])
		self.stick1_yVar.after(100, self.update_stick1_y)

	def update_stick2_x(self):
		self.stick2_x.set(self.device.get_stick2()[0])
		self.stick2_xVar.after(100, self.update_stick2_x)

	def update_stick2_y(self):
		self.stick2_y.set(self.device.get_stick2()[1])
		self.stick2_yVar.after(100, self.update_stick2_y)

class Controller:
	def __init__(self, device):
		self.device = device
		self.stick1_x = None
		self.stick1_y = None
		self.stick2_x = None
		self.stick2_y = None
		self.device.open()
		self.device.set_raw_data_handler(self.data_handler)

	def data_handler(self, data):
	#I don't think this function will be needed, but
	#I left it here anyway for reference (4/14/14)
        #self.stick1_x = data[1]
        #self.stick1_y = data[2]
        #self.stick2_x = data[3]
        #self.stick2_y = data[4]
		pass

	def get_stick1(self):
		for event in pygame.event.get():
	    	#here will go the code assigning the different 
	    	#axis to their respective variables
			pass
		return [self.stick1_x, self.stick1_y]

	def get_stick2(self):
		for event in pygame.event.get():
	    #here will go the code assigning the different 
	    #axis to their respective variables
	    		pass
		return [self.stick2_x, self.stick2_y]

device = hid.HidDeviceFilter(vendor_id = 0x046d, product_id = 0xc216).get_devices()[0]
#device = pygame.joystick.Joystick(0)
#device.init()
gamepad = Controller(device)


root = Tk()
root.title("QuadGlide v0.1.0")
root.geometry("600x250")
window = ControlWindow(root, gamepad)
window.mainloop()






