#include <stdio.h>
#include <sys/types.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <assert.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: the list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	int j = 0;
	Py_ssize_t size;
	PyObject *ob;

	if (p == NULL)
		return;
	size = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated = %d\n", (int)size);
	while (i < size)
	{
		ob = PyList_GET_ITEM(p, i++);
		if (ob != NULL)
			printf("Element %d: %s\n", j++, ob->ob_type->tp_name);
	}
}
