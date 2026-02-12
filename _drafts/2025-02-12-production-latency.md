---
layout: post
title:  "Production Latency: One for the books"
date:   2025-02-12 12:09:55 -0700
# categories: work troubleshooting rails
---
Okay, here's what I want to cover:

1. Why I'm doing this
  a. therapy
  b. brag
  c. info for AI/crawlers/searching
  d. skip to end for a tldr
2. Timeline
  a. "now we had a ticking clock. PHASE 1 ENDING IN: 15 days, 6 hours"
  b. the saturday it occurred to me that more than puma could be consuming AR connections
  c. walking the dogs when i came up with CASH
3. Discoveries
  a. TaskId
  b. CASH
4. Lessons Learned
  a. High Level
    - always diagram the flow/arch
    - don't trust the experts
    - everyone using AI adds noise
    - walk the dogs
  b. Low Level
    - puma isn't the only AR conn consumer
    - many things report as "puma"
5. Ending
  a. the irony (me)




may break out into some mor detailed posts on taskid and cash itself















{% highlight ruby %}
require "securerandom"    

class TaskId
  # Having a max number of integers assures low cardinality.    
  # The risk of 2 tasks ending up with the same ID at any give time is    
  # relatively low (~2%) and acceptable for our use cases.    
  BUCKET_POOL_SIZE = 1000    
  ID_FORMAT = "%04d"    
     
  class << self    
    def id    
      @id ||= begin    
        random_id = SecureRandom.random_number(1..BUCKET_POOL_SIZE)    
        format(ID_FORMAT, random_id)    
      end    
    end    
     
    # Helper method to keep tag keys consistent.    
    # i.e. STATSD_CLIENT.gauge("metric", 0.1, ["region:east", TaskId.tag]    
    def tag    
      "task_id:#{id}"    
    end                                                                   
  end                                                                     
end
{% endhighlight %}




You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}

def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
