import socket #import libraries
import time # import libraries
#import RPi.GPIO as GPIO # import libraries
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(10, GPIO.OUT)
#GPIO.setup(9, GPIO.OUT)
#GPIO.setup(8, GPIO.OUT)
#GPIO.setup(7, GPIO.OUT)
array = []
rts = '*'
bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a server object called 'bot'
port = 6000 #port number for the socket. 5000 to 8000 work for me
bot.bind(('', int(port))) #bind the server object called bot to the pi's current ip address and port 6000
bot.listen(5) #listen for up to five connections
client, address = bot.accept() #accept a connection
print("Starting...")
while True:
    client.send(rts)
    data = client.recv(2)
    for char in data:
        array.append(char)
        if (int(array[0]) == 1):
            #GPIO.output(10, True)
            print("F Go")
        elif (int(array[0]) == 0):
            #GPIO.output(10, False)
            print("F Stop")
        else:
           #GPIO.output(10, False)
           print("F NR")
           
#####################################################
           
        if (int(array[1]) == 1):
            #GPIO.output(9, True)
            print("L Go")
        elif (int(array[0]) == 0):
            #GPIO.output(9, False)
            print("L Stop")
        else:
            #GPIO.output(9, False)
            print("L NR")
            
#####################################################

        if (int(array[2]) == 1):
            #GPIO.output(8, True)
            print("B Go")
        elif (int(array[2]) == 0):
            #GPIO.output(8, False)
            print("B Stop")
        else:
           #GPIO.output(8, False)
           print("B NR")

######################################################
           
        if (int(array[3]) == 1):
            #GPIO.output(7, True)
            print("R Go")
        elif (int(array[3]) == 0):
            #GPIO.output(7, False)
            print("R Stop")
        else:
           #GPIO.output(7, False)
           print("R NR")
        
        array = []  
  
 
