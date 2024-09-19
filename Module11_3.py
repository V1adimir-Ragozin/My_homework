import inspect
from pprint import pprint
from types import ModuleType
from typing import Union, Any


def introspection_info(obj):
    result: dict[str, Union[Union[str, list[str], ModuleType, None], Any]] = {
        'Type': type(obj),
        'Attribute': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'Method': [method for method in dir(obj) if callable(getattr(obj, method))],
        'Module': inspect.getmodule(obj),
        'Module_name': introspection_info.__module__,
        'Func_name': introspection_info.__name__,
        'id_object': id(obj)
    }
    return result


class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.info()

    def info(self):
        print(f'My name {self.name}, I am a {self.school} student')


number_info1 = introspection_info(42)
pprint(number_info1)
print()
print('----------------------------------------------------------------------------')
print()
number_info2 = introspection_info(Student('Vyacheslav', 'Urban university'))
pprint(number_info2)
