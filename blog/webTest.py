import inspect


def f(a, c=1, *b, d=1, e, **f):
    pass


sig = inspect.signature(f)
params = sig.parameters
for name, param in params.items():
    if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
        print('default',name)
    if param.kind == inspect.Parameter.KEYWORD_ONLY:
        print(name)
