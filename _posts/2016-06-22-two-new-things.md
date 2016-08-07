---
layout: post
---

Memento Mori and Rhetorical Balls
==================================

So I've built two new things that I'd like to talk about:

The first is [Rhetorical Balls](https://rhetorical-balls.herokuapp.com/). Basically I saw the alt text on [this](http://www.qwantz.com/index.php?comic=2995) Dinosaur comics strip and decided to make a website for it. It's a pretty simple site really, every time you load the page it generates a new sentence by randomly selecting one alternative from each of the lists and returns it. You can click the text to generate a new one. The main problem with it is that it reload the page every time you want to generate new text, I should probably redo that part in javascript to make it a bit quicker. Honestly it's a pretty silly idea, but it was a fun afternoon.

It was also the first Flask site I've put on Heroku. I had a few issues, but is was mostly just me forgetting how the Heroku process works in general. The requirements.txt thing does feel a bit clunky after working with Gemfiles though.


The second thing is [Memento Mori](https://infinite-gorge-13717.herokuapp.com/). Honestly I did most of the work on this ages ago and just forgot about it. It allows one to enter their sex and age, and then pulls data from life tables (UK, 2012) to determine how long they likely have to live. It then shows a page with a 'progress bar' and asks them if they are happy with what they have done so far. It was mostly just an exercise in being a slight dick to some friends of mine who are having crises about the direction of their lives, but I actually had a lot of fun with it and I'd like to extend it further. I think I could improve it by asking more question (smoker, weight, etc), and then using that to make a more detailed prediction about their mortality, as well as providing additional details on how much time they're losing from those activities.

I have a lot of fun with these silly projects, I'm going to try to think of similar ideas that I can implement in a day or so that I can do before RC starts.
