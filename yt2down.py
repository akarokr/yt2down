# coding: utf-8

from pytube import YouTube
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url',
                    dest='url',
                    help='the video URL',
                    required=True)

parser.add_argument('-o', '--output',
                    dest='out',
                    help='file output, e.g. /folder/')

args = parser.parse_args()
urls = args.url
output = args.out

yt = YouTube()
yt.url = urls
video = yt.get()
video.download(output)
