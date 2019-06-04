---
layout: default
---

# Yo

My name is Shaun and I'm a developer/engineer with a particular focus in ruby, linux, networking, security, and docker. Though I dabble in quite a few things.

This site is to showcase some of the things I figure out. It's for that other lone person googling a way-too-specific error message to shout "YES!" when they discover I had the same struggles, but prevailed. Or maybe it'll be the platform (backed by github's CDN) for detailing a juicy hack I pull off.

There will definitely be some mistakes and not every post will be perfect. At the very least, it'll sharpen my writing skills and be a cool collection of my adventures.

## Posts:
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
