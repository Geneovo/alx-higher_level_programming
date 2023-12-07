#include <stdio.h>

struct timespec;

#include <Python.h>
#include <object.h>
#include <bytesobject.h>
#include <time.h>

/**
 * print_python_bytes - prints bytes informaton
 *
 * @p: Python Object
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, x, end;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		end = 10;
	else
		end = size + 1;
	printf("  first %ld bytes:", end);

	for (x = 0; x < end; x++)
		if (str[x] >= 0)
			printf(" %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);
	printf("\n");
}

/**
 * print_python_list - prints list information
 *
 * @p: Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, x;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python List info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		obj = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
