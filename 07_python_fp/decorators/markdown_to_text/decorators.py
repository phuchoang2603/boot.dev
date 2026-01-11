def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = tuple(map(convert_md_to_txt, args))
        converted_kwargs = dict(
            map(lambda tup: (tup[0], convert_md_to_txt(tup[1])), kwargs.items())
        )
        return func(*converted_args, **converted_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
