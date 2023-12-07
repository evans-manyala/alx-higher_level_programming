#include <python.h>
#include <string.h>
#include <stdio.h>

/**
 * print_python_list - Prints list information
 * @p: Pointer to the python Object
 * Return: void no return value
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, x;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (x = 0; x < size; ++x)
	{
		item = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints bytes information
 * @p: Pointer to the python Object
 * Return: void no return value
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, x;
	char *data;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);
	printf("  first %ld bytes:", (size > 10) ? 10 : size);

	for (x = 0; x < size && x < 10; ++x)
		printf(" %02hhx", data[x]);
	printf("\n");
}
