
#define GPIO_X 2
#define GPIO_Y 4
#define GPIO_Z 16

int State_X = 0; 
int State_Y = 0; 
int State_Z = 0; 

void setup() { 

pinMode(2, INPUT);
pinMode(4, INPUT);
pinMode(16, INPUT);

Serial.begin(9600); 
} 


void loop() { 

State_X = analogRead(GPIO_X);
State_Y = analogRead(GPIO_Y);
State_Z = analogRead(GPIO_Z);

// Serial.println(" x is" + State_X + " y is " + State_Y); 
// Serial.println("x is " + String(State_X) + " y is " + String(State_Y));


float normalized_x = (float)State_X / 4095.0f;
float normalized_y = (float)State_Y / 4095.0f;

Serial.println("Normalized x is " + String(normalized_x) + " Normalized y is " + String(normalized_y));

Serial.println(State_Z);
// Serial.println(String(normalized_x) +"S"+ String(normalized_y))

Serial.println(); 

delay(150); 
} 