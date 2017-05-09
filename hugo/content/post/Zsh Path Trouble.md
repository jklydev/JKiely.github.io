+++
date = "2016-10-04"
title = "Zsh Path Trouble"

+++



I've been loving Zsh since switching over, but yesterday I had my first problem with it: When I tried running a python 3 program, it couldn't find any packages. A quick `exec bash -l` let me check that they still worked with bash, so it probably wasn't a python thing, but a zsh thing. It grew even stranger when it turned out that it could still find all of my old python 2 packages just fine, as well as run the 2.7 version of Ipython in the command line.

I don't really understand the shell all that well yet, so this post really just describes how I went about trying to fix this using the little knowledge I do have, a lot of this might be wrong and/or unsafe. If you just want to see how I actually did solve it then skip to the second to last paragraph.

So my first though was that this was likely to have something to do with Conda, having used that to install my python 3. My next (kinda stupid) thought was that maybe my python 3 package path (in the anaconda directory) needed to be added to my $PATH? So I checked where that was:

```py
import site
site.getsitepackages() #=> ['/Users/jkiely/anaconda/lib/python3.5/site-packages']
```

Added it ... and of course that didn't work. A quick check of my path on bash showed that I didn't have the packages there ether. But it did show that I had the Conda python 3 in my path on bash but not on Zsh. Wait... so how was I even getting python 3 to run on zsh them? I checked `which python3` on zsh and it turns out that unbeknownst to me I had a second python 3 installation on my system in `/usr/local/bin` and when I ran python 3 it was using that.

So that helps me a bit. I have no idea how the anaconda version ended up in my bash path but not my zsh one, since it's not in my bashrc, but I add it to zshrc and... nothing. It's still calling the wrong python. Hmm, so I think the shell uses the first binary of that name that it finds in the path right? What if I move it to the top of my 'export to path' list? Nope, still wrong version. Ok how about I try this changing `PATH=$PATH:/path/to/anaconda` to `PATH=/path/to/anaconda/:$PATH` ensuring that it's added to the front of the path regardless of when it's exported. And... it works!

This solution feels a bit hacky, and I'm pretty sure that the right way to solve it, and thus the next step, is to figure out how to use virtual environments to specify exactly what version of python I want use with each project. But for now I'm glad I can at run python 3 programs at all.
