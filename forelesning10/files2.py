infile = open("files/input.txt", "r")

for line in infile:
    print(line)
    line = line.rsplit("l")
    print(line)
infile.close()