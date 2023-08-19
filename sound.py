from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import socket
import cv2
import argparse
import io
import time
import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter
'''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = '192.168.30.41'
port = 5566
s.connect((addr, port))'''
#print(s.recv(1024).decode())
"""while True:
    s.recv(1024).decode()
    s.send(input().encode())"""

def load_labels(path):
    with open(path, 'r') as f:
        return {i: line.strip() for i, line in enumerate(f.readlines())}


def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
    """Returns a sorted array of classification results."""
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))

    # If the model is quantized (uint8 data), then dequantize the results
    if output_details['dtype'] == np.uint8:
        scale, zero_point = output_details['quantization']
        output = scale * (output - zero_point)

    ordered = np.argpartition(-output, top_k)
    return [(i, output[i]) for i in ordered[:top_k]]


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--model', help='"C:/Users/s6112/Desktop/converted_tflite/model_unquant.tflite"', required=True)
    parser.add_argument(
        '--labels', help='"C:/Users/s6112/Desktop/converted_tflite/labels.txt"', required=True)
    args = parser.parse_args()

    labels = load_labels(args.labels)

    interpreter = Interpreter(args.model)
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']
  
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
  
    while(True):
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('live', frame)
        results = classify_image(interpreter, frame)
        label_id, prob = results[0]
        if labels[label_id] == "class 1":
            print("往前")
        elif labels[label_id] == "class2":
            print("往後")
        elif labels[label_id] == "class3":
            print("停")
        if cv2.waitKey(1) == ord('q'):
            break;
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()