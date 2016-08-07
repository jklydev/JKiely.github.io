---
layout: post
---

So my first week at Recurse Center is over (it still feel odd to write centre 'center', even if I usually prefer American spelling). It's been fun, and tiring. Unsurprisingly my resolve to work exclusively on python web stuff and theory has been shaken by talking to people and seeing what everyone else is working on. The intention to learn some theory has more or less gone out of the window, I think I'll get far more out of this if I focus on more practical pursuits. As for python, well I wanted to get good at at least one language before I branched out to learn others, but as I talk to people I'm starting to think that I'd be a lot better off learning at least one other. Another language will give me a point of comparison, and help me to understand what parts of my python programs are just the way the computer does things, or just the way python does things. In the same way that learning another human language gives you a better grasp of your own, learning another programming language could accelerate my understanding of python.

Of course that still leave the matter of which one. My first thoughts go to javascript, I am hoping to become a web programmer after all. But while I do hope do at least one project in javascript while I'm here, I really don't want to focus on it. I expect I'll need to know some, but frankly it doesn't interest me that much, and I don't think it's the best choice for my mostly back end interests. The two that really do appeal to me are Go and Elixer. But I'll weight the two up later, in a different post.

The thing that has stayed constant is my desire to collaborate and spend as much time working with others as possible. And I got off to a good start this week by pairing on a Markov bot (which I'll talk about in a moment). It really surprised me though how much pairing and having to articulate concept in the program takes it out of me. Far more than coding alone. I guess that's just another reason why I should practice it!

As for the actual projects I've been working on, there have been two:

As I said, the first is a [Markov bot](https://github.com/JesseRap/ngram) similar to my previous Markov journal project. The difference is that it always starts with a word that was found at the start of a sentence in the original corpus and always ends with a word that ended one (and a proper punctuation mark). It was surprisingly difficult to get only the words that started sentences into a separate dict, but after experimenting with a lot of regex ("(?<=[.?!]\s)[A-Z][a-z']+\|(?<=[\n])[A-Z][a-z']+"), we eventually settled on turning the doc into a list of words and punctuation marks using re.split and grabbing all the words that came after an end marker ('.', '!', or '?'). After that it continued generating text as usual until it hit another end stopper (which were treated as words by the program) and returns the sentence.

Here are some examples from when it was trained on the bible:

    Jesus saith it was upon the kingdom which I kept the Jews?
    
    And he shall condemn the flock in the shadow dwelt there come.

    And it to him as it.

It's not exactly biblical, but we're getting there. We're both pretty interested in language generation, it would be fun to try another more advanced approach.

The second thing I've been working on is trying to implement a server in python. This is part of my effort to better understand web programming by learning exactly what happens between the code I write and it appearing in the browsers. I've been following a series of [blog posts](https://ruslanspivak.com/lsbaws-part1/) that explain how a server works, and implementing all the example python code before looking up every library function he calls in the documentation and [annotating](https://github.com/JKiely/server/blob/master/main.py) it. I think I'm getting a pretty good understanding, I'll try writing it up when I'm finished with the project.

So that's week one. Frankly I'm frightened that I only have 11 left, There's so much more I want to do.
