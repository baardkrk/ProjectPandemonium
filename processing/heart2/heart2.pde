ArrayList<PVector> heart = new ArrayList<PVector>();
float p = 0;

void setup() {
  size(400,400);
}

void draw() {
  background(255, 100, 150);
  
  translate(width/2, height/2 -20);
  stroke(255);
  
  float r = 10;
  float s = 1;
  
  strokeWeight(2);
  if (p >= TWO_PI) {
    fill(255, 150, 190);
    s = map(cos(p), -1, 1, 0.7, 1);
    
    if (p > TWO_PI*5) {
      if (p < TWO_PI*6) {
        heart.clear();
        for (float a = 0; a <= TWO_PI; a += 0.07) {
          buildHeart((r*s)-TWO_PI*20/p, a);
        }
      } else {
        heart.clear();
        p = 0;  
      }
      // heart.remove(0);
    } else {
      heart.clear();
      for (float a = 0; a <= TWO_PI; a += 0.07) {
        buildHeart(r*s, a);
      }
    
      p += 0.07; // p controls speed of the animation, and we want double the speed.

    }
  } else {
    noFill();
    buildHeart(r, p);
  }
  
  
  p += 0.07;
  render();
}

void render() {
  beginShape();
  for (PVector v : heart) {
    vertex(v.x, v.y);  
  }
  endShape();
}

void buildHeart(float r, float t) {
  
  float x =  r * (16 * pow(sin(t), 3));
  float y = -r * (13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t));
  
  heart.add(new PVector(x, y));
}
