#include <iostream>
#include <sstream>

using namespace std;

void printx(int n)
{
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {

      // diagonal top left to lower right
      if (i == j) cout << "#";
      // border
      else if (i == 0      || j == 0 ||
	       i == n-1 || j == n-1) cout << "#";
      // diagonal lower left to top right
      else if (i == n-1-j) cout << "#";
      else cout << " ";

    }
    cout << "\n";
  }
};

void fizzbuzz(int n)
{
  
  for (int i = 1; i < n; i++) {

    stringstream s;
    s << "";
    
    if (i % 3 == 0) s << "Fizz";
    if (i % 5 == 0) s << "Buzz";

    if (s.str() == "") s << i;
    
    cout << s.str() << "\n";
  }
  

};

int main(int argc, char *argv[])
{

  printx(11);
  fizzbuzz(16);

  return 0;
}



