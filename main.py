import builtins
import keyword
import sys
import token
import tokenize
import types

builtin_function_names = [
    name
    for name, obj in vars(builtins).items()
    if isinstance(obj, types.BuiltinFunctionType)
]
space = ["for", "else", "elif", "if", "def", "return", "import"]
double = ["in"]

try:
    debug = sys.argv[1] == "debug"
except:
    debug = False


class Theme:
    def __init__(self, colors: dict) -> None:
        """
        colors default:
        
        {
            "STRING": "\\033[32m",
            "NUMBER": "\\033[33m",
            "KEYWORD": "\\033[95m",
            "NORMAL": "\\033[0m"
        }
        """,
        color = {
            "STRING": "\033[32m",
            "NUMBER": "\033[33m",
            "KEYWORD": "\033[95m",
            "NORMAL": "\033[0m",
            "BULITIN": "\033[94m",
        }
        self.colors = color | colors


def apply_color(theme: Theme, key: str, hi: str):
    return theme.colors[key] + hi + theme.colors["NORMAL"]


def parse(filename: str, theme: Theme):
    table = token.tok_name
    for i in tokenize.generate_tokens(open(filename).readline):
        if debug:
            print(i.string, i.type, table[i.type], i.start, i.end, i.line, sep=", ")
            continue
        if table[i.type] == "STRING":
            print(apply_color(theme, "STRING", i.string), end="")
        elif keyword.iskeyword(i.string):
            content = apply_color(theme, "KEYWORD", i.string)
            if i.string in space:
                print(content + " ", end="")
                continue
            if i.string in double:
                print(" ", content, " ", end="")
                continue
            print(content, end="")
        elif table[i.type] == "NUMBER":
            print(apply_color(theme, "NUMBER", i.string), end="")
        elif i.string in builtin_function_names:
            print(apply_color(theme, "BULITIN", i.string), end="")
        else:
            print(i.string, end="")


parse("test.py", Theme({}))
