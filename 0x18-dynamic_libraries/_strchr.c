#include "main.h"

char *_strchr(char *s, char c) {
  // Loop through characters until the desired character or null terminator is found.
  while (*s && *s != c) {
    s++;
  }
  return ((*s == c) ? s : NULL);
}
