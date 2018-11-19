void setup() {
  Serial.begin(9600);

}

void loop() {
  bool start = false;
  int incomingByte = 0;
  
  if(Serial.available() > 0) {
    incomingByte = Serial.read();
    // Serial.println(incomingByte);
  }
  
  if(incomingByte == 98) {
    start = true;
    Serial.println("Start");
    delay(2000);
  }
  for (int i = 0; i < 200 && start; i++) {
    Serial.print(F("test "));
    Serial.print(i);
    Serial.print("\n");
    delay(100);
   
  }
  if(start) Serial.println("done");

}

