#!/usr/bin/env python3
import fileinput
from sys import argv
import datetime
import pytz
import os

def get_date():
    mountain = pytz.timezone('America/Denver')
    now = datetime.datetime.now(mountain)
    return now

if len(argv) < 1:
    print("please input the draft filename")
    exit()

filename = argv[1]

now = get_date()
draft_date = "date:   [insert post date here]"
publish_date = f'date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}'

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(draft_date, publish_date), end='')

# get filename from draft filename
# add date
# move to _publish dir
os.rename(filename, "path/to/new/destination/for/file.foo")
