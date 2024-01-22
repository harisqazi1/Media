#!/usr/bin/python3
import argparse
import re
from datetime import date, datetime
import tempfile
import os
import sys

parser = argparse.ArgumentParser(
                    prog='Subtitle Shift',
                    description='Allows you to shift a subtitle, even in the negative space (for subtitles you want sooner)',
                    epilog='- Haris Qazi')
parser.add_argument('filename')           # positional argument
parser.add_argument('-t', '--time', help='How much do you want to shift by. (+/_)00:00:00,000 format.')
parser.add_argument('-o', '--output', help='Name of output file.')
args = parser.parse_args()

output_file = open(args.output, "w") #Use for output
temp = tempfile.TemporaryFile(mode='w+t') #A temporary file to write to before final changes are made

def shift(filename, user_time): #direction = shift back or shift forward; time is how much you want to do it by.
    regex=r"^\d\d:\d\d:\d\d,\d\d\d\s-->\s\d\d:\d\d:\d\d,\d\d\d$" #00:00:00,000 --> 00:00:00,000 format
    file = open(filename,'r')
    time_one = datetime.strptime('00:00:00,000011', '%H:%M:%S,%f') #See Issues section for info on this
    while True:
        next_line = file.readline()
        if not next_line:
            break;
        if re.match(regex, next_line):
            for each_word in next_line.split(): #whitespace split
                if re.match(r"\d\d:\d\d:\d\d,\d\d\d", each_word):
                    original_time = datetime.strptime(each_word, "%H:%M:%S,%f")
                    shift_direction=user_time[0] #Delay or speed up subtitle binary (+/-)
                    actual_time_shift=user_time[1:]
                    modified_time = datetime.strptime(actual_time_shift, "%H:%M:%S,%f")
                    delta=0
                    if shift_direction=='+':
                        delta = (original_time - time_one +  modified_time).time()
                    else:
                        delta = original_time-modified_time
                    #Using [:-3 to remove 3 extra spaces at the end to make it into original format]
                    delta=str(delta)[:-3] #str is used to bypass TypeError: expected string or bytes-like object
                    if re.match(r"-\d\sday", delta): #match -1 day, to prevent having negative time stamp
                        break
                    if re.match(r"^\d:", delta): #To add one 0 to the beginning, if strptime removed it
                        delta = "0" + str(delta)
                    #print(delta, end='') #print without new line
                    temp.writelines(str(delta))
                else:
                    #print(" " + each_word + " ", end='')
                    temp.writelines(" " + each_word + " ")
        else:
            #print('\n' + next_line.strip())
            temp.writelines('\n' + next_line.strip() + "\n")

def cleanup(temporary_file, output_file_name):
    temporary_file.seek(0)
    content = temporary_file.read()
    content = re.sub(r"[\uFEFF]", "", content, re.M)
    content = re.sub(r"\d\n\n[ -~]{0,}\n\n", r"", content, re.M) #Remove all lines where no time is printed (for negative times)
    content = re.sub(r"\n\n\n", r"\n", content, flags=re.M) #After 10 there was a extra lines
    content = re.sub(r"[\uFEFF]", "", content, re.M) #Super specific regex, but was to remove a unicode char
    output_file_name.write(content)
    #print(content, end='')

#This only validates for time, they fail some use cases
def input_validation(time):
    if bool(re.match(r"[\+\_]\d\d\:\d\d\:\d\d,\d\d\d", time)) == False:
        print("ERROR: String does not match expected format")
        sys.exit()

input_validation(args.time)
shift(args.filename,args.time)
cleanup(temp, output_file)

#Close files
output_file.close()
temp.close()
