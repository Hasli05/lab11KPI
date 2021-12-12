lines_set = set()

with open(r"input.txt", "r") as fin, open(r"output.txt", "w") as fout:
    for line in fin:
        if line not in lines_set:
            fout.write(line)
        lines_set.add(line)
