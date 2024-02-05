#!/usr/bin/python3
import os, glob, subprocess, datetime

#Amount
all_media=0
halfshows=0
fullshows=0
movies=0
dvd=0
bluray=0
#Length
halfshows_list=[]
fullshows_list=[]
movies_list=[]
total_list=[]
#Size
halfshows_size_list=[]
fullshows_size_list=[]
#movies_size_list=[]
dvd_size_list = []
bluray_size_list = []
total_size_list = []

def get_length(video):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", video],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def avg_duration(time_list):
    try:
        avg = sum(time_list) / len(time_list)
    except ZeroDivisionError:
        avg = 0
    return str(datetime.timedelta(seconds=avg)) # Return the average time in proper format

def total_duration(time_list):
    total = sum(time_list)
    return str(datetime.timedelta(seconds=total)) # Return the average time in proper format

def avg_size(size_list):
    try:
        avg = sum(size_list) / len(size_list)
    except ZeroDivisionError:
        avg = 0
    avg = format_bytes(avg)
    return str(avg) # Return the average time in proper format


def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    size = '{0:.2f}'.format(size)
    return size + " " + power_labels[n]

# "." can be replaced with full path like /home/user/Desktop/files
for filename in glob.iglob('./**/*.mkv', recursive=True):
    all_media=all_media+1
    if get_length(filename) < 1800: #30 minutes or less
        halfshows+=1
        halfshows_list.append(get_length(filename))
        halfshows_size_list.append(os.path.getsize(filename))
        total_list.append(get_length(filename))
        total_size_list.append(os.path.getsize(filename))
    elif get_length(filename) > 1800 and get_length(filename) < 3600: #30 minutes to 1 hour
        fullshows+=1
        fullshows_list.append(get_length(filename))
        fullshows_size_list.append(os.path.getsize(filename))
        total_list.append(get_length(filename))
        total_size_list.append(os.path.getsize(filename))
    else: # above an hour is considered a movie
        movies+=1
        movies_list.append(get_length(filename))
        total_list.append(get_length(filename))
        total_size_list.append(os.path.getsize(filename))
        #movies_size_list.append(os.path.getsize(filename))
        if os.path.getsize(filename) > 10737418240:
            bluray+=1
            bluray_size_list.append(os.path.getsize(filename))
        else:
            dvd+=1
            dvd_size_list.append(os.path.getsize(filename))


print("Amount of Media: " + str(all_media))
print("Sub-30:          " + str(halfshows))
print("Super-30:        " + str(fullshows))
print("Movies:          " + str(movies))
print("DVDs:            " + str(dvd))
print("Blu-rays:        " + str(bluray))
print("Average sub-30 show duration:   " + avg_duration(halfshows_list))
print("Average super-30 show duration: " + avg_duration(fullshows_list))
print("Average movie duration:         " + avg_duration(movies_list))
print("Average sub-30 show size:       " + avg_size(halfshows_size_list))
print("Average super-30 show size:     " + avg_size(fullshows_size_list))
print("Average DVD size:               " + avg_size(dvd_size_list))
print("Average Blu-ray size:           " + avg_size(bluray_size_list))
print("Total media duration:           " + total_duration(total_list))
print("Total media(Show/Movies) size:  " + str(format_bytes(sum(total_size_list))))