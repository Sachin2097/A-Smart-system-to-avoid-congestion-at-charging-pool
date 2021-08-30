int red = 11;//sensor1
int green = 10;//sensor1
int red1= 2;//sensor2
int green1=3;//sensor2
int trigPin = 9;
int echoPin = 8;
int trigPin1 = 12;
int echoPin1 = 13;
int red2=4;
int green2=5;
int duration1, distance1;
int duration, distance;




void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  /*#pinMode(trigPin3, OUTPUT);
  #pinMode(echoPin3, INPUT);*/
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(red1, OUTPUT);
  pinMode(green1,OUTPUT);
  pinMode(red2,OUTPUT);
  pinMode(green2,OUTPUT);
    
}

void loop() {
  int duration, distance;
  //First Sensor
  digitalWrite (trigPin, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin, LOW);
  duration = pulseIn (echoPin, HIGH);
  distance = (duration/2) / 29.1;
  Serial.print(distance);
  Serial.print("\t");

//Second sensor  
  digitalWrite (trigPin1, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin1, LOW);
  duration1 = pulseIn (echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;
 
  Serial.print(distance1);
  Serial.print("\n");
    
    if (distance <=15 && distance1 > 15) {  // Change the number for long or short distances.
      digitalWrite (red, HIGH);
      digitalWrite(green,LOW);
      digitalWrite (red1, LOW);
      digitalWrite(green1,HIGH);
      digitalWrite (red2, LOW);
      digitalWrite(green2, HIGH);
    }
    else if (distance > 15 && distance1 <= 15) {  // Change the number for long or short distances.
      digitalWrite (red, LOW);
      digitalWrite(green,HIGH);
      digitalWrite (red1, HIGH);
      digitalWrite(green1,LOW);
      digitalWrite (red2, LOW);
      digitalWrite(green2,HIGH);
    }
    else if(distance <= 15 && distance1 <= 15)
    {
      digitalWrite (red, HIGH);
      digitalWrite(green,LOW);
      digitalWrite (red1, HIGH);
      digitalWrite(green1,LOW);
      digitalWrite (red2, HIGH);
      digitalWrite(green2,LOW);
    }
    else
    {
      digitalWrite (red, LOW);
      digitalWrite(green,HIGH);
      digitalWrite (red1, LOW);
      digitalWrite(green1,HIGH);
      digitalWrite (red2, LOW);
      digitalWrite(green2,HIGH);
    }
}
