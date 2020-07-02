from . import core, namespaces
from .core import CommentError

__all__ = [
    "CommentError",
    "main",
]


def main(arg):
    return " ".join(namespaces.Core.formap(core.parse(arg)))
