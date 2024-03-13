// This code is copied from:
// http://code.litomisky.com/2014/03/09/how-to-have-multiple-versions-of-the-same-library-side-by-side/

#include <iostream>
#include "opencv2/core/version.hpp"

int main(int argc, char ** argv)
{
  std::cout << "OpenCV version: "
			<< CV_MAJOR_VERSION << "." 
			<< CV_MINOR_VERSION << "."
			<< CV_SUBMINOR_VERSION
			<< std::endl;
  return 0;
}
