#include "main.h"

char *_strcat(char *dest, char *src) {
  int i = 0; // Destination index.

  // Find the null terminator in the destination.
  while (dest[i]) {
    i++;
  }

  // Append source string to the end of destination.
  int j = 0;
  while (src[j]) {
    dest[i++] = src[j++];
  }

  // Add null terminator to the end.
  dest[i] = '\0';
  return dest;
}
