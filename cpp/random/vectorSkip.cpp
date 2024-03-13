#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

int jumpingOnClouds(vector<int> c) {

    int jumps = 0;
    vector<int>::iterator it;

    for (it = c.begin()+1; it != c.end(); ++it) {

      jumps++;
      
      if (*(next(it,1)) == 0 && next(it,1) != c.end()) ++it;
      
    }

    return jumps;
}


int main(int argc, char *argv[])
{

  vector<int> v{0, 0};

  cout << jumpingOnClouds(v) << endl;
  
  
  return 0;
}
