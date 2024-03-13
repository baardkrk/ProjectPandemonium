class Drop {
 
  float x, y, len, z, mass, nX, nY, nZ, speed;
  Drop(float x, float y, float z, float mass) {
    this.x = x; this.y = y; this.z = z; this.mass = mass;
    speed = 0;
  }
  
  void update(float gravity, float wX, float wY) {
    // calculating endpoints
    nX = x + wX/mass + wX;
    nY = y + mass*gravity + wY/mass + mass*2;
   
    show();
    // calculating new startpoints
    if (y > height) {
      y = -100;
      speed = 0;
    } else {
      speed = speed + mass*gravity + wY/mass;
      y = y + speed;
    }
    
    if (x > width) {
      x = 0;
    } else {
      x = x + wX;
    }
  }
  
  void show() {
    stroke(z);
    line(x, y, nX, nY);
  }
  
}