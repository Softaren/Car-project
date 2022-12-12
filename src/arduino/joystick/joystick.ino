int VRy = A1;

int yPosition = 0;

void setup() {
  Serial.begin(9600); 

  pinMode(VRy, INPUT);  
}

void loop() {
  yPosition = analogRead(VRy);

  Serial.println(yPosition);

  delay(100);
}