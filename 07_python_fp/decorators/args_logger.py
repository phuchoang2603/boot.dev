def args_logger(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"{index}. {arg}")
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")
