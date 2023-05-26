import time
import socket
from djitellopy import Tello

# https://github.com/dbaldwin/DroneBlocks-Tello-Simulator-ChatGPT
# https://github.com/dbaldwin/DroneBlocks-Tello-Python
# https://github.com/damiafuentes/DJITelloPy


# # IP and port of the Tello drone
# tello_ip = '192.168.10.1'  # Example IP address, replace with the actual IP of your Tello drone
# tello_port = 8889

# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # Bind the socket to a specific IP and port (optional)
# # Allows for listening to incoming messages
# sock.bind(('0.0.0.0', tello_port))

# # Send commands to the Tello
# command = "command"
# sock.sendto(command.encode(), (tello_ip, tello_port))

# # Receive response from the Tello
# response, address = sock.recvfrom(1024) #2097152 
# print(response.decode())

tello = Tello()
tello.takeoff()
time.sleep(10)
tello.land()

# Close the socket
#sock.close()