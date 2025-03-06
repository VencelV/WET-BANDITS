import cv2
import socket
import pickle
import struct

# Open the laptop camera
cap = cv2.VideoCapture(0)

# Set up the socket connection
server_ip = "YOUR_CORAL_DEV_BOARD_IP"
server_port = 8000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Send data in a loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode the frame to JPEG
    _, encoded_frame = cv2.imencode('.jpg', frame)
    data = pickle.dumps(encoded_frame)

    # Send the length of the data followed by the actual data
    message_size = struct.pack("L", len(data))
    client_socket.sendall(message_size + data)

cap.release()
client_socket.close()