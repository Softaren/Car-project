int VRy = A1;
int VRx = A0;

int yPosition = 0;
int xPosition = 0;

void setup() {
  Serial.begin(9600); 

  pinMode(VRy, INPUT);  
  pinMode(VRx, INPUT);
}

void loop() {
  yPosition = analogRead(VRy);
  xPosition = analogRead(VRx);

  Serial.print(yPosition);
  Serial.print("|");
  Serial.println(xPosition);

  delay(100);
}