.void setup() {
  // put your setup code here, to run once:
  Serial1.begin(115200);
  Serial.begin(115200);
  pinMode(7, OUTPUT);
  analogWrite(7, 190);
  pinMode(50, OUTPUT);
  pinMode(51, OUTPUT);
  pinMode(52, OUTPUT);
  pinMode(53, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(Serial1.read());
  if(Serial1.available()){
    char option = Serial1.read();
    Serial.print(option);
    if(option == 'F'){
      forward();
    }
    else if(option == 'B'){
      backward();
    }
    else if(option == 'L'){
      turnLeft();
    }
    else if(option == 'R'){
      turnRight();
    }
    else if(option == 'S'){
      digitalWrite(50, LOW);
      digitalWrite(51, LOW);
      digitalWrite(52, LOW);
      digitalWrite(53, LOW);
    }
  }
}
void forward(){
  digitalWrite(50, HIGH);
  digitalWrite(51, LOW);
  digitalWrite(52, HIGH);
  digitalWrite(53, LOW);
}
void backward(){
  digitalWrite(50, LOW);
  digitalWrite(51, HIGH);
  digitalWrite(52, LOW);
  digitalWrite(53, HIGH);
}
void turnRight(){
  digitalWrite(50, HIGH);
  digitalWrite(51, LOW);
  digitalWrite(52, LOW);
  digitalWrite(53, HIGH);
}
void turnLeft(){
  digitalWrite(50, LOW);
  digitalWrite(51, HIGH);
  digitalWrite(52, HIGH);
  digitalWrite(53, LOW);
}
