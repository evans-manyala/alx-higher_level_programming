int _strlen(char *s) {
  int count = 0;
  // Loop through characters until null terminator is reached.
  while (*s) {
    count++;
    s++;
  }
  return count;
}
