# Python Control Flow

## Overview

We'll be learning and implementing python control flow, and proper `indententation`.

## If/Else/ElIf

In python, we can perform logic utilizing `if`, `elif`, `else` statements to check for a condition. Each statement is a `block`, and each block must be indented correctly or our code will fail to run. Common indentation in python is typically 1 tab or 2 spaces, heres an example:

```python
if 5 > 2:
    print('Yay')
```

Notice the syntax, in Python we use the `:` symbol to indicate the end of our condition. The code after is indented to declare a `block` or `scope`.

Here's a comparison between javascript if's and python if's:

| Javascript              | Python            |
| ----------------------- | ----------------- |
| `if(something){}`       | `if something:`   |
| `else if (something){}` | `elif something:` |
| `else {}`               | `else:`           |

As you can see they're quite similar, but syntactically different.

## `And`'s `Not`'s and Everything Else

Python also has comparison operators such as `<` and `>`. Here's a list of python's comparison and logical operators with their js counterparts:

| Javascript | Python | Operation             |
| ---------- | ------ | --------------------- | --- | ---------- |
| !==        | !=     | Not Equal             |
| ===        | ==     | Equals                |
| >          | >      | Greater Than          |
| <          | <      | Greater Than          |
| >=         | >=     | Greater Than Or Equal |
| <=         | <=     | Less Than Or Equal    |
| !          | not    | Logical Not           |
| &&         | and    | Logical And           |
| `          |        | `                     | or  | Logical Or |

Utilizing the above table, work in the `check_gpa` function in `main.py` and follow the instructions.

Run the `test_gpa.py` file to test your logic: `python3 test_gpa.py`. If everything is correct you'll have an `ok` message printed to your terminal.
