# Hacker Hour 2019 - Python 3

The code inside `calculator.py` solves arbitrary arithmetic expressions in Python

# Usage

On any Linux machine with Python installed, run:

`./calculator.py`

Then, input your arithmetic expressions into stdin (the results will be printed out). Press Ctrl-c to exit the program.

# Architecture

OK fine, I cheated a bit! I was initially going to write a regex to match expressions and then solve them like that, but eventually lost patience with making the regex work. This uses the `eval` function in Python.

The [eval](https://docs.python.org/3/library/functions.html#eval) function in Python takes any string and basically treats it as its own Python program. Case in point, if you run `eval("1 + 2")`, it would be like typing in "1 + 2" in the Python REPL.
