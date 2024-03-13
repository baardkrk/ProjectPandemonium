Drop drop;

Drop[] rain;

void setup() {
  size(640, 320); 
  rain = new Drop[500];
  
  for (int i = 0; i < rain.length; i++) {
    float x = random(0, width);
    float y = random(0, height);
    float mass = random(1, 10);
    float z = random(100, 255);
    
    rain[i] = new Drop(x, y, z, mass);
  }
  
  drop = new Drop(width/2, height/2, 255, 5);
}

void draw() {
  background(51);
  
  for (int i = 0; i < rain.length; i++) {
    rain[i].update(.04, 1, 0);
  }
  drop.update(.04, 1, 0);
  
}