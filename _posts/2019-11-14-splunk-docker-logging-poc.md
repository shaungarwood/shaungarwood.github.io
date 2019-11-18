---
layout: post
title:  "Darn You Splunk! Darn You to HEC!"
date:   2019-11-16 19:54:23 -0700
tags: docker splunk logs
---

So, the goal was to get Splunk running to monitor/alert/graph several docker containers and the physical hosts they're running on. I ended up hitting a few roadblocks getting there, while finding suprisingly little help in my Google travels. So I'm writing out a simple top-to-bottom proof-of-concept to get docker logs flowing into a Splunk docker instance.

{% highlight bash %}
# quick splunk server, with HTTP Event Collector running and pre-determined token:
docker run -d \
  --name "splunk" \
  -p '8000:8000' \
  -p '8088:8088' \
  -e "SPLUNK_START_ARGS=--accept-license" \
  -e "SPLUNK_PASSWORD=password" \
  -e "SPLUNK_HEC_TOKEN=secret-token" \
splunk/splunk:latest

# manually insert an event
curl -k  https://localhost:8088/services/collector/event -H "Authorization: Splunk secret-token" -d '{"event": "hello world"}'

# using docker's "splunk" log driver
docker run -d \
  --name "nginx" \
  --publish "80:80" \
  --log-driver=splunk \
  --log-opt splunk-token=secet-token \
  --log-opt splunk-url=https://127.0.0.1:8088 \
  --log-opt splunk-insecureskipverify=true \
nginx

# inspect nginx to see logging driver (you'll need jq if you want pretty print)
docker inspect --format='{{json .HostConfig.LogConfig}}' nginx | jq .

# use above nginx, generating a log event
curl http://localhost:80
{% endhighlight %}

Log in to Splunk to view the logs (yes, there's a space in that URL):
```
http://127.0.0.1:8000/en-US/app/search/search?q=search source%3D"http%3Asplunk_hec_token"
```

If you want to set a system wide docker logging setting, edit your /etc/docker/daemon.json like so:
```json
{
  "log-driver": "splunk",
  "log-opts": {
    "splunk-token": "secret-token",
    "splunk-url": "https://127.0.0.1:8088",
    "splunk-verify-connection": "false",
    "splunk-insecureskipverify": "true"
  }
}
```

I didn't want it to verify the connection first, because it'll error out starting the docker containers if it can't reach Splunk first. Best to just throw logs that direction and hope for the best.


## gothcas
- You would be a FOOL to think that just because your Mac is running on BSD code base that it's the same as Linux. One MIGHT spend HOURS reconfiguring a completely useless /etc/docker/daemon.json on Mac, only to find out you need to configure the daemon.json through the taskbar (Preferences > Daemon > Advanced).

- Not being familiar enough with Splunk, I kept watching the main search page to see if my new changes were making it to Splunk. APPARENTLY the "What to Search" section and data summary are only for the default idex. If you're putting things in a different index (I had set the index to "logs" in my testing), you need to search for that index specifically to see the results. Even the "last event" counter is only for the default index.

## to-do
* need to tag docker container names
* set-up a universal forwarder
* dashboards and alerts
