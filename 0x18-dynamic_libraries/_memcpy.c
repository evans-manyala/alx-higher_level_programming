#include "main.h"

char *_memcpy(char *dest, char *src, unsigned int n)
{
	// Copy n bytes from src to dest.
	for (unsigned int i = 0; i < n; i++)
	{
		dest[i] = src[i];
	}
	return (dest);
}
