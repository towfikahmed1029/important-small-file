def firstline():
    lines = []
    with open(r"t1.txt", 'r') as fp:
        lines = fp.readlines()
    with open(r"t1.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number != 0:
                fp.write(line)
    return lines[0].replace("\n","")
