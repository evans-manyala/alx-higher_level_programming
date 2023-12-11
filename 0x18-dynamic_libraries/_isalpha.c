#include "main.h"

int _isalpha(int c) 
{
	// Check if the character is either lowercase or uppercase.
	return ((_islower(c) || _isupper(c)));
}
