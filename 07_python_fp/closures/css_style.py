import copy
from collections.abc import Callable


def css_styles(initial_styles: dict) -> Callable[[str, str, str], dict]:
    initial_styles_cp = copy.deepcopy(initial_styles)

    def add_style(selector: str, property: str, value: str) -> dict:
        if selector not in initial_styles_cp:
            initial_styles_cp[selector] = {}
        initial_styles_cp[selector][property] = value
        return initial_styles_cp

    return add_style
