import socket			 
s = socket.socket()		 
print ("Socket successfully created")
port = 12345		
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 
s.listen(5)	 
print ("socket is listening")		 
while True:  
	c, addr = s.accept()	 
	print ('Got connection from', addr ) 
	while True:
		data = c.recv(1024)
		if not data:
			break
		print("Mesage:", data.decode())
	c.send('Thank you for connecting'.encode()) 
	c.close()
	break