#!/usr/bin/env python
import sys


def main():
    """
    Calculator in Python

    Solves arbitrary arithmetic expressions in Python.
    """
    for s in sys.stdin:
        try:
            print(eval(s))
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()
