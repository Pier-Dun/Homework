from inspect import getmodule


def introspection_info(obj):
    attr = [m for m in dir(obj) if not callable(getattr(obj, m))]
    met = [m for m in dir(obj) if callable(getattr(obj, m))]
    inf = {'type': type(obj), 'methods': met, 'attribute': attr, 'module': getmodule(obj)}
    return inf

number_info = introspection_info(42)
print(number_info)