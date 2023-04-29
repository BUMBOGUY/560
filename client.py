import socket
import threading 
from random import random

def RECEIVE(BIGMESSAGE):
    while True:
        response = BIGMESSAGE.recv(1024)
        print('\n' + response.decode('utf-8'))

        if(stopflag == True):
            client_socket.close()
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = '127.0.0.1' #socket.gethostname()
port = 8000 

stopflag = False

print('Waiting to connect...')
log_on = 0

while(log_on == 0):
    connection = input('>> ')
    if(connection.upper().strip() == 'CONNECT'):
        log_on = 1
        try:
            client_socket.connect((host, port))
        except socket.error as e:
            print(str(e))
    else:
        print('\nUnrecognized command.')
        print('Enter \"CONNECT\" to connect to server.\n')

SMALLTHREAD = threading.Thread(target = RECEIVE, args = (client_socket,))
SMALLTHREAD.start()

password = str(int(random() * 100)) 
print(password)
username = input('Name: ')
#PASSWORD


# USER AUTHENTIFICATION
verification = input('Password: ')

while(verification != password):
    print("YOU SUCK \n")
    verification = input('Password: ')


while True:
    Input = input('>> ')
    #client_socket.send(str.encode(User_Tag) + str.encode(Input))

    if(Input[0:4] == 'SEND'):
        User_Tag = username + ': '
        client_socket.send(str.encode(User_Tag) + str.encode(Input[5:]))

    elif(Input.upper().strip() == 'QUIT'):
        print('\nUser_1 disconnected from the server.')
        print('Restart client program to reconnect.\n')
        stopflag = True
        #print('Reconnect to the sever by entering \"CONNECT\".\n')
        client_socket.close()
    else:
        print("TYPE 'SEND' BITCH")
        #print(Input[0:4])
       

    #Updates:
    #host changed to socket.gethostname()
    #added If statement on 26 and else on 32/33
    #Added client1() function to restart process as needed
    
    #IMPLEMENT??
    #Make recv funciton its own thread to constantly look for input rather than
    #wait for input

'''
def client():
    host = socket.gethostname()
    port = 8000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(' -> ')
    
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(' -> ')

    client_socket.close()

if __name__ == '__main__':
    client()
'''