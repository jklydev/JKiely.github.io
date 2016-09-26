Last night, in a fit of sleeplessness, I decided to utterly over hall all of the tools I use on my laptop: Switching from emacs to Atom (with vim mode), from Chrome to Vivaldi, and from bash to zsh. I've really only spent a day with them all so far but I'm going to report my initial impressions:

Vivaldi
--------
I suspect Vivaldi is the one that you're least likely to have heard of, it's a newish browser (1.0 came out last April) from one of the people who brought us the Opera browser. It's aimed at power uses (read: people who hate using the mouse), especially those who were annoyed by some of the more recent changes to the Opera browser that removed features.

It's built on top of Chromium, which means it has access to all of Chrome's add-ons, so I don't have to worry about losing Lastpass, Pushbullet, or any of the other add-ons I really don't want to leave behind.

So far I'm really liking Vivaldi. I love the speed dial on new tabs, and how I can have multiple speed dial 'tabs' for different kinds of bookmarks. It's pretty much made the book-mark bar obsolete for me. The default keyboard shortcuts are really well though out, and really easy to customize. You can pretty much do everything without the mouse. My first instinct was to customize them to superficially resemble emacs keyboard shortcuts, and that was pretty easy to do (though I had to reassign some of the shortcuts that already occupied those key combinations), but if I'm going to take the trouble of learning vim I might as well go forward with the vim shortcuts.

In fact the only thing I dislike about it so far is that among all the customizability, the few things I can't change (or haven't figure out how to change yet), stand out all the more. I want to hide the extension icons in the menu bar, or hide and show my tabs on a button press, but I have no idea how.

Atom
--------------------
Well I'm writing this post in Atom, so the first thing I should point out is how much I like the markdown preview mode. It updates as I type, it renders pretty much exactly like it does on the web, and it even loads images from the web when I use image tags. I think at some point I'd like to figure out how to give it a css file so that it shows me exactly what it will look like on my site, but I'm really happy with it for now.

I also love having tabs again, being able to see what's in each buffer and drag them around makes working with many files a lot more pleasant that it was in emacs (and yes, I'm sure I could have configured emacs to do that somehow, but I doubt it would have been as smooth).

But frankly I do miss emacs. Having the power to do a few additional things that I wanted to do with the mouse don't really make up for all the things I can't do without the mouse. I miss emacs file opening functionality, which allowed me to open a file with it's path and then set its directory as the working directory for that buffer. I've tried some extensions that give me more functionality than the atom defaults but so far they all lack something. And I'm sure that as I continue I'll find more and more things I miss.

Atom (with Vim mode)
--------------------
Vim is taking some getting use to. The lurches back towards emacs shortcuts don't really surprise me, but what's really been getting to me is that when moving the cursor I'm expected to keep my fingers *just a little* offset from their normal position on the home row. As a result of this I'm repeatedly using my normal touch-typing muscle memory and pushing one key to the right of what I'm aiming for. Which most often means pushing `u` when I meant to push `i` and undoing whatever I did last.

The other issue if that the general philosophy of 'modes' doesn't fit will with how I typically work. I tend to back track a lot and having to switch every time I want to correct the variable name I just wrote is a bit of a hassle. But to be honest, it's probably a far more productive way of working and I should give it a chance (this draft is currently full of typos that I'm struggling not to correct).

The reason I'm so interested in switching, despite the hassle of switching over is that the more familiar I became with emacs shortcuts the more I wanted to use them **everywhere**. But this is a bit of a problem, because emacs shortcuts use a pretty popular set of keys. I'd have to utterly reconfigure every app I used if I wanted to have `cmd-n` and `cmd-p` for up and down. But vim with it's assumption of modes makes it much easier to use those short cuts everywhere else, I just need to free up one key for switching modes. Just as importantly it makes it easy to use the short cuts I've become accustomed to everywhere else in my editor. No more constantly mixing up cut and yank.

Zsh
----
Zsh is the tool I've used the least of the ones in this post. So far all I can really say is that all my bash knowledge has carried over and it was really easy to set up (using oh-my-zsh). But I'm excited to get a chance to use it some more.

### Outro
This is probably too many changes at once, and I'm sure I'll come to hate the John of yesterday over the course of the next few weeks as my productivity goes to shit. But hopefully the John of six months for now looks back on all of these changes favorably!

Frankly the John of right now is just glad I managed to talk myself out of migrating my blog to Hugo and redoing the css before writing this post.
