char *_strncpy(char *dest, char *src, int n)
{
	int i;
	
	// Copy at most n characters from the source.
	for (i = 0; i < n && src[i]; i++)
	{
		dest[i] = src[i];
	}
	return dest;
}
