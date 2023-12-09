#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int x;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (x = 0; x <= size && x < 10; x++)
		printf(" %02hhx", str[x]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int x;
	PyListObject *list = (PyListObject *)p;
	const char *obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (x = 0; x < size; x++)
	{
		obj = (list->ob_item[x])->ob_type->tp_name;
		printf("Element %i: %s\n", x, obj);
		if (!strcmp(obj, "bytes"))
			print_python_bytes(list->ob_item[x]);
	}
}
