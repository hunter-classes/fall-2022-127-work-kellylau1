#include <iostream>


/*
  This is a multi line
  comment
  to compile:
  g++ main.cpp
  ./main

 */

void absoluteValue(int num)
{
    if (num < 0) {
      std::cout << "The absolute value of " << num << " is " << abs(num)<< ". "<< std::endl;
    }
    else if (num > 0){
      std::cout << "The absolute value of " << num << " is " << num<< ". " << std::endl;
    }
}
 
int main() {
  std::cout << "Hello World!" << std::endl;
  
  for (int num=1; num <= 25; ++num) {
    std:: cout << num << " "<< std::endl;{
      
    }
    std:: cout << "Hello there!"<< std::endl;{
      
    }
  }
  
  absoluteValue(-20);
  
  return 0;
}