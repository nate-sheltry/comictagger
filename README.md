[![CI](https://github.com/nate-sheltry/comictagger/actions/workflows/build.yaml/badge.svg)](https://github.com/nate-sheltry/comictagger/actions/workflows/build.yaml)
[![GitHub release (latest by date)](https://img.shields.io/github/downloads/nate-sheltry/comictagger/latest/total)](https://github.com/nate-sheltry/comictagger/releases/latest)
[![PyPI - License](https://img.shields.io/pypi/l/comictagger)](https://opensource.org/licenses/Apache-2.0)
# ComicTagger

ComicTagger is a **multi-platform** app for **writing metadata to digital comics**, written in Python and PyQt.

![ComicTagger logo](https://raw.githubusercontent.com/comictagger/comictagger/develop/comictaggerlib/graphics/app.png)

## Features

* Runs on macOS, Microsoft Windows, and Linux systems
* Get comic information from [Comic Vine](https://comicvine.gamespot.com/)
* **Automatic issue matching** using advanced image processing techniques
* **Batch processing** in the GUI for tagging hundreds or more comics at a time
* Support for **ComicRack** and **ComicBookLover** tagging formats
* Native full support for **CBZ** digital comics
* Native read only support for **CBR** digital comics: full support enabled installing additional [rar tools](https://www.rarlab.com/download.htm)
* Command line interface (CLI) enabling **custom scripting** and **batch operations on large collections**
* Includes support for advanced image formats:
    - *JPEG XL* **.jxl**
    - *AVIF* **.avif**
    - *HEIC & HEIF* **.heic**, **.heif**

For details, screen-shots, and more, visit [the Wiki](https://github.com/comictagger/comictagger/wiki)

For more information on why I forked and made some modification [click here](Q&A.md)

## Installation

### Binaries

Windows and macOS binaries are provided in the [Releases Page](https://github.com/comictagger/comictagger/releases).

Just unzip the archive in any folder and run, no additional installation steps are required.

### PIP installation

A pip package is provided, you can install it with:

```
 $ pip3 install comictagger[GUI]
```

There are two optional dependencies GUI and CBR. You can install the optional dependencies by specifying one or more of `GUI`,`CBR` or `all` in braces e.g. `comictagger[CBR,GUI]`

### Chocolatey installation (Windows only)

A [Chocolatey package](https://community.chocolatey.org/packages/comictagger), maintained by @Xav83, is provided, you can install it with:
```powershell
choco install comictagger
```
### From source

 1. Ensure you have python 3.12 installed
 2. Clone this repository `git clone https://github.com/nate-sheltry/comictagger.git`
 3. `pip3 install -r requirements_dev.txt`
 7. `pip3 install .` or `pip3 install .[GUI]`
