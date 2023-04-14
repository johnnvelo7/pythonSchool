input_file_name = input("input file name: ")
output_file_name = input("output file name: ")

input_file = open(input_file_name, "r")

line = input_file.readline()
while line != "":
    value = float(line)
    output_file.write("%15.2f\n" % value)
    total = total + value
    count = count + 1
    line = input_file.readline()