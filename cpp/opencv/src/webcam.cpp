#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdlib.h>

using namespace cv;
using namespace std;

int main(int argc, char *argv[])
{

  const char* gst = "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)320, height=(int)240, format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)I420 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";

  int cam_num = 0;
  if (argc > 1)
    cam_num = atoi(argv[1]);
    
  
  VideoCapture cap(cam_num);
  Mat frame;

  if (!cap.isOpened()) {
    cout << "Could not open webcamera" << endl;
    return 1;
  }
  
  for (;;) {
    if (!cap.read(frame)) break;

    imshow("webcam", frame);

    if (waitKey(30) >= 0) break;
  }

  return 0;
}
