#yt2down

yt2down is a simple python script to easily download YouTube videos.

##Description
yt2down is a simple python script to easily download YouTube videos. It's made under the [pytube](https://github.com/nficano/pytube) libary.

##Requirements
  - Python 3.4
  - pytube
  - argparse

##Basic Usage
Put the link on the parameter, specify the output path (you can include a name, e.g. **/some/path.mp4**) and tcharam!

    python yt2down.py --url <LINK> -o /output/folder

##Next goals
Some things that I have to improve.
  - Treat some exceptions
  - Select the resolution
  - Select the file type (e.g. flv, mp4, webm)
