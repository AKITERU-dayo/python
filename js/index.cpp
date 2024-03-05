#include <iostream>
#include <windows.h>

wchar_t keys{};
bool loop = false;

void func(int i);

int main(void)
{
  std::cout << "I'm perfect nuts" << std::endl;
  loop = true;
}

void func(int i)
{
  while(loop)
  {
    OutputDebugStringA("s set test");
  }
}