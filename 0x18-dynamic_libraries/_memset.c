#include "main.h"

char * _memset(char * s, char b, unsigned int n)
{
        // Fill n bytes of s with the character b.
        for (unsigned int i = 0; i < n; i++)
        {
                s[i] = b;
        }
        return (s);
}
