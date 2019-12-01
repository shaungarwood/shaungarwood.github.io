---
layout: post
title:  "New Post Title"
date:   [insert post date here]
tags:  python oauth api
---

1. i had to register as an Intuit app developer
2. they generate a sandbox company for you fuck around with, which is honestly pretty cool.
3. i have to have a seperate web server running because they will only issue the keys BACK to "redirect uri". so you have code that will use your oauth keys to generate a link, that you have to click, web browser opens and you grant the code access to your account, that will send new keys back to the web server you're running.
4. the api isn't great, or at least not intuitive if you're not an accountant
5. NOW you move on to your production company
6. you have to link your fake app to a publicly available privacy policy and EULA. luckily there are online generators.
7. however, the redirect URI for prod has to be SSL and cannot be "localhost".
