import socket

MESSAGE = b'givetime'
ADDRESS   = ("127.0.0.1", 123)
 
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

client.sendto(MESSAGE, ADDRESS)
client.settimeout(1)

response = client.recvfrom(19)
response_decoded = response[0].decode('utf-8')

print(f'Current time from server: {response_decoded}')
