#!/usr/bin/env python3

from sys import argv
import datetime
import pytz

if len(argv) > 1:
    argv_size = len(argv)
    title = '-'.join(argv[1:argv_size])
else:
    title = "new-post"

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
