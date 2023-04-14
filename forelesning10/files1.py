input_file_name = input("input file name: ")
output_file_name = input("output file name: ")

input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w")

total = 0.0
count = 0

line = input_file.readline()
while line != "":
    value = float(line)
    output_file.write("%15.2f\n" % value)
    total = total + value
    count = count + 1
    line = input_file.readline()

output_file.write("%15s\n" % "----------")
output_file.write("Total: %8.2f\n", total)
avg = total/count
output_file.write("Average: %6.2f\n" % avg)

input_file.close()
output_file.close()
