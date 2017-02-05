Books
=====

* [High Performance Python](https://www.amazon.co.uk/High-Performance-Python-Performant-Programming/dp/1449361595)
  * A general overview of how to speed up python programs. Starts out with an overview of profiling which I found useful and then covers implementation details to help you make better decisions about how to use the standard python syntax and tools. I got the most value out of these chapters, not having any specific projects I need to speed up but just generally being curious, but I also found the later chapters about numpy, compiling to C and parallelizing interesting.
* [Building Microservices](https://www.amazon.co.uk/gp/product/1491950358/)
  * Mostly just skimmed it, but it seemed like a pretty good overview of why and how to use microservices.
* [Peak](https://www.amazon.co.uk/Peak-Secrets-New-Science-Expertise-x/dp/1847923194/)
  * A book about how to achieve excellence though training by the author who conducted the experiments used by Gladwell to promote the idea of '10,000' hours. While he spends some time debunking, or at least giving context to Gladwell's claims about his research, the book is mostly focused on the evidence for and implementation details of his claims. The book came at the right time for me as I've been spending a lot of time thinking about how to become a better programmer, and use my spare time more effectively.
* [Frankenstein](https://www.amazon.co.uk/Frankenstein-Modern-Prometheus-Wordsworth-Classics/dp/1853260231/)
  * Not much I really need to say here as the book's reputation proceeds it, but I utterly loved it.
* [A Numerate Life](https://www.amazon.co.uk/gp/product/B00TNBPLH4)
  * John Allen Paulos's autobiography, though it spends a lot more time talking about why autobiographies are necessarily bullshit and using examples from mathematics to argue his case. I did find that it dragged a bit, despite it's short length, but overall it enjoyed it. It introduces a lot of interesting mathematical ideas and shows you how to use them to reason about life. Also it has a brief section on the dystopian state of pickup lines in a hypothetical trans-human society. So it has that going for it.

Papers
======

* [Programming as Theory Building](http://pages.cs.wisc.edu/~remzi/Naur.pdf)
  * Argues that programming should be though of not as 'source code production' but as building a theory by which to model the system in question. Thus a programmers job is to come up with a model of how a system works, and how to map that model on to the symbolic manipulations of a computer. And so when a new programmer is to be introduced to the code base, it's not enough to throughly introduce them to the text of the code and give them documentation to read, they must be introduced to the core theory and shown how the text of the program maps onto it. Also, a lot of the paper is spent arguing against formal methods, and I guess it won since I've never heard of any of them?
* [Eliza](https://web.stanford.edu/class/linguist238/p36-weizenabaum.pdf)
  * A paper introducing the worlds first chat bot. Some of the technical details, such as how they used a their time sharing system to make it work are a little lost on me, and it was fascinating to realist I was reading an explanation that seems to come from a time before they were common knowledge. But overall it gave me a good idea of how to implement a version of the bot.
* [Collective dynamics of ‘small-world’ networks](http://barabasilab.neu.edu/courses/phys5116/content/watts_strogatz.pdf)
  * Introduces a network representation that sits between fully regular and fully random, these 'small world' networks start out regular but them have a given number of edges randomly rewired. A few networks in nature are shown to resemble these networks, and it is explained why the small world property should hold true for them.
* [Should Computer Scientists Experiment More?](https://www.cs.princeton.edu/~jrex/teaching/spring2005/fft/moreexperiments.pdf)
  * Argues that computer scientists should conduct more experiments in order to validate ideas that are not fully understood theoretically and make sure efforts are being spent in productive directions, and debunks 16 reasons not to. The arguments certainly sound convincing but I'm hardly in a position to come down too strongly on it.
* [Famine, Affluence, and Morality](http://www.utilitarian.net/singer/by/1972----.htm)
  * An early essay by Peter Singer, that argues we in affluent societies are morally obligated to do far, far more to alleviate suffering that is the norm.
* [What’s Wrong with Git? A Conceptual Design Analysis](https://people.csail.mit.edu/sperezde/onward13.pdf)
  * A critique of 'conceptual mismatch' in the implementation of git, arguing that the tools git provides map poorly onto the problems it's trying to solve. It introduces 'gitless' a git porcelain that introduces a new conceptual framework for git.
  * While the paper makes no reference to the above *Programming as Theory Building* it seems like it strongly supports its thesis. Another way to state it is that while git provides a lot of tools pertinent to the problem it is trying to solve, it provides no core theory on which to map those ideas, resulting in a confusing framework.
* [The Absurd](https://philosophy.as.uky.edu/sites/default/files/The%20Absurd%20-%20Thomas%20Nagel.pdf)
  * Argues against the normal justifications for life being meaningless (The Universe is big, time is long, all will die, etc), and provides it's own justification of meaningless, that however we try to justify our lives we can always take one more step back and see there is nothing inherently supporting those justifications other than self reference. With this new notion it argues against despair or Camus' defiance, but instead that we should regard the absurdity of our lives with a sense of irony. It ends on the note that if nothing truly matters, then the fact none of this matters also doesn't matter.

Blog Posts
==========

* [What can a technologist do about climate change?](http://worrydream.com/ClimateChange/)
  * Fascinating article, with some fascinating visualizations. Discusses ways in which Technologists can help combat global warming.
* [Though as Technology](http://cognitivemedium.com/tat/index.html)
  * Talks about the idea of well designed interfaces as expanding the range of thoughts we can think. As I understood it: The way kind of ideas we can have about a system depend on our mental representation of the system. The role of a good interface designer is to invent new groupings and operations for a particular system, and once a user masters this interface they also master that particular representation.
* [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
  * A succinct explanation of why building distributed systems is hard, and how to make it a bit easier on yourself.
