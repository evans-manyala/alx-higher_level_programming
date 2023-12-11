#include "main.h"

int _putchar(char c)
{
  // Write the character to standard output using write system call.
  return write(1, &c, 1);
}
