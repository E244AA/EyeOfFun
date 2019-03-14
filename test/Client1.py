import socket
import cv2
import numpy
import pickle
import struct

cap = cv2.VideoCapture(0)
sock = socket.socket()
sock.connect(('localhost', 9090))

while(True):

    frame = cap.read()[1]
    frame = cv2.flip(frame, 1)
    data = pickle.dumps(frame)
    # sock.send(frame)
    sock.sendall(struct.pack("H", len(data))+data)
    print("Sended")

    friend_frame = sock.recv(4096)
    print("Getted " + str(friend_frame))

    cv2.imshow('to c1 from c2', friend_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sock.close()