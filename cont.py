import pygame
pygame.init()

pygame.joystick.init()

print("There are", pygame.joystick.get_count(), " joysticks")

gamepad = pygame.joystick.Joystick(0)
gamepad.init()
print(gamepad)
print(gamepad.get_name())
numaxes = gamepad.get_numaxes()
listaxes = [i for i in range(numaxes)]
numbuttons = gamepad.get_numbuttons()
listbuttons = [j for j in range(numbuttons)]
print("Buttons:", listbuttons)
print("Axes:", listaxes)

while 0:
	for event in pygame.event.get():
		x1 = gamepad.get_axis(0)
		y1 = gamepad.get_axis(1)
		x2 = gamepad.get_axis(3)
		y2 = gamepad.get_axis(4)
		axis2 = gamepad.get_axis(2)
		axis5 = gamepad.get_axis(5)	
		
