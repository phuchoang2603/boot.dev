from collections.abc import Callable


def new_collection(initial_docs: list[str]) -> Callable[[str], list[str]]:
    initial_docs_cp = initial_docs.copy()

    def add_doc(doc: str) -> list[str]:
        initial_docs_cp.append(doc)
        return initial_docs_cp

    return add_doc
