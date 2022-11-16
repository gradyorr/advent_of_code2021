#!/bin/python3
import sys

# sonar sweep
# give nthe measurements of depth between lines,
# print if the measurement went up or down.
# given in: file to read from, file to write to
def sonar_sweep(filename_in, filename_out):
    file = open(filename_in, 'r')
    previous = -1
    increase_counter = 0
    decrease_counter = 0
    same_counter = 0
    out = "(N/A - no previous measurement)\n"
    for line in file:
        if(previous > 0 and (int(line) > previous)):
            out = out + "(increased)\n"
            increase_counter += 1
        elif (previous > 0 and (int(line) < previous)):
            out = out + "(decreased)\n"
            decrease_counter += 1
        else:
            out = out + "(constant)\n"
            same_counter += 1
        previous = int(line)
    out_file = open(filename_out, 'w')
    out_file.write(out)
    print("[increased, decreased, same]")
    return [increase_counter, decrease_counter, same_counter]

# Same idea as the last program but measure in pairs of 3
# observations. A = (1,2,3), B = (2,3,4), C = (4,5,6)...
# print if the measurement is greater or lesser than the 
# previous measurement
# given: files to read in and write out to
def rolling_sweep(filename_in, filename_out, err_out = False):
    file = open(filename_in, 'r')
    lines = file.readlines()
    lines_len = len(lines)
    out = ""
    err = ""
    # track the previous data point
    previous = -1
    # track the index to skip
    skip = 1
    # measure the trends of the data
    trends = [0,0,0]
    # measure the number of additions
    counters = [0,0,0,0]
    # measure the total counts of the current variables
    totals = [0,0,0,0]
    for line in range(lines_len):
        # for each result reported in the file
        err += lines[line][:-1] + " "
        # add to the slots in this iteration
        for i in range(len(totals)):
            if not ((i==skip) or ((line < 2) and (i > skip))):
                totals[i] += int(lines[line])
                counters[i] += 1
                err += str(i) + " "
            else:
                err += "* "
        # find targets with counters > 3
        curr_target = -1
        try:
            curr_target = counters.index(3)
        except:
            curr_target = -1
        if(curr_target >= 0):
            if(previous < 0):
                # initial setting of 'previous'
                out += "(NA)\n"
                err += " NA"
            else:
                # previous was set.
                if(totals[curr_target] > previous):
                    out += "(increased)\n"
                    err += str(totals[curr_target]) + " +\n"
                    trends[0] += 1
                elif(totals[curr_target] < previous):
                    out += "(decreased)\n"
                    err += str(totals[curr_target]) +  " -\n"
                    trends[1] += 1
                else:
                    out += "(same)\n"
                    err +=  str(totals[curr_target]) + " =\n"
                    trends[2] += 1
            previous = totals[curr_target]
            totals[curr_target] = 0
            counters[curr_target] = 0
        # end target logic
        skip = (skip+1) % 4
    out_file = open(filename_out, 'w')
    out_file.write(out)
    if(err_out):
        print(err)
    print("[increased, decreased, same]")
    return trends

# we do a little testing
def test_length():
    values = [0] * 15
    len_values = len(values)
    for i in range(len_values):
        print(i < 2 or i > (len_values - 3))

if __name__ == "__main__":
    print(rolling_sweep("day1_input.txt", "day1_output_part2.txt"))
    print(sonar_sweep("day1_input.txt", "day1_output_part1.txt"))
