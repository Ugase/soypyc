import token
import tokenize

table = token.tok_name

for i in tokenize.tokenize(open("/home/denzel/Dev/mathematics.py", "rb").readline):
    length = f"{i.start},{i.end}".__len__()
    spacing = 21 - length
    space1 = " " * spacing
    space2 = " " * (21 - f"{table[i.type]}".__len__())
    print(f"{i.start},{i.end}{space1}{table[i.type]}{space2}{i.string}")
#    if i.string == "def":
#        print(f"Function on line {i.start[0]}")
