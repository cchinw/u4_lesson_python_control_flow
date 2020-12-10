# Python Control Flow

## Overview

We'll be learning and implementing python control flow, and proper `indententation`.

## If/Else/ElIf

In python, we can perform logic utilizing `if`, `elif`, and `else` statements to check a condition. Each statement creates a `block`, and each block must be indented correctly or our code will fail to run. Whatever is decalared inside of this block is only accessible within that `scope`. Common indentation in python is typically 1 tab or 2 spaces, here's an example:

```python
if 5 > 2:
    print('Yay')
elif 5 > 3:
    print('Ohhh')
else:
    print('Whoops')
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

<table>
    <tr>
        <th>Javascript</th>
        <th>Python</th>
        <th>Operation</th>
    </tr>
    <tr>
        <td>!==</td>
        <td>!=</td>
        <td>Not Equal</td>
    </tr>
    <tr>
        <td>===</td>
        <td>==</td>
        <td>Equals</td>
    </tr>
    <tr>
        <td>></td>
        <td>></td>
        <td>Greater Than</td>
    </tr>
    <tr>
        <td><</td>
        <td><</td>
        <td>Less Than</td>
    </tr>
    <tr>
        <td>>=</td>
        <td>>=</td>
        <td>Greater Than Or Equal</td>
    <tr>
        <td><=</td>
        <td><=</td>
        <td>Less Than Or Equal</td>
    </tr>
    <tr>
        <td>!</td>
        <td>not</td>
        <td>Logical Not</td>
    </tr>
    <tr>
        <td>&&</td>
        <td>and</td>
        <td>Logical And</td>
    </tr>
    <tr>
        <td>||</td>
        <td>or</td>
        <td>Logical Or</td>
    </tr>
</table>

Utilizing the above table, work in the `check_gpa` function in `main.py` and follow the instructions.

Run the `test_gpa.py` file to test your logic: `python3 test_gpa.py`. If everything is correct you'll have an `ok` message printed to your terminal.
