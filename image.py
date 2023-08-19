from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
import socket

# Load the model
model = load_model('C:/Users/s6112/Downloads/converted_keras/keras_model.h5', compile=False)
"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = '192.168.30.41'
port = 5566
s.connect((addr, port))"""
cap = cv2.VideoCapture(0)
if not cap.isOpened():
   print("Cannot open camera")
   exit()
while(True):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if cv2.waitKey(1) == ord('q'):
        break;
    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = cv2.resize(frame, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('live', frame)
    prediction = model.predict(data)
    highest = np.argmax(prediction, axis = 1);
    if(highest == 0):
        print("往前")
        #s.recv(1024).decode();
        #s.send("F".encode())
    elif(highest == 1):
        print("往後")
        #s.recv(1024).decode();
        #s.send("B".encode())
    elif(highest == 2):
        print("停下")
        #s.recv(1024).decode();
        #s.send("S".encode())
    #print(np.argmax(prediction, axis = 1))
cap.release()
cv2.destroyAllWindows()