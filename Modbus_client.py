# first: target ip, second: target port, third: quantity of request


from pyModbusTCP.client import ModbusClient
import random
from sys import argv

if(len(argv)!=4):
	print "first: target ip\nsecond: target port\nthird: quantity of request"
else:
	program, ip, port, quantity = argv

	client = ModbusClient(host=ip, port=int(port))

	client.open()

	for k in range(int(quantity)):
		which=random.uniform(0,4)
		#print int(which)
		if int(which)==0:
			my_number=random.uniform(0,10)
			client.read_holding_registers(int(my_number))

		elif int(which)==1:
			my_value=random.uniform(1,125)
			my_register=random.uniform(0,10)
			client.write_single_register(int(my_register), int(my_value))
			
		elif int(which)==2:
			client.write_multiple_registers(1, [1,2,3])

		else:
			my_number=random.uniform(0,10)
			client.read_holding_registers(int(my_number))

	client.close()

