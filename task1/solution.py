from functools import wraps
from inspect import signature


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        type_hints = func.__annotations__
        params = signature(func).parameters
        bound_args = signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        for param_name, value in bound_args.arguments.items():
            expected_type = type_hints.get(param_name)
            if expected_type and not isinstance(value, expected_type):
                error_message = f"Аргумент {param_name} должен соответствовать типу данных {expected_type.__name__}, а был получен тип данных {type(value).__name__} со значением {value}"
                raise TypeError(error_message)
        result = func(*args, **kwargs)
        return result
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

try:
    print(sum_two(1, 2))
    print(sum_two(1, 2.4))
except TypeError as err:
    print(f"Ошибка: {err}")