---
layout: post
title:  "Mr. Robot's Bootstraps"
date:   2020-01-13 06:00:28 -0700
tags: ansible bash automation vagrant
---

Watching Mr. Robot, it occurred to me that Elliot is almost always on a new system. He's either using a live system ([Kali Linux](https://www.kali.org/)), on someone else's computer, or he's just finished microwaving his RAM. But there's no way that he's always using default set-ups. Right? He wouldn't use nano and bash for his late night coding. He'd have custom python modules, elaborate nmap scripts, and a million zsh aliases. So how does he have time to set up his environments?

<center>
  <iframe src="https://giphy.com/embed/ZKQpx4TYrxTtS" width="336" height="321" frameBorder="0" allowFullScreen>
  </iframe>
</center>

I think that he probably has some automated scripts sitting out on the internet somewhere. Scripts that will install everything he needs and configure all the dotfile to his liking. Sitting on some AWS server paid for anonymously, who's IP address he has memorized. His own personal bootstrap kit floating in the cloud...I want one!

## My Bootstraps

While this was a fun thought experiment, it's also been on my to-do list for a while. I spend too much time setting up new systems or VMs. Plus, I can never remember how I got the directory colors just right so it's readable in dark theme terminals. It'd be nice to stop fighting that.

## Design

Needs to be:
1. **Fast**. Mr. Robot needs to go from zero to writing exploits in less than a minute.
2. **Versatile**. I could probably stuff it all in a bash script, but that'd be a pain for more complex stuff like updating dotfiles based on programs installed or if it's a work system or personal.
3. **Easy**. No long commands to memorize or type. No flags I can't remember.
4. **Fully headless**. I don't know, just because I like not being tied to a GUI.

I went with [ansible](https://www.ansible.com/) because it seemed better suited for provisioning a localhost. You can do the same with salt or chef, but you have to make some config changes before you can. Ansible just worked out of the box for what I needed.

All the ansible "playbooks" are obviously in a git repo. But I didn't want to type out a long git clone command, so I wrote a bootstrap for my bootstrap! Just a quick bash script that would install git and ansible, then clone my repo full of the playbooks. This saves me time and about 5 lines of commands.

So this part I'm really pleased with myself about: **I stored this bootstrap bootstrap script in the root directory of this site!** Here it is:
<a href="https://shaungarwood.com/bs.sh">shaungarwood.com/bs.sh</a>

[Here](https://github.com/shaungarwood/my_bootstraps/blob/master/bin/initial-bootstrap.sh) is the github link if you just want to check out my bash scripting skillz.

<center>
  <iframe src="https://giphy.com/embed/146OLb5nrHt3Co" width="240" height="240" frameBorder="0" class="giphy-embed" allowFullScreen>
  </iframe>
</center>

This means that all I need to type to begin setting up a new linux host is:
```wget shaungarwood.com/bs.sh```

## Solution

In fact the full solution is a total 3 lines long!

```bash
wget shaungarwood.com/bs.sh
bash bs.sh
ansible-playbook my_bootstraps/tasks/*.yml
```

Gorgeous, isn't it? This simple beauty probably saves me half a day of manually installing/configuring things.

Yeah, yeah - I could pipe the result of wget into bash and have the script run the ansible-playbook command which would mean the final solution is just one command. But that would require a few wget flags and I don't always want to run ALL the playbooks. Three simple commands is fine with me.

Full repo:
<a href="https://github.com/shaungarwood/my_bootstraps">https://github.com/shaungarwood/my_bootstraps</a>

## Other concerns

I just want to address the pedantic nerd voice in my head.

> This isn't secure! You're blindly running a bash script that could compromise your whole computer!

Okay, yes. Someone could theoretically hack into my github account or man-in-the-middle my wget. That's a weird amount of work just so they can own my raspberry pi. If I were Mr. Robot - I'd probably memorize the checksum of the bash script so I'd know if someone messed with it. I'm not going to do that.

> You're downloading the script from your personal website? Goodbye anonymity.

Yeah, it doesn't get more personal on a fresh system than having the first command contain my full name. If I'm trying to stay mysterious, I won't use this project. Elliot would probably just host the script on a public e-corp server he hacked.

## Demo

Okay, ready to see it in action? A <a href="https://asciinema.org/a/oOVnonDr00420VksGn99HN8H9">link</a> in case it doesn't load right.

<center>
  <script id="asciicast-oOVnonDr00420VksGn99HN8H9" src="https://asciinema.org/a/oOVnonDr00420VksGn99HN8H9.js?speed=1.1&size=medium" async>
  </script>
</center>

<center>
  <iframe src="https://giphy.com/embed/RPwrO4b46mOdy" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen>
  </iframe>
</center>
<center><b>YATTA!</b></center>


Want to try it out yourself? Here's a full run Vagrant demo using ubuntu and centos:
```ruby
Vagrant.configure("2") do |config|
  $script = <<-SCRIPT
  wget shaungarwood.com/bs.sh
  bash bs.sh
  ansible-playbook ~/my_bootstraps/tasks/basic.yml
  SCRIPT

  config.vm.provision "shell", inline: $script, privileged: false

  config.vm.define "centos" do |centos|
    centos.vm.box = "bento/centos-7.2"
    centos.vm.hostname = "centos"
  end

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "bento/ubuntu-18.04"
    ubuntu.vm.hostname = "ubuntu"
  end
end
```

And finally, here is the repo so you can check it out yourself:
<a href="https://github.com/shaungarwood/my_bootstraps">https://github.com/shaungarwood/my_bootstraps</a>

Even if you don't know ansible, you should check it out. All the magic is in the "tasks" directory. It's very human readable and easy to start hacking up to make your very own bootstrap kit in the cloud.

Edit (2020/01/14): Fixed the vagrant demo code. It was running everything as root, fixed with ```privileged: false```.
