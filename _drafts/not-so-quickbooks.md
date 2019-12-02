---
layout: post
title:  "Not So QuickBooks"
date:   2019-11-21 06:20:49 -0700
tags:  python oauth api fail
---

Not every story on here will be a triumphant victory. There are plenty of things to be learned from falling flat on our faces. Or spending days spinning our wheels THEN falling flat on our faces.

<center>
  <iframe src="https://giphy.com/embed/5tiIlnk9rPNUYWXDwl" width="200" height="113" frameBorder="0" class="giphy-embed" allowFullScreen>
  </iframe>
</center>

So a friend was doing some work with QuickBooks online and she said that it was slow-doing, repetitive, and going to take forever. "I can automate that!" said a foolish voice at the table. "Great!", said the relieved friend. All she needed was any transaction on the books before 9/1/2019 to be deleted. How hard could it be?

## Hurtle #1

I had to register as developer.

Not a big hurtle, but more than I had planned on for writing a quick script. I couldn't find anything on the internet for one-shot client scripts to interact with QuickBooks online, but  a ton about developing apps to interact with QuickBooks online. I guess I'm an app developer then.

Intuit (the company who makes QuickBooks) actually has a pretty great development setup. Once I signed up, they redirected me to a nice little dashboard with the keys I needed AND they create a sandbox company to play around with, complete with 50+ small business transactions. Pretty sweet.

![My helpful screenshot](/assets/2019-12-01-quickbooks-sandbox.png)

## Hurtle #2

I had to write a full app, just to get logged in.

So I was getting [this python package](https://github.com/sidecars/python-quickbooks) running with my new shiny oauth keys and I keep seeing this "redirect URI". Come to find out, it is where Intuit's oauth login page redirects your user WITH the necessary refresh token. Confusing? Yeah.

All this work is because the assumption is you're writing an app or developing some online tool to be used by strangers. You send the user to Intuit's login page, they authorize your app, Intuit sends the user AND the tokens back to your app.

My flow, just to get all the ids and tokens to login:
```
                                                                   
  +----------+  generates a  +------------+                        
  |          |  link to      |            |                        
  |  run.py  --------------->| intuit's   |                        
  |          |               | auth page  |                        
  +----------+               |            |                        
       ^                     +------------+                        
       |                            |                              
       | which feeds                | sends tokens and users to    
       | back into                  | "redirect uri" (my localhost)
       |                            |                              
+-------------+               +----------+                         
|             |               |          |                         
| config.toml |<------------- |  api.py  |                         
|             |   writes      |          |                         
+-------------+   tokens to   +----------+                         
```

```run.py``` is the main script and ```api.py``` was my little flask API to retrieve the tokens that the Intuit auth page sent. Write them to my config.toml (I LOVE toml files for configs) and have ```run.py``` use them. Phew! But I have to be getting close...

## Hurtle #3

I am not an accountant.

<center>
  <iframe src="https://giphy.com/embed/FaLhiZQHrBIYw" width="300" height="264" frameBorder="0" class="giphy-embed" allowFullScreen>
  </iframe>
</center>

I'm in! Aaaaand I have no idea what I'm looking at. The API doesn't flow the same way as the dashboard. It's probably minor differences in how things are worded, but it's enough to throw me off.

A few emails back and forth with my friend and I learn that the "view register" part of the dashboard does not have an API equivalent. Opening a register on the dashboard would show you all the bills, payments, credit card transactions, etc. for an account. In the API, you can pull all bills, all payments, all credit cards, etc - but you're doing so for only that transaction type. I code around it.

What a pain. Well, it's almost over...

## Hurtle #4

Out of the sandbox, into production.

It's been a few days now, but I'm so close I can taste it. My code works on the sandbox company, I deleted a few transactions, now it's time to turn this loose on the actual target.

In order for Intuit to let me touch a production company, I have to:
- Finish filling out my profile
- Link to my app's privacy policy
- Link to my app's EULA
- Supply my app's redirect URIs

UGH! Finish my profile: no problem. A privacy policy and a EULA? This is just ridiculous. So I find some online privacy policy and EULA generators. Could I have just linked to a text file for the lyrics to a Sir Mix-a-Lot song? Probably, but the generators were fast enough and they hosted the end result.

More redirect URIs? I got this, I'll just use my localhost address and...
```
Error: All Production URI requests must use HTTPS.
```

Noooooooo!!!!

Okay, maybe I can just use a self signed cert...

```
Error: Please enter a unique valid redirect URI
```

It doesn't like localhost. It needs an FQDN (something with a ".com").

<center>
  <iframe src="https://giphy.com/embed/22CEvbj04nLLq" width="480" height="411" frameBorder="0" class="giphy-embed" allowFullScreen>
  </iframe>
</center>

## Game Over

At this point I took a good hard look at what I had become and the lengths I have gone to "save time and energy", and I admitted defeat. In hindsight, I should have called it quits at hurtle #2. But I learned a lot about QuickBooks, some things about OAuth2, and a little about accounting. So it wasn't a total loss.

Called my friend and told her to contact someone at Intuit. They could do it for her in minutes.
