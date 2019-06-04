---
layout: post
title:  "My Set-Up For Blogging"
date:   2019-06-03 20:24:21 -0600
categories: docker
---
Nothing better to kick this blog off than explaining how I set it up!

## Choices
I went with github-pages because I wanted something fast & easy, backed by a CDN, and obviously a platform where I still own the content. A big plus that I can tweak and tinker with everything. Could I write my own site from scratch and host it on the cloud? Yes, and I still might. But this works for now and will be easy to port all the content if I do.

## Initial Set-up
1. ```jekyll new blog```
2. Edit Gemfile, comment out jekyll, uncomment github-pages.
3. Update _config.yml with details, comment out theme cause we're importing all the files manually.
4. 
```
git clone https://github.com/poole/hyde.git ../
cp -r ../hyde/_layouts/ ./
cp ../hyde/*.html ./
cp ../hyde/atom.xml ./
cp -r ../hyde/public/ ./
cp -r ../hyde/_includes ./
```

## Currently
As alway, I'm using Vim and will until the day I die. I'll probably use it to finalize my will.

In order to try things out locally, I needed to run a local web server for github pages. Dockerhub user ```starefossen``` wrote a nice little Dockerfile for exactly this: [https://hub.docker.com/r/starefossen/github-pages/](https://hub.docker.com/r/starefossen/github-pages/)

So to see live updates of my changes I just run:
{% highlight bash %}
docker run -t --rm --name ghp -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
{% endhighlight %}

## Future Improvements
I'll definitely write a quick ruby script to generate a skeleton markdown post with the current date/time and proper front matter.
