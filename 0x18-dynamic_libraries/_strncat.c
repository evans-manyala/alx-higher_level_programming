char *_strncat(char *dest, char *src, int n) {
  int i = 0; // Destination index.

  // Find the null terminator in the destination.
  while (dest[i]) {
    i++;
  }

  // Append at most n characters from the source.
  int j = 0;
  while (src[j] && j < n) {
    dest[i++] = src[j++];
  }

  // Add null terminator to the end.
  dest[i] = '\0';
  return dest;
}
