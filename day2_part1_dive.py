#!/bin/python3

def dive(filename_in, err_out = False):
    file = open(filename_in, 'r')
    lines = file.readlines()
    line_len = len(lines)
    # measurements
    horiz = 0
    depth = 0
    # error creation
    err = ""
    for line in range(line_len):
        split = lines[line].split(" ")
        err += lines[line][:-1]
        if(split[0] == "forward"):
            horiz += int(split[1])
            err += " | horizontal increased by " + str(split[1][:-1]) + " to " + str(horiz) + "\n"
        elif(split[0] == "up"):
            depth -= int(split[1])
            err += " | depth decreased by " + str(split[1][:-1]) + " to " + str(depth) + "\n"
        else:
            depth += int(split[1])
            err += " | depth increased by " + str(split[1][:-1]) + " to " + str(depth) + "\n"
    if(err_out):
        print(err)
    print("Horizontal position is " + str(horiz))
    print("Depth is " + str(depth))
    return (horiz, depth)

if __name__ == "__main__":
    print(dive("day2_input.txt", True))
