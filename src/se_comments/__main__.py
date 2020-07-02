import sys
from typing import Iterator

from . import main

if __name__ == "__main__":
    try:
        message = main(sys.argv[1])
        print(f"{len(message)} / 600  ")
        print(message)
    except core.CommentError as e:
        print("!", e)
        raise SystemExit(1) from None
