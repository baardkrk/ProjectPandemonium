#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/utility.hpp>

#include <iostream>
#include <stdlib.h>

#define USAGE_STRING "Usage: ./gridfinder </path/to/image.jpg> <X> <Y>\n"
#define DEFAULT_PATH "/home/baard/opencv-testing/res/test.jpg"

int main(int argc, char *argv[])
{

  if (argc != 4) {printf(USAGE_STRING); return -1;}
  
  std::string filepath = DEFAULT_PATH; // argv[1];

  cv::Mat src = cv::imread(filepath, 1);
  cv::Mat gray_frame, edges;
  // Convert to grayscale
  cv::cvtColor(src, gray_frame, cv::COLOR_BGR2GRAY);
  // Find edges
  cv::Canny(gray_frame, edges, 100, 200, 3);
  
  std::vector<cv::Vec4i> lines;

  cv::HoughLinesP(edges, lines, 1, CV_PI / 180, 50, 60, 5);


  // Check line similarity -- O(n^2) for exhaustive..
  

  
  for (size_t i = 0; i < lines.size(); ++i) {
    
    cv::Vec4i l = lines[i];
    cv::line(src, cv::Point(l[0], l[1]), cv::Point(l[2], l[3]), cv::Scalar(0, 0, 255), 3, cv::LINE_AA);
  }

  for (;;) {
    cv::imshow("Lines", src);
    if (cv::waitKey(30) >= 0) break;
  }
  return 0;
};
