#/usr/bin/python3
import re #for checking user input format
import math
import argparse

parser = argparse.ArgumentParser(
                    prog='storage_estimat-inator.py',
                    description='Approximates how much media can be stored on a specific storage size',
                    epilog='- Haris Qazi')
parser.add_argument('Number')
parser.add_argument('Bytes')
args = parser.parse_args()

user_input = (str(args.Number) + " " +  args.Bytes)
splitted_input = user_input.split(" ")

#User input check
pattern = re.compile("^[0-9]{0,3}([.][0-9]{1,4})?\s\w\w")
if not pattern.match(user_input):
    print("Regex doesn't match the following: 10 MB, 20 TB")
    exit()
# add splitted input check here
if splitted_input[1] not in ["KB","MB","GB","TB","PB", "EB"]:
    print("Following are supported: KB, MB, GB, TB, PB, EB")
    exit()

# Assigning byte values to the units - these are in binary, not decimal
# These are Real capacity - since people buy based on claimed
bytes_values = {
    'KB' : (1000 * 0.9765625),           #1000 Claimed capacity / 1024 (now bytes)
    'MB' : (1000000 * 0.953674316),         #1000000 Claimed capacity / 1024 (now KB) / 1024 (now bytes)
    'GB' : (1000000000 * 0.931322575),         #1000000000 Claimed capacity /1024 (now MB) / 1024 (KB) / 1024 (bytes)
    'TB' : (1000000000000 * 0.909494702),         #1000000000000 CC / 1024 (GB) / 1024 /1024 /1024
    'PB' : (1000000000000000 * 0.88817842),          #1000000000000000 CC / 1024 (5 times)
    'EB' : (1000000000000000000 * 0.867361738)          #1000000000000000000 CC / 1024 (6 times)
}

#User input converting to bytes
user_to_bytes = (float(splitted_input[0]) * float(bytes_values[splitted_input[1]]))

#Outputting real capacity
#Dividing by 1000 to return to decimal standard, allowing for 1:1 correlation between input and real capacity on drive
print("----------------------------------------------------------------------")
if splitted_input[1] == "KB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 1)), splitted_input[1])) #Bytes to KB
if splitted_input[1] == "MB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 2)), splitted_input[1])) #Bytes to KB
if splitted_input[1] == "GB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 3)), splitted_input[1])) #Bytes to KB
if splitted_input[1] == "TB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 4)), splitted_input[1])) #Bytes to KB
if splitted_input[1] == "PB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 5)), splitted_input[1])) #Bytes to KB
if splitted_input[1] == "EB":
    print("Real capacity for %s is %s %s" % (user_input ,(user_to_bytes / (1000 ** 6)), splitted_input[1])) #Bytes to KB
print("----------------------------------------------------------------------")
# This is in bytes - to make math easier (Mebibytes, Gibibytes, etc) (2^X basically)
# Storage size is basically decimal size to binary bytes size
# Ex. 10 MB = 10000000 in decimal but 10485760 in Binary (1000 vs 1024)
data_storage = {
    "character in text file" : 1,                        #1 character = 1 byte
    "MP3 Song File" : 10485760,                          #10 MB 
    "DVD" : 4294967296,                                  #4 GB
    "DVD Backup" : 8589934592,                           #8 GB
    "Blu-ray Disc" : 26843545600,                        #25 GB
    "Ultra HD Blu-ray" : 59055800320,                    #55 GB
    "Ultra HD Blu-ray Backup" : 67967857459.2,           #63.3 GB
    "Video Game" : 85899345920,                          #80 GB
    "480p x264 Movie(s)" :  576716800.25,                #550 MB
    "720p x264 Movie(s)" :  1493172224.18,               #1.39 GB
    "1080p x264 Movie(s)" : 3758096384,                  #3.5 GB
    "2K (1440p) x264 Movie(s)" : 6442450944,             #6 GB
    "UHD (4K) x264 Movie(s)" : 15032385536,              #14 GB
    "8K x264 Movie(s)" : 64424509440,                    #60 GB
    "480p x265 Movie(s)" :  419430400.18,                #400 MB
    "720p x265 Movie(s)" : 1119879168.135,               #1.12 GB
    "1080p x265 Movie(s)" : 2952790016,                  #2.75 GB
    "2K (1440p) x265 Movie(s)" : 5368709120,             #5 GB
    "UHD (4K) x265 Movie(s)" : 11274289152,              #10.5 GB
    "8K x265 Movie(s)" : 51002736640,                    #47.5 GB
    "480p x264 Episode(s)" : 288358400.12,               #275 MB
    "720p x264 Episode(s)" : 734003200.31,               #700 MB
    "1080p x264 Episode(s)" : 1879048192,                #1.75 GB
    "2K (1440p) x264 Episode(s)": 3489660928,            #3.25 GB
    "UHD (4K) x264 Episode(s)" : 7516192768,             #7 GB
    "480p x265 Episode(s)" : 209715200.09,               #200 MB
    "720p x265 Episode(s)" : 576716800.25,               #550 MB
    "1080p x265 Episode(s)" : 1503238553.6,              #1.4 GB
    "2K (1440p) x265 Episode(s)" : 2952790016,           #2.75 GB
    "UHD (4K) x265 Episode(s)" : 5905580032              #5.5 GB
}

print("With a %s storage device you can store the following information:" % user_input)
print("%s character(s) in a text file" % math.floor(user_to_bytes / data_storage["character in text file"]))
print("%s MP3 Song(s)" % math.floor(user_to_bytes / data_storage["MP3 Song File"]))
print("%s DVD(s)" % math.floor(user_to_bytes / data_storage["DVD"]))
print("%s Blu-yay(s)" % math.floor(user_to_bytes / data_storage["Blu-ray Disc"]))
print("%s Ultra HD Blu-ray(s)" % math.floor(user_to_bytes / data_storage["Ultra HD Blu-ray"]))
print("%s Ultra HD Blu-ray Backup(s)" % math.floor(user_to_bytes / data_storage["Ultra HD Blu-ray Backup"]))
print("%s Video Game(s)" % math.floor(user_to_bytes / data_storage["Video Game"]))
print("%s 480p x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["480p x264 Movie(s)"]))
print("%s 720p x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["720p x264 Movie(s)"]))
print("%s 1080p x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["1080p x264 Movie(s)"]))
print("%s 2K (1440p) x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["2K (1440p) x264 Movie(s)"]))
print("%s UHD (4K) x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["UHD (4K) x264 Movie(s)"]))
print("%s 8K x264 (H.264) Movie(s)" % math.floor(user_to_bytes / data_storage["8K x264 Movie(s)"]))
print("%s 480p x265 (H.265) Movie(s)" % math.floor(user_to_bytes / data_storage["480p x265 Movie(s)"]))
print("%s 720p x265 (H.265) Movie(s)" % math.floor(user_to_bytes / data_storage["720p x265 Movie(s)"]))
print("%s 1080p x265 (H.265) Movie(s)" % math.floor(user_to_bytes / data_storage["1080p x265 Movie(s)"]))
print("%s 2K (1440p) (H.265) x265 Movie(s)" % math.floor(user_to_bytes / data_storage["2K (1440p) x265 Movie(s)"]))
print("%s UHD (4K) (H.265) x265 Movie(s)" % math.floor(user_to_bytes / data_storage["UHD (4K) x265 Movie(s)"]))
print("%s 8K x265 (H.265) Movie(s)" % math.floor(user_to_bytes / data_storage["8K x265 Movie(s)"]))
print("%s 480p x264 (H.264) Episode(s)" % math.floor(user_to_bytes / data_storage["480p x264 Episode(s)"]))
print("%s 720p x264 (H.264) Episode(s)" % math.floor(user_to_bytes / data_storage["720p x264 Episode(s)"]))
print("%s 1080p x264 (H.264) Episode(s)" % math.floor(user_to_bytes / data_storage["1080p x264 Episode(s)"]))
print("%s 2K (1440p) x264 (H.264) Episode(s)" % math.floor(user_to_bytes / data_storage["2K (1440p) x264 Episode(s)"]))
print("%s UHD (4K) x264 (H.264) Episode(s)" % math.floor(user_to_bytes / data_storage["UHD (4K) x264 Episode(s)"]))
print("%s 480p x265 (H.265) Episode(s)" % math.floor(user_to_bytes / data_storage["480p x265 Episode(s)"]))
print("%s 720p x265 (H.265) Episode(s)" % math.floor(user_to_bytes / data_storage["720p x265 Episode(s)"]))
print("%s 1080p x265 (H.265) Episode(s)" % math.floor(user_to_bytes / data_storage["1080p x265 Episode(s)"]))
print("%s 2K (1440p) x265 (H.265) Episode(s)" % math.floor(user_to_bytes / data_storage["2K (1440p) x265 Episode(s)"]))
print("%s UHD (4K) x265 (H.265) Episode(s)" % math.floor(user_to_bytes / data_storage["UHD (4K) x265 Episode(s)"]))
