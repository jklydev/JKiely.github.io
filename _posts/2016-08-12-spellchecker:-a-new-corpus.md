---
layout: post
---

Since the last post I've made a few changes, including making progress on getting the site working again. But the most important thing I've done is to finally get it working with the Open American National Corpus. This has raised my total unique words from ~30,000 to ~150,000... and decreased my correction speed from ~5 incorrect words per second to just over 1 wsp. So it seems my current approach is not scalable, and I need to make some changes. I see three immediate options:

1. Pruning the known list: If I dropped all words that only appear only once (~60,000) I could get a bit of a speed increase. But frankly this isn't very appealing, increasing my speed by around a third really isn't that impressive and will still be far too slow. Not to mention this actually costs me quite a bit of functionality, as it's rare words like that which most often need checking. Dropping unique trigrams and bigrams may however reduce the amount of memory I consume, without any great loss of accuracy.

2. Reducing the possible words: Right now an unknown word is checked against every known word, if I could find some way to only check it against a plausible subset then it would reduce the time taken greatly. However, actually finding such an implementation is tricky, though one half solution would be to run the edit distance function first and drop the rest of the calculation if it's over a given number. This could save me a lot of time of lookups which eat up a lot of time.

3. Rewrite the whole damn thing in Cython. By writing it in Cython and declaring my types I could potentially make it much, much faster. The only downside is the work I'd have to put in rewriting it, but I'd actually like to get some experience with Cython so that doesn't bother me that much. 

These options aren't mutually exclusive and I'll continue to explore all three, but my focus for now is likely to be on the second and third options.

Another possibility that I'm exploring is the [Trie](https://en.wikipedia.org/wiki/Trie) data structure for handling some of my look ups, it could certainly speed up parts of the program, but I don't think it will help with any of my main bottlenecks.

The other issue I discussed before that I'm still dealing with is the lack of good test data. However I think I might have a solution to this problem now. If I get another collection of text I can write a program that pulls from it a random selection of trigrams and make a spelling error with the middle word*, while remembering the original word so I can verify my correction. This has two advantages, firstly it allows me to generate as much data as I like to test on, which will help avoid over fitting, and secondly it can record what kind of spelling error it's making so I can check if I'm failing on any particular class of them. The actual function that makes random errors might pose some difficulty, depending on how technical I want to get with it, but the most common categories of errors in English spelling are documented and I'm sure I could automate a portion of them.


*Only the words on each side affect the correction, pulling out more would be redundant.
