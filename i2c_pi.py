# Import modules
from smbus import SMBus
from time import sleep

address = 0x05
b = SMBus(1)

try:
	while True:
		# Read light value, the number is sent by Particle Argon
		lightValue = b.read_byte(address)

		# Print information based on lightValue
		if lightValue <= 20:
			print("Too dark. Light: ", lightValue)
		elif lightValue <= 40:
			print("Dark. Light: ", lightValue)
		elif lightValue <= 60:
			print("Medium. Light: ", lightValue)
		elif lightValue <= 80:
			print("Bright. Light: ", lightValue)
		else:
			print("Too bright. Light: ", lightValue)
		
		# 2 Seconds delay between data read
		sleep(2)
except KeyboardInterrupt:
	pass
