#!/bin/python3

def dive_aim(filename_in, err_out = False):
    file = open(filename_in, 'r')
    lines = file.readlines()
    lines_len = len(lines)
    # build error
    err = ""
    # build positions and aim
    horiz = 0
    depth = 0
    aim = 0
    # start reading commands
    for line in range(len(lines)):
        err += lines[line][:-1]
        split = lines[line].split(" ")
        if(split[0] == "forward"):
            horiz += int(split[1])
            depth += (int(split[1]) * aim)
            err += (" | changing horiz by " + split[1][:-1] + 
            " to " + str(horiz) + " aim is " + str(aim) + 
            " so depth changes by " + str(int(split[1]) * aim) + " to " + str(depth) + "\n")
        elif(split[0] == "up"):
            aim -= int(split[1])
            err += " | aim decreased by " + split[1][:-1] + " to " + str(aim) + "\n"
        else:
            aim += int(split[1])
            err += " | aim increased by " + split[1][:-1] + " to " + str(aim) +"\n"
    if(err_out):
        print(err)
    print("Horizontal position is " + str(horiz))
    print("Depth is " + str(depth))

    return (horiz, depth)

if __name__ == "__main__":
    dive_aim("day2_input.txt", True)
