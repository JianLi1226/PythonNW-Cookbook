import socket
from binascii import hexlify

def convert_ip4_address (ip4Address):
	packedBin=socket.inet_aton(ip4Address)
	print('Packed: %s'%hexlify(packedBin))
ip4Address= str(input('Enter IPv4 address: '))

convert_ip4_address(ip4Address)
