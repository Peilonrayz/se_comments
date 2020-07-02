import functools
from typing import Iterator

NORMALIZE_TABLE = str.maketrans("", "", " \n\t\r")


def normalize_name(name):
    return name.translate(NORMALIZE_TABLE).casefold()


def english_join(values, oxford=False, sep=", ", conj="and "):
    if 1 < len(values):
        if oxford:
            values[-1] = conj + values[-1]
        else:
            values[-1] = values[-2] + " " + conj + values.pop()
    return sep.join(values)


class CommentError(Exception):
    pass


class ValuedInt(int):
    def __new__(self, value, /, *_, **__):
        return super().__new__(self, value)

    def __init__(self, value, /, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def flag_field(value, **kwargs):
    def inner(fn):
        return ValuedInt(value, fn=fn, **kwargs)

    return inner


class Namespace:
    def validate(self):
        return self

    def format(self, values):
        return [
            value.value.fn(self, values.get(value, ()))
            for value in type(self)
            if self & value
        ]

    @classmethod
    def names(cls):
        return {
            normalize_name(name): value
            for value in cls
            for name in getattr(value.value, "names", ())
        }

    @classmethod
    def _apply_names(cls, items):
        NAMES = cls.names()
        for key, value in items:
            try:
                yield NAMES[normalize_name(key)], value
            except KeyError:
                raise CommentError(f"Unknown input {key!r}")

    @classmethod
    def get_items(cls, keys):
        keys = iter(keys)
        ret = next(keys, cls.NONE)
        for key in keys:
            ret |= key
        return ret

    @classmethod
    def apply_names(cls, items):
        mapping = dict(cls._apply_names(items))
        return mapping, cls.get_items(mapping.keys())

    @classmethod
    def formap(cls, items):
        mapping, enum = cls.apply_names(items)
        return enum.validate().format(mapping)


def parse(text: Iterator[str]):
    text = iter(text)
    tokens = []
    token = [None, ()]
    stack = []
    for char in text:
        if char == "\\":
            stack.append(next(text))
            continue
        if char in ",[":
            token[0] = "".join(stack).strip()
            stack = []
            if char == "[":
                token[1] = parse(text)
            if token[0] or token[1]:
                tokens.append(token)
            token = [None, ()]
        elif char == "]":
            break
        else:
            stack.append(char)
    if stack:
        token[0] = "".join(stack).strip()
        if token[0]:
            tokens.append(token)
    return [(token, tuple(values)) for token, values in tokens]
