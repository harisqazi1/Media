# Subtitle Shift

I wrote a Python script to shift the timestamps in a subtitle document. I had tried the following projects, but they did not end up working for my use case (going negative):

- https://github.com/spion/subsync
- https://github.com/smacke/ffsubsync
- https://github.com/netharuM/srt-subtitle-time-fix/tree/master
- https://marcustansoon.github.io/Subtitle-Time-Shifting-Tool/

## Features

- Move Subtitles Earlier (_)
- Delaying Subtitles (+)


## Usage/Examples
Format:
```
<python3 location> subtitle_shift.py <input_file> -t <(+/_)time shift> -o <output_file>
```
**NOTE: _ is used to speed up; + is used to delay subtitles**

Thus, 
```python
python3 subtitle_shift.py input.srt -t _00:01:32,001 -o output.txt
```
**This currently is tested on single input files. Wildcards might be possible with a bash script.**

### Example:

Input (excerpt):

```
1
00:00:00,000 --> 00:00:02,363
Hi, This is a test

2
00:00:02,363 --> 00:00:03,470
of the Subtitle Shift program

3
00:01:16,888 --> 00:01:23,054
written to make shifting

4
00:05:20,362 --> 00:05:21,627
Subtitles Easy

5
00:06:58,168 --> 00:06:59,000
It is currently located at:

6
00:07:22,765 --> 00:07:23,808
https://github.com/harisqazi1/Subtitle_Shift
```

Command:
```python
python3 subtitle_shift.py testing.srt -t _00:01:32,001 -o test.txt
```

Output (excerpt):
```



4
00:03:47.361 --> 00:03:48.626
Subtitles Easy

5
00:05:25.167 --> 00:05:25.999
It is currently located at:

6
00:05:49.764 --> 00:05:50.807
https://github.com/harisqazi1/Subtitle_Shift
```
## Problems

### Problem 1
The format that mkvmerge reads timestamps seems to be **only** in `00:00:00,000` format. At times my code would output strings like `00:07`, which mkvmerge would not accept, and thus reject all subtitles after. In order to combat this, I have added a line on line 24: 
```
time_one = datetime.strptime('00:00:00,000011', '%H:%M:%S,%f')
```
This allows me to fix this error for the most part. However, if you see the error in your files, adding a millisecond (ex. `_00:01:32,001`) in **your command** should resolve this issue. This could **potentially** (untested at the moment) also be mitigated by not stripping the end 3 characters on line 42.
## Installation

Clone and run the code. You need to have `git` installed for this.

```bash
  git clone https://github.com/harisqazi1/Subtitle_Shift.git
  cd Subtitle_Shift.git
  python3 new_script.py -h 
```
You can also download the raw file using curl or wget. Link to raw file:
https://raw.githubusercontent.com/harisqazi1/Subtitle_Shift/main/subtitle_shift.py
## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)


## Sources
- https://stackoverflow.com/questions/43479551/addition-of-two-datetime-datetime-strptime-time-objects-in-python
- https://stackabuse.com/the-python-tempfile-module/
- https://docs.python.org/3/library/re.html
- https://docs.python.org/3/library/time.html#module-time
- Some more I can't recall at the moment.
