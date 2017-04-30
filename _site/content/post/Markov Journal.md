+++
date = "2016-06-17"
title = "Markov Journal"

+++



So for a while now I've been keeping a journal using Emacs Org Journal, mostly to chronicle various ideas and to shout at myself. I've had a few problems with it, but I'm mostly quite satisfied, and in contrast to my previous journal tools I love having everything easily accessible in plain text. In fact I was inspired by a friends project to take advantage of this accessibility and use it as a corpus to try and generate automatic journal-like sentences. I thought this project might teach me a little bit about myself, but I was apprehensive since whatever it would teach me was likely to be *horrifically* depressing.

So I thought I'd start out with a simple bigram Markov model. And while I know there are plenty of libraries that implement this for me I've never worked with these kind of things before so I wanted to implement it myself in order to learn more about them. This was my first attempt:

<script src="https://gist.github.com/JKiely/aea941ca3e6d90f14b25f1470835e7e0.js"></script>

And it got me lines like this:

    "so many distractions, it's just need to be noble in the intensity now, I'm using that one last time online, read"

    "never happens. Library. Bring the basic vertion, and then bam, I'm an interveiw for the world if I also need to"

    "the worst thing and just get to redirect my walking will be nervous about how I wonder if it that might be nervous about your fucking"

    
So... yeah... Between my small relatively small corpus and the simplicity of the bigram model it turned out basically nonsensical. Though for all I know, I've actually texted someone the third one at 3am.

I couldn't really do anything about the small size of the corpus but I could improve the model. Rather than just making it spit out trigram models I decided it would be best to make a more general ngram implementation:

<script src="https://gist.github.com/JKiely/76e2766d7506bad5ce5d83008d07eb43.js"></script>

Which worked a bit better and resulted in:

    "Umwelt is a weird millionair who has no plans to let people define custom states."

    "It is rarely the physical injury but the damange to the status of art in itself, and it would be blocked forever"
    
    "I'm there. I need to push myself harder on the scheme book, prepping for the throaty annoyed/exaperated sigh/growl I like the young"


A lot of the results seem like they could be extracts from real text, although I promise my journal was never as creepy as the third one. And yeah, I'm aware that this would have gone a lot smoother if I'd spellchecked my journal as I wrote.

Unfortunately four-grams mostly resulted in it spitting out sentences from the journal verbatim, so I guess I've reached the limit of what I can do with my small corpus with this method. Though I would be interested in mixing the journal files up with other things I've written and trying out some other models on them.

All the code I wrote for this can be found [here](https://github.com/JKiely/markov).
