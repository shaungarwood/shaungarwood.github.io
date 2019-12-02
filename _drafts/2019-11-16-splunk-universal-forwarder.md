---
layout: post
title:  "Universal Splunk Forwarder"
date:   2019-06-03 20:24:21 -0600
categories: docker
---
{% highlight bash %}
docker run -d -p 9997:9997 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=<password>" --name uf splunk/universalforwarder:latest
{% endhighlight %}
