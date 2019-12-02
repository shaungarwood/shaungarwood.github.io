#!/usr/bin/env python3

import datetime
from random import randint
from sys import argv

import pytz

if len(argv) > 1:
    argv_size = len(argv)
    title = '-'.join(argv[1:argv_size])
else:
    random = randint(1_000, 9_999)
    title = "new-draft-" + str(random)

mountain = pytz.timezone('America/Denver')
now = datetime.datetime.now(mountain)
filename = now.strftime("%Y-%m-%d-") + title + ".md"

print(filename)

front_matter = \
f'''---
layout: post
title:  "New Post Title"
date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}
tags:
---
'''

with open("_drafts/" + filename, 'w') as f:
    f.write(front_matter)
