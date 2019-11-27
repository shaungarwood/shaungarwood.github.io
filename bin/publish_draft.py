#!/usr/bin/env python3
import fileinput
from sys import argv
import datetime
import pytz
import os
import re

def get_date():
    mountain = pytz.timezone('America/Denver')
    now = datetime.datetime.now(mountain)
    return now

if len(argv) < 1:
    print("please input the draft filename")
    exit()

filepath = argv[1]
filename = os.path.basename(filepath)
filename = re.sub(r'\.md$', '', filename)
filename = re.sub(r'^\d{4}\-\d{2}\-\d{2}\-', '', filename)

now = get_date()
draft_date = "date:   [insert post date here]"
publish_date = f'date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}'
date_regex = r'date:\s+\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2} \-\d{4}'

with fileinput.FileInput(filepath, inplace=True) as file:
    for line in file:
        existing = re.search(date_regex, line)
        if existing:
            draft_date = existing[0]
        print(line.replace(draft_date, publish_date), end='')

new_path = "_posts/" + now.strftime("%Y-%m-%d-") + filename + ".md"
os.rename(filepath, new_path)
print(new_path)
