# Storage Estimat-inator

Have you ever wondered how much media X amount of storage would be able to hold? This script is my best attempt to get those answers. 

It currently supports the following inputs (storage sizes): `KB`, `MB`, `GB`, `TB`, `PB`, and `EB`. 

It currently outputs the following information:

- character in text file 
- MP3 Song File 
- DVD 
- DVD Backup 
- Blu-ray Disc 
- Ultra HD Blu-ray 
- Ultra HD Blu-ray Backup 
- Video Game 
- 480p x264 Movie(s) 
- 720p x264 Movie(s) 
- 1080p x264 Movie(s) 
- 2K (1440p) x264 Movie(s) 
- UHD (4K) x264 Movie(s) 
- 8K x264 Movie(s) 
- 480p x265 Movie(s) 
- 720p x265 Movie(s) 
- 1080p x265 Movie(s) 
- 2K (1440p) x265 Movie(s) 
- UHD (4K) x265 Movie(s) 
- 8K x265 Movie(s) 
- 480p x264 Episode(s) 
- 720p x264 Episode(s) 
- 1080p x264 Episode(s) 
- 2K (1440p) x264 Episode(s)
- UHD (4K) x264 Episode(s) 
- 480p x265 Episode(s) 
- 720p x265 Episode(s) 
- 1080p x265 Episode(s) 
- 2K (1440p) x265 Episode(s) 
- UHD (4K) x265 Episode(s) 

**NOTE: I have tried my best to validate the values used for the aformentioned media. If you have corrections for these, either file an issue or feel free to pull and push it here.**
## Logic

There are two forms of capacity on a storage device: what the manufacturer claims (Claimed Capacity) and what the drive is actually capable of storing (Real Capacity). For example, on WD Data Sheet for the "My Passport" lineup, you can see that for a 1TB storage: `1TB = one trillion bytes` ([source](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/wd/product/external-storage/my_passport/my-passport-new/product-overview-wd-my-passport.pdf) | [archived source](https://web.archive.org/web/20240403171247/https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/wd/product/external-storage/my_passport/my-passport-new/product-overview-wd-my-passport.pdf)). This is completely factual...but one main thing to note is that their calculation of capacity is done in base(10) not base(2). Why does that matter?

When you buy a 1 TB hard drive, you might realize that you might only have 909.4947 GB of storage instead of the 1000 GB (1 TB) you had expected. This is due to this discrepency between binary (a.k.a base(2) or real capacity) and decimal (a.k.a base(10) or claimed capacity). By knowing and understanding the real capacity, we can then assume how much we can fit into our storage device.

### Math

I have found the math for this from https://www.minitool.com/lib/hard-drive-capacity.html. It boils down to the following: Divide the amount of total bytes you have by `1024` until you reach the specified bytes-level. My explanation is not the best, so see the following example.

If we have 10 GB USB, that is 10000000000 bytes. To figure out the real capacity, we go down the following list:

- Step 1 (you are here): Bytes / 1024 = KB
- Step 2: KB / 1024 = MB
- Step 3: MB / 1024 = GB

In Math terms:

```
10000000000 bytes #10 Gigayte in bytes
/1024             #Adding KB Layer
= 9765625

9765625 / 1024    # Adding MB layer
= 9536.743164063

9536.743164063 / 1024 #Adding GB layer
= 9.313225746
```

**You have a total real capacity of `9.313225746 GB` out of a `10 GB USB`**

The following sites do a good job of calculating this as well: https://endmemo.com/data/diskcapacity.php and https://platinumdatarecovery.com/hard-drive-capacity-calculator. 

This math takes care of the real storage, but what I have also done, is grabbed the binary bytes values for the media formats, as well. This allows for a 1-to-1 correlation between media file sizes and the actual capacity on your device.
## Usage/Examples

To run the code:
`python3  storage_estimat-inator.py <Value (10)> <Bytes (MB)>`

Example output for 10 TB:

```
----------------------------------------------------------------------
Real capacity for 10 TB is 9.09494702 TB
----------------------------------------------------------------------
With 10 TB storage device you can store the following information:
9094947020000 character(s) in a text file
867361 MP3 Song(s)
2117 DVD(s)
338 Blu-yay(s)
154 Ultra HD Blu-ray(s)
133 Ultra HD Blu-ray Backup(s)
105 Video Game(s)
15770 480p x264 (H.264) Movie(s)
6091 720p x264 (H.264) Movie(s)
2420 1080p x264 (H.264) Movie(s)
1411 2K (1440p) x264 (H.264) Movie(s)
605 UHD (4K) x264 (H.264) Movie(s)
141 8K x264 (H.264) Movie(s)
21684 480p x265 (H.265) Movie(s)
8121 720p x265 (H.265) Movie(s)
3080 1080p x265 (H.265) Movie(s)
1694 2K (1440p) (H.265) x265 Movie(s)
806 UHD (4K) (H.265) x265 Movie(s)
178 8K x265 (H.265) Movie(s)
31540 480p x264 (H.264) Episode(s)
12390 720p x264 (H.264) Episode(s)
4840 1080p x264 (H.264) Episode(s)
2606 2K (1440p) x264 (H.264) Episode(s)
1210 UHD (4K) x264 (H.264) Episode(s)
43368 480p x265 (H.265) Episode(s)
15770 720p x265 (H.265) Episode(s)
6050 1080p x265 (H.265) Episode(s)
3080 2K (1440p) x265 (H.265) Episode(s)
1540 UHD (4K) x265 (H.265) Episode(s)
```


## Sources

These are the sources I used for this project:

-  https://physics.nist.gov/cuu/Units/binary.html
-  https://www.computerhope.com/issues/chspace.htm
-  https://www.gbmb.org/
-  https://en.wikipedia.org/wiki/Comparison_of_high-definition_optical_disc_formats
-  https://gamerant.com/pc-games-file-size-hd-space-biggest-huge/
-  https://blog.online-convert.com/average-file-sizes/
-  https://en.wikipedia.org/wiki/Pirated_movie_release_types
-  https://www.kingston.com/en/memory-cards/storage-chart
-  https://www.mindgems.com/info/file-size/
-  https://storytellertech.com/how-many-videos-per-gb/
-  https://stackoverflow.com/questions/3387655/safest-way-to-convert-float-to-integer-in-python
-  https://massive.io/file-transfer/gb-vs-gib-whats-the-difference/
-  https://www.minitool.com/lib/hard-drive-capacity.html
-  https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb

I also did get a bit of help from ChatGPT in order to gain insights into average file sizes for different encodings. It output the following:

```
Sure, here are rough estimates for average file sizes for movies and TV shows encoded in x264 and x265 across various resolutions, including 480p, 720p, 1080p, 2K (1440p), UHD (4K), and 8K:

    Movies:

        x264 (H.264):
            480p: Approximately 300 MB to 800 MB.
            720p: Approximately 800 MB to 2 GB.
            1080p: Approximately 2 GB to 5 GB.
            2K (1440p): Approximately 4 GB to 8 GB.
            UHD (4K): Approximately 8 GB to 20 GB.
            8K: Varies widely, but can range from 20 GB to 100 GB or more.

        x265 (H.265):
            480p: Approximately 200 MB to 600 MB.
            720p: Approximately 600 MB to 1.5 GB.
            1080p: Approximately 1.5 GB to 4 GB.
            2K (1440p): Approximately 3 GB to 7 GB.
            UHD (4K): Approximately 6 GB to 15 GB.
            8K: Varies widely, but can range from 15 GB to 80 GB or more.

    TV Shows:

        x264 (H.264):
            480p: Approximately 150 MB to 400 MB per episode.
            720p: Approximately 400 MB to 1 GB per episode.
            1080p: Approximately 1 GB to 2.5 GB per episode.
            2K (1440p): Approximately 2 GB to 4.5 GB per episode.
            UHD (4K): Approximately 4 GB to 10 GB per episode.
            8K: Not commonly available for TV shows due to high file sizes and limited content availability.

        x265 (H.265):
            480p: Approximately 100 MB to 300 MB per episode.
            720p: Approximately 300 MB to 800 MB per episode.
            1080p: Approximately 800 MB to 2 GB per episode.
            2K (1440p): Approximately 1.5 GB to 4 GB per episode.
            UHD (4K): Approximately 3 GB to 8 GB per episode.
            8K: Not commonly available for TV shows due to high file sizes and limited content availability.

Sources:

    These estimates are based on industry standards, encoding practices, and discussions within the digital video community.
    They also draw from personal experience and observations of file sizes for movies and TV shows encoded in x264 and x265 formats across various resolutions.
    No specific sources are available as these estimates are derived from general knowledge within the field.

```

It did not provide me any concrete sources I can link here.
