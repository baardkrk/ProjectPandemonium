PImage buffer1;
PImage buffer2;

void setup() {
    size(600,400);
    buffer1 = createImage(width, height, RGB);
    buffer2 = createImage(width, height, RGB);
    
}


void fire(int rows) {
    buffer1.loadPixels();
    for (int i = 0; i < buffer1.width; i++) {
	for (int j = 0; j < rows; j++) {
	    int y = buffer1.height - (j+1);
	    int index = i + y * buffer1.width;

	    buffer1.pixels[index] = color(255);

	}
    }

    buffer1.updatePixels();
}

void draw() {
    fire(2);
    
    background(0);
    image(buffer1,0,0);

    buffer1.loadPixels();
    buffer2.loadPixels();
    for (int x = 1; x < width-1; x++) {
	for (int y = 1; y < height-1; y++) {

	    int index0 = x + (y-1) *width;
	    int index1 = (x+1) + y *width;
	    int index2 = (x-1) + y *width;
	    int index3 = x + (y+1) *width;
	    int index4 = x + (y-1) *width;

	    color c1 = buffer1.pixels[index1];
	    color c2 = buffer1.pixels[index2];
	    color c3 = buffer1.pixels[index3];
	    color c4 = buffer1.pixels[index4];
	    
	    float newC =
		brightness(c1) +
		brightness(c2) +
		brightness(c3) +
		brightness(c4);

	    buffer2.pixels[index0] = color(newC * .25);
	}
    }
   
    buffer2.updatePixels(); 


    PImage temp = buffer1;
    buffer1 = buffer2;
    buffer2 = temp;

    image(buffer2, 0,0);
}
