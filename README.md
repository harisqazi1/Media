# Media

A collection of scripts and packages for use with home media. There are two ways to use these: running the script yourself or using the package (Python packages are made using [PyInstaller](https://pyinstaller.org/)). With the second option (PyInstaller package), all the needed code that works in the background comes with it, so all you have to do is run the script. 

Compilation with PyInstaller on my side is done with the following command:
`pyinstaller program.py`.

## Directory Structure (example)
```
Media (Root Directory - you are here)/
└── Folder (Each script will have it's own folder)/
    ├── dist (packaged output)/
    │   └── script folder name/
    │       ├── binary (executable)
    │       └── folder with dependencies
    ├── README.md (Explanation of the script)
    └── name.extention (source code)
```

## Projects
- Subtitle Shift - Edit subtitle files to show text sooner or later (works for negative)
- Statistics - Get statistics on your media vault
## Usage/Examples

If you want to download the script only, I would recommend using `curl`, `wget`, or the "Save page as..." built into the browser. However, if you want to download the package, I would use the following tools to do so (I am not affiliated to these services, nor have I reviewed them):

- https://githubdownloader.com/
- https://download-directory.github.io/
- http://kinolien.github.io/gitzip
- https://minhaskamal.github.io/DownGit

Go to the dist folder in each project and use the aforementioned tools on it. **You might have to run `chmod +x binary_name` to make it executable.**
