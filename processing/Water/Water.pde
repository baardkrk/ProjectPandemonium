
int cols, rows;
float[][] curr, prev;

float damping = .97;

void setup() {
  size(600, 400);
  
  cols = width;
  rows = height;
  
  curr = new float[cols][rows];
  prev = new float[cols][rows];

  curr[100][100] = 255;

}

void draw() {
  
  background(0);

  loadPixels();
  for (int i = 1; i < cols-1; i++) {
    for (int j = 1; j < rows-1; j++) {
  
      curr[i][j] = (prev[i-1][j] + 
                    prev[i+1][j] + 
                    prev[i][j+1] + 
                    prev[i][j-1]) / 2 - curr[i][j]; 
                    
      curr[i][j] = curr[i][j] * damping;
      
      int index = i + j * cols;
      pixels[index] = color(curr[i][j] * 100);
    }
  }
  
  updatePixels();
  
  float[][] tmp = prev;
  prev = curr;
  curr = tmp;
 
}

void mouseDragged() {

  // int index = mouseX + mouseY * cols;
  if (mouseX > 1 && mouseX < width && mouseY > 1 && mouseY < height)
    prev[mouseX][mouseY] = 255;

}