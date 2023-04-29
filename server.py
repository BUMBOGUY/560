import socket
import threading 

host = '127.0.0.1' #was socket.gethostname()
port = 8000
Threads = 0
client_reconnect = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

clientlist = []

client = ''
address = ''

try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waiting for connection...')
server_socket.listen(1000) #was 2

def client_threads(conn, address):
    client_reconnect = 0
    conn.send(str.encode('TALK NOW'))

    while True:
        data = conn.recv(1024).decode()
        print("From - " + str(data))  # str(data) = user

        for clients in clientlist:
            if(clients != conn):
                clients.send(data.encode())
            #Line 23 was: print("From connected user: " + str(data))
            #data = "ACKNOWLEDGE"
            #conn.send(data.encode())
            #  
        #conn.sendall(str.encode(data))

    print('\nUser_1 disconnected from server.')
    print('Restart client program to connect again.\n')
    conn.close()
    
    
while True:
    client, address = server_socket.accept()
    #print('\tDEBUG address[0]: ' + address[0])
    #print('\tDEBUG str(address[1]): ' + str(address[1]))
    #print('\tDEBUG str(address): ' + str(address)) 
    print("Connection from: " + address[0] + ' | ' + str(address[1]))   # Client IP / Port
    clientlist.append(client)
    BIGTHREAD = threading.Thread(target = client_threads, args = (client, address))
    BIGTHREAD.start()
    Threads += 1
    print('Number of Users: ' + str(Threads))


#Updates:
#changed host to socket.gethostname()
#under While True, changed connection from to str(address)
#added ' : ' to client connection line 33
#line 22 and 23 dynamic string
#Adding a way to reconnect starting on 31

#Trying to add:
#A way to reconnect to the server after QUIT (line 34?)
#Subtract 1 from Threads when user disconnects (Users increase with each connection but no decrease /w disconnect)
#Broadcast messages from server and from clients
#Send messages to clients from server individually

#Per Assignment description (What's left)
#Server Implementation:
#The server should relay messages between clients, broadcasting messages from one client to all other connected clients.
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Client Implementation:
#Client should be able to send messages to the server, which will broadcast them to all other connected clients
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#User Interface:
#Implement a simple command-line interface for both the server and the client; "SEND <message>" to send a message
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Style Points:
#Implement error handling for cases such as connection failures, disconnections, and invalid commands.
#Add additional features, such as user authentication, private messaging between clients, or file transfer capabilities
#Implement a GUI (Graphical User Interface) for the client using a Python library such as tkinter or PyQt.
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





'''
host = '127.0.0.1'
port = 8000
Threads = 0
server_socket = socket.socket()

try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waiting for connection...')
server_socket.listen(3) #was 2

def client_threads(conn):
    conn.send(str.encode('Welcome to the server'))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
        #conn.sendall(str.encode(data))
    conn.close()

while True:
    conn, address = server_socket.accept()
    print("Connection from: " + address[0] + str(address[1]))
    start_new_thread(client_threads,(conn,))
    Threads += 1
    print('Number of Threads: ' + str(Threads))
server_socket.close()
'''



'''
#Get host name and port num > 1024
host = socket.gethostname()
port = 8000
Threads = 0
server_socket = s  ocket.socket()
 
try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waiting for connection...')
server_socket.listen(3) #was 2


def client_threads(conn):
    conn.send(str.encode('Welcome to the server'))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()

while True:
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    start_new_thread(client_threads,(conn,))
    Threads += 1
    print('Number of Threads: ' + str(Threads))

'''
'''
        #Uriel
if(computer_engineer):
    graduate_2023()
    print("Congrats!")
'''