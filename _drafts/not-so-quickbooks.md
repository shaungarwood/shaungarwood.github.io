---
layout: post
title:  "Not So Quickbooks"
date:   [insert post date here]
tags:  python oauth api fail
---

Not every story on here will be a triumpant victory. There are plenty of things to be learned from falling flat on our faces. Or spending days spinning our wheels THEN falling flat on our faces.

So a friend was doing some work with Quickbooks online and she said that it was slow-doing, repetative, and going to take forever. "I can automate that!" said a foolish voice at the table. "Great!", said the relieved friend. All she needed was any transaction on the books before 9/1/2019 to be deleted. How hard could it be?

## Hurtle #1

I had to register as developer. Not a big hurtle, but more than I had planned on for writing a quick script.  Intuit (the company who makes Quickbooks) actually has a pretty great development setup. Once I signed up, they redirected me to a nice little dashboard with the keys I needed AND they create a sandbox company to play around with, complete with 50+ small business transactions. Pretty sweet.

![My helpful screenshot](/assets/2019-12-01-quickbooks-sandbox.png)

## Hurtle #2

So I was getting [this python package](https://github.com/sidecars/python-quickbooks) running with my new shiny oauth keys and I keep seeing this "redirect URI". Come to find out, it is where Intuit's oauth login page redirects your user WITH the necessary refresh token. Confusing? Yeah.

All this work is because the assumption is you're writing an app or developing some online tool to be used by strangers. You send the user to Intuit's login page, they authorize your app, Intuit sends the user AND the tokens back to your tool. I searched Google high and low, but there weren't any simple one-shot client solutions. I guess I'm an app developer then.

What this means for me, is I had to setup a little flask API to 

1. i had to register as an Intuit app developer
2. they generate a sandbox company for you fuck around with, which is honestly pretty cool.
3. i have to have a seperate web server running because they will only issue the keys BACK to "redirect uri". so you have code that will use your oauth keys to generate a link, that you have to click, web browser opens and you grant the code access to your account, that will send new keys back to the web server you're running.
4. the api isn't great, or at least not intuitive if you're not an accountant
5. NOW you move on to your production company
6. you have to link your fake app to a publicly available privacy policy and EULA. luckily there are online generators.
7. however, the redirect URI for prod has to be SSL and cannot be "localhost".
