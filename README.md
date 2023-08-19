# wifi-base remote control car
## Description
This project make a wifi-base remote control car which can be controlled by keyboard, sound and image. This car is made by esp8266 as wifi recevier and arduino mega as car controller.
## how to use
1. Burn the arduino.ino into arduino mega and burn the esp8266.ino into esp8266.
2. Connect esp8266 RX, TX pin with arduino mega pin 16 and pin 17.
3. Use keyboard.py as keyboard input mode you can input "F" for forward, "B" for backward, "L" for turn left, "R" for turn right, "S" for stop.
4. Use image.py as image regonize mode you can train your model and load the model in this script to control our car.
5. Use sound.py as sound regonize mode you can train your model and load the model in this script to control our car.
