---
layout: default
---

My name is Shaun.

I'm a developer/engineer with a particular focus in
```
  linux,
  python,
  ruby,
  networking,
  security,
  and docker.
```
Though I dabble in quite a few things.

This site is to showcase my findings, notes, hacks, ideas, rants, raves, musings, and thoughts.

## Posts:
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
