import inspect

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


def introspection_info(obj):
    info = {}

    # Получаем тип объекта
    info['type'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes


    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods


    info['module'] = getattr(obj, '__module__', '__main__')


    return info



number_info = introspection_info(42)
print(number_info)


my_obj = MyClass(10)
class_info = introspection_info(my_obj)
print(class_info)