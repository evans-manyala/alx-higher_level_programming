#include "main.h"

int _atoi(char *s)
{
	int num = 0;
	int sign = 1; // Positive sign by default.
	
	// Check for negative sign.
	
	if (*s == '-')
	{
		sign = -1;
		s++; // Skip the sign.
	}
	
	// Loop through digits and convert them to number.
	while (*s && _isdigit(*s))
	{
		num = 10 * num + (*s - '0');
		s++;
  	}
	return (num * sign);
}
