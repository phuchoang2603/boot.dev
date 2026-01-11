def configure_plugin_decorator(func):
    def wrapper(*args):
        args_dict = dict(args)
        return func(**args_dict)

    return wrapper
