import traceback
### Try catch Function For find line Number
try:
    00000/0000000
except:
    print(traceback.format_exc())
### First Line Catch
def firstline():
    lines = []
    with open(r"t1.txt", 'r') as fp:
        lines = fp.readlines()
    with open(r"t1.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number != 0:
                fp.write(line)
    return lines[0].replace("\n","")
