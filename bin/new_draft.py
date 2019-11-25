#!/usr/bin/env python3

from sys import argv
from random import randint

if len(argv) > 1:
    argv_size = len(argv)
    title = '-'.join(argv[1:argv_size])
else:
    random = randint(1_000, 9_999)
    title = "new-draft-" + str(random)

filename = title + ".md"

print(filename)

front_matter = \
f'''---
layout: post
title:  "New Post Title"
date:   [insert post date here]
tags:
---
'''

with open("_drafts/" + filename, 'w') as f:
    f.write(front_matter)
