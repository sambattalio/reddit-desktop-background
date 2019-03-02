#!/usr/bin/env python
import applescript
import re
import requests
import os
import pprint
import schedule
import sys
import time

# Globals

BASE = 'https://www.reddit.com'
SUB = '/r/wallpapers'
URL = BASE + SUB + '/.json'

reddit_header = {'user-agent': 'reddit-{}'.format(os.environ.get('USER', 'sambatt99'))}

HOURS = 24

# Functions

def usage(code=0):
    print('''Usage: {} [options] subreddit_name
    Pick a subreddit that exclusively has images (earthporn,wallpapers,...)

    -n        Number of hours between updates (default=24)
    '''.format(os.path.basename(sys.argv[0])))
    sys.exit(code)

# run applescript command to switch background to image @ filepath
def change_background(img):
    applescript.run('tell application "System Events" to tell every desktop to set picture to "{}"'.format(os.path.realpath(img)))

# download image
def wget(url):
    p = os.path.basename(url) # name of image

    req = requests.get(url, headers=reddit_header) # request from site
    with open(p, 'wb') as fs: # write image
        fs.write(req.content)

    return p # return image file

# get url of top post image
def grab_top_post(url=URL):
    r = requests.get(url,headers=reddit_header)
    posts = r.json()['data']['children']
    return posts[0]['data']['url']

# remove background after changing
def cleanup():
    for item in os.listdir(os.getcwd()):
        if item.endswith('.jpg'):
            os.remove(item)

# combine change and cleanup operation
def do_it_all(url=URL):
    change_background(wget(grab_top_post(url)))
    cleanup()

    
# Handle arguments
args = sys.argv[1:]
while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    # check arguments
    if arg == '-h':
        usage(0)
    elif arg == '-n':
        HOURS = int(args.pop(0))

if len(args) == 1:
    SUB = '/r/' + args.pop(0)
else:
    usage(1)

URL = BASE + SUB + '/.json'

# main execution
if __name__ == "__main__":
    do_it_all(URL)
    sys.exit(0)
