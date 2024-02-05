# Statistics

This project aims to provide insight into the media in your library. With the rise of DRM-free, Copyright-free, and Fair-Use content, this allows you to get information on your collection. There is currently no plan to add audio files into this project. 

## Usage/Examples

Files should be stored in the following format:
```
Media/
├── statistics.py
├── Folder 1/
│   └── file1.mkv
├── Folder 2/
│   └── file2.mkv
└── Folder X/
    └── fileX.mkv
```

This is coded to look for `.mkv` files only at the moment. In order to add more extensions see this [stackoverflow answer](https://stackoverflow.com/a/4568638)].

```python
python3 statistics.py
```

### Output Example (X represents a number)

```
Amount of Media: XXX
Sub-30:          XXX
Super-30:        XXX
Movies:          XX
DVDs:            XXX
Blu-rays:        XXX
Average sub-30 show duration:   X:XX:XX.XXXXXX
Average super-30 show duration: X:XX:XX.XXXXXX
Average movie duration:         X:XX:XX.XXXXXX
Average sub-30 show size:       XXX.XX MB
Average super-30 show size:     XXX.XX MB
Average DVD size:               XX.XX GB
Average Blu-ray size:           XX.XX GB
Total media duration:           X days, X:XX:XX.XXXXXX
Total media(Show/Movies) size:  XXX.XX GB
```
