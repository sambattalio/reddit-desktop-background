# reddit-desktop-background
Changes Desktop background to top reddit post in set subreddit

# Requirements
Made for Mojave 10.14 in python 2.7 (TODO: add linux/windows support)

* applescript
* pyobjc

# How to?

### Mac

`$ git clone https://github.com/sambattalio/reddit-desktop-background.git`

`$ crontab -e`

Then, add the following line to crontab window:

`@hourly ~/Path/to/cloned/repo/runBackground.sh`

*TODO: add init script to do this part for you*
