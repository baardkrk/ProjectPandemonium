void setup() {
  size(640,320);
}

void draw() {
  background(51);
  
  int center = mouseX;
  
  // testing the gaussian function
  float[] gauss_test = new float[width];
  for (int i = 0; i < gauss_test.length; i++) {
    gauss_test[i] = height-gaussian(i, 4*(abs(width/2-mouseX)+1), center)*(height-mouseY)*height/2;
  }

  
  // drawing the values
  for (int i = 1; i < gauss_test.length; i++) {
    line(i-1, gauss_test[i-1], i, gauss_test[i]);
    stroke(255);
  }
}

// the x pos will be whatever position the wind speed origin is minus the current position being updated
float gaussian(int x, float variance, int center) {
  float ret = 1.0/sqrt(variance*2*PI) * exp(-(1.0/2.0)*pow(x-center, 2)/variance);
  return ret;
}