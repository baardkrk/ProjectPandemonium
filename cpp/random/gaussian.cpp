
/**
 * Produces a normalized gaussian with dimentions 2*r+1
 */

cv::Mat gaussian_win(int r)
{

  cv::Mat tmp = cv::Mat::zeros(cv::Size(2*r+1, 2*r+1), CV_64FC1);

  for (int i = 0; i < tmp.rows; i++)
    for (int j = 0; j < tmp.cols; j++)
      tmp.at<double>(i,j) = exp(-(pow((r-i),2)+pow((j-r),2)) / (2*pow(r/2,2)));

  cv::Mat out;
  double s = cv::sum(tmp)[0];

  cv::multiply(tmp, 1/s, out);
  
  cv::imshow("gaussian", out);
  cv::waitKey(1);

  return out;
};
