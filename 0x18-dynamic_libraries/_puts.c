#include "main.h"

void _puts(char *s) {
  // Loop through characters and call _putchar for each.
  while (*s) {
    _putchar(*s);
    s++;
  }
  _putchar('\n');
}
