#include <opencv2/highgui/highgui.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/imgproc.hpp>

#include <iostream>
#include <stdlib.h>

using namespace cv;
using namespace std;


void detect_and_display(cv::Mat frame);

/** Global variables */
//String face_cascade_name = "/home/baard/opencv-testing/data/haarcascade_frontalface_alt.xml";
String face_cascade_name = "/home/baard/opencv-testing/data/lbpcascade_frontalface_improved.xml";
String eyes_cascade_name = "/home/baard/opencv-testing/data/haarcascade_eye_tree_eyeglasses.xml";
CascadeClassifier face_cascade;
CascadeClassifier eyes_cascade;
String window_name = "Capture - Face detection";

int main(int argc, char *argv[])
{

  const char* gst = "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)320, height=(int)240, format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)I420 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";

  int cam_num = 0;
  if (argc > 1)
    cam_num = atoi(argv[1]);
    
  if( !face_cascade.load( face_cascade_name ) ) {
    printf("--(!)Error loading face cascade\n%s\n", face_cascade_name.begin()); return -1; };
  if( !eyes_cascade.load( eyes_cascade_name ) ) {
    printf("--(!)Error loading eyes cascade\n"); return -1; };

  
  VideoCapture cap(cam_num);
  Mat frame;

  if (!cap.isOpened()) {
    cout << "Could not open webcamera" << endl;
    return 1;
  }

  
  for (;;) { // while (cap.read(frame))
    if (!cap.read(frame)) break; // if (frame.empty())

    detect_and_display(frame);
    // imshow("webcam", frame);

    if (waitKey(30) >= 0) break;
  }

  return 0;
};


void detect_and_display(cv::Mat frame)
{

  std::vector<cv::Rect> faces;
  cv::Mat gray_frame;

  cv::cvtColor(frame, gray_frame, COLOR_BGR2GRAY);
  cv::equalizeHist(gray_frame, gray_frame);

  face_cascade.detectMultiScale(gray_frame, faces, 1.1, 2, 0|CASCADE_SCALE_IMAGE, cv::Size(30,30));

  for (size_t i = 0; i < faces.size(); i++) {

    cv::Point center(faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2);
    ellipse(frame, center, cv::Size(faces[i].width/2, faces[i].height/2), 0, 0, 360, cv::Scalar(0,0,255), 6, 8, 0);

    // finding eyes in the face
    
  }

  cv::imshow("face_finder", frame);

};
