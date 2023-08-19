#include <ESP8266WiFi.h>
const char* ssid = "Xperia 10 II_3677";
const char* password = "372fc4d005cc";
WiFiServer server(5566);

void setup() {
  Serial.begin(115200);
  //pinMode(LED, INPUT);
  Serial.print("Connecting to ");
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("TP-> ");
  Serial.print(WiFi.localIP());
  server.begin();
  Serial.println();
}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client = server.available();
  if(!client){
    Serial.println("等待Client端接入");
    delay(5000);
    return;
  }
  Serial.println("New Client!");
  while(client){
    //client.print('S');
    if(client.available())
      Serial.println((char)client.read());
      client.flush();
    //delay(1000);
    
  }
}
