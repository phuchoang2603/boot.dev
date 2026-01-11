def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        match option:
            case "--one":
                return filter_one(content)
            case "--two":
                return filter_two(content)
            case "--three":
                return filter_two(filter_one(content))
            case _:
                raise Exception("invalid option")

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
