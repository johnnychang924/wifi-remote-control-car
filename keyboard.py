import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = input("Please enter the Server ip:")
port = 5566
s.connect((addr,port))
print("Client start at : ",s.getsockname())
#data1=s.recv(1024)
#print(data1)
while True:
    cmd = input("Please input message:")
    s.send(cmd.encode())
    #data = s.recv(1024)
    #print (data.decode())
    if cmd == 'exit':
        print ("Close socket")
        s.close()
        break
