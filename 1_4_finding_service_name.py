import socket

def find_service_name() :
    protocolName = 'tcp'
    portsNum=[80,25,443,88]

    for port in portsNum:
        print('Port: %s, Service: %s'%(port, socket.getservbyport(port,protocolName)))

find_service_name()