+++
date = "2016-09-02"
title = "Totes Random"

+++



So it turns out that Haskell doesn't have a random number generator in the same sense python does, one that can be called at any time and return a float between 0 and 1, instead it has a generator which needs a seed in order to produce a number. Naturally the same seed results in the same output each time, making it a little tricky to write a program which requires generating a lot of random numbers. After running into this problem while building the sudoku solver, me, [Sean](https://github.com/phasedchirp), and [Taylor](https://github.com/tayloraburgess) got talking and we had an idea...

Typically RNGs are seeded with unpredictable events such as radioactive decay, or [atmospheric noise](https://www.random.org/). And while we don't have access to that, we do know of a source of noise that's available to everyone, Twitter!

So, in order to capitalize off of this bountiful resource, we set about harvesting tweets to seed our RNG. But not just any tweets would do, no, we wanted only the most statistically valid tweets, so we re-purposed some of Sean's [code](https://github.com/phasedchirp/chirpy-learning) to search the Twitter streaming API for indicative key words:

> "random", "stochastic", "probability", "randos", "entropy", "totes random", "serendipity", "coincidence"," surprise", "bayes", "baes", "laplace", "unlikely", "million to one", "lottery", "las vegas", "monte carlo", "monty python", "MCMC", "astrology"

Once we gathered some tweets we tried a few transformations on them to get a number out of them, such as adding up the ordinal values of the characters, but eventually we settled on hashing them all together. This hash is then fed though a [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) (a pseudo-random number generator which is capable of passing something called the [Diehard tests](https://en.wikipedia.org/wiki/Diehard_tests), which includes the adorably named birthday test), and finally used to seed the native Haskell pseudo-random number generator. That's right, our seeds go though three layers of randomization. We don't skimp on quality here.

<img src="http://www.jkiely.co.uk/images/totes_random.png">

At current we have an API that can return to you a random number between zero and one, and optionally return the tweets that were used to generate it, although so far it's only running on my computer. I did however take the natural next step of building a [twitter bot](https://github.com/JKiely/Totes-Random-Bot) that takes numbers generated from twitter and posts them back to twitter, perhaps even seeding itself. This is also pending our public API before it's up and running properly. For now the code can be viewed [here](https://github.com/JKiely/Totes-Random).
