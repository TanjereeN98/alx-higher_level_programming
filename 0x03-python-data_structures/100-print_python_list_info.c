#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer PyObject
 */
<<<<<<< HEAD

=======
void print_python_list_info(PyObject *p)
{
	long int len;
	int i;
	PyListObject *l_obj;

	len = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < len; i++)
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
>>>>>>> 386effa1f63731606892071695db05d5aefd8260
